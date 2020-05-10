
import json
import logging
from django import forms
from django.db import models
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager

from wagtail.core.models import PageBase, Page, Orderable
from wagtail.core.fields import (
    RichTextField,
    StreamField,
)

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.utils import resolve_model_string
from wagtail.search import index
from wagtail.utils.decorators import cached_classmethod
from wagtailcache.cache import WagtailCacheMixin

from taggit.models import TaggedItemBase
from wagtail.admin.edit_handlers import (
    HelpPanel,
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    ObjectList,
    PageChooserPanel,
    StreamFieldPanel,
    TabbedInterface
)

from blocks.models import (
    CONTENT_STREAMBLOCKS,
    LAYOUT_STREAMBLOCKS,
    # STREAMFORM_BLOCKS,
    ContentWallBlock,
    OpenHoursBlock,
    StructuredDataActionBlock,
)

from blocks.snippets import CategoryTerm
from blocks.widgets import CategorySelectWidget
# from common import schema
from common.wagtailsettings_models import GeneralSettings, LayoutSettings, SeoSettings, GoogleApiSettings  # noqa

logger = logging.getLogger('coral')

FRONTEND_TEMPLATES_PAGES = {
    # templates that are available for all page types
    '*': (
        ('', 'Default'),
        ('pages/web_page.html', 'Web page showing title and cover image'),
        ('pages/web_page_notitle.html', 'Web page without title and cover image'),
        ('pages/home_page.html', 'Home page without title and cover image'),
        ('pages/base.html', 'Blank page - no navbar or footer'),
    ),
}

CORAL_PAGE_MODELS = []

def get_page_models():
    return CORAL_PAGE_MODELS

class CoralPageMeta(PageBase):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        if 'amp_template' not in dct:
            cls.amp_template = None
        if 'search_db_include' not in dct:
            cls.search_db_include = False
        if 'search_db_boost' not in dct:
            cls.search_db_boost = 0
        if 'search_filterable' not in dct:
            cls.search_filterable = False
        if 'search_name' not in dct:
            cls.search_name = cls._meta.verbose_name
        if 'search_name_plural' not in dct:
            cls.search_name_plural = cls._meta.verbose_name_plural
        if 'search_template' not in dct:
            cls.search_template = 'pages/search_result.html'
        if not cls._meta.abstract:
            CORAL_PAGE_MODELS.append(cls)

class CoralTag(TaggedItemBase):
    class Meta:
        verbose_name = _('Coral Tag')
        
    content_object = ParentalKey('pages.CoralPage', related_name='tagged_items')

class CoralPageMixin(models.Model):
    class Meta:
        abstract = True

    ###############
    # Content fields
    ###############

    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Cover image'),
    )

    # ###############
    # # SEO fields
    # ###############

    og_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Open Graph preview image'),
        help_text=_("The image shown when linking to this page on social media. If blank, defaults to article cover image, or logo in Settings > Layout > Logo"),  # noqa
    )

    ###############
    # Settings
    ###############

    content_walls = StreamField(
        [
            ('content_wall', ContentWallBlock())
        ],
        blank=True,
        verbose_name=_('Content Walls')
    )

    ###############
    # Panels
    ###############

    content_panels = [
        ImageChooserPanel('cover_image'),
    ]

    body_content_panels = []

    bottom_content_panels = []

    # category_panels = []

    # layout_panels = []

    promote_panels = [
        MultiFieldPanel(
            [
                FieldPanel('slug'),
                FieldPanel('seo_title'),
                FieldPanel('search_description'),
                ImageChooserPanel('og_image'),
            ],
            _('Page Meta Data')
        ),
    ]

    settings_panels = [
        StreamFieldPanel('content_walls'),
    ]

    # integration_panels = []

    def __init__(self, *args, **kwargs):
        """
        Inject custom choices and defaults into the form fields
        to enable customization by subclasses.
        """
        super().__init__(*args, **kwargs)

    @cached_classmethod
    def get_edit_handler(cls):
        """
        Override to "lazy load" the panels overriden by subclasses.
        """
        panels = [
            ObjectList(
                cls.content_panels + cls.body_content_panels + cls.bottom_content_panels,
                heading=_('Content')
            ),
            # ObjectList(cls.category_panels, heading=_('Category')),
            # ObjectList(cls.layout_panels, heading=_('Layout')),
            ObjectList(cls.promote_panels, heading=_('SEO'), classname="seo"),
            ObjectList(cls.settings_panels, heading=_('Settings'), classname="settings"),
        ]

        # if cls.integration_panels:
        #     panels.append(ObjectList(
        #         cls.integration_panels,
        #         heading='Integrations',
        #         classname='integrations'
        #     ))

        return TabbedInterface(panels).bind_to(model=cls)


    def get_content_walls(self, check_child_setting=True):
        current_content_walls = []
        if check_child_setting:
            for wall in self.content_walls:
                if wall.value['show_content_wall_on_children']:
                    current_content_walls.append(wall.value)
        else:
            current_content_walls = self.content_walls

        try:
            return list(current_content_walls) + self.get_parent().specific.get_content_walls()
        except AttributeError:
            return list(current_content_walls)

  

class CoralPage(WagtailCacheMixin, Page, metaclass=CoralPageMeta):
    """
    General use page with caching and templating functionality.
    All pages should inherit from this.
    """
    class Meta:
        verbose_name = _('Coral Page')
        # abstract = True

    # Do not allow this page type to be created in wagtail admin
    is_creatable = False

    # Templates
    # The page will render the following templates under certain conditions:
    #
    # template = ''
    # amp_template = ''
    # ajax_template = ''
    # search_template = ''

    ###############
    # Content fields
    ###############

    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Cover image'),
    )

    ###############
    # Index fields
    ###############

    # Subclasses can override this to enabled index features by default.
    index_show_subpages_default = False

    # Subclasses can override this to query on a specific
    # page model, rather than the default wagtail Page.
    index_query_pagemodel = 'pages.CoralPage'

    # Subclasses can override these fields to enable custom
    # ordering based on specific subpage fields.
    index_order_by_default = ''
    index_order_by_choices = (
        ('', _('Default Ordering')),
        ('-first_published_at', _('Date first published, newest to oldest')),
        ('first_published_at', _('Date first published, oldest to newest')),
        ('-last_published_at', _('Date updated, newest to oldest')),
        ('last_published_at', _('Date updated, oldest to newest')),
        ('title', _('Title, alphabetical')),
        ('-title', _('Title, reverse alphabetical')),
    )
    index_show_subpages = models.BooleanField(
        default=index_show_subpages_default,
        verbose_name=_('Show list of child pages')
    )
    index_order_by = models.CharField(
        max_length=255,
        choices=index_order_by_choices,
        default=index_order_by_default,
        blank=True,
        verbose_name=_('Order child pages by'),
    )
    index_num_per_page = models.PositiveIntegerField(
        default=10,
        verbose_name=_('Number per page'),
    )

    index_categories = ParentalManyToManyField(
        'blocks.Category',
        blank=True,
        verbose_name=_('Filter child pages by'),
        help_text=_('Enable filtering child pages by these categories.'),
    )

    ###############
    # Layout fields
    ###############

    # custom_template = models.CharField(
    #     blank=True,
    #     max_length=255,
    #     choices=None,
    #     verbose_name=_('Template')
    # )

    ###############
    # Categorize
    ###############

    category_terms = ParentalManyToManyField(
        'blocks.CategoryTerm',
        blank=True,
        verbose_name=_('Categories'),
        help_text=_('Categorize and group pages together. Used to organize and filter pages across the site.'),  # noqa
    )
    tags = ClusterTaggableManager(
        through=CoralTag,
        blank=True,
        verbose_name=_('Tags'),
        help_text=_('Used to organize pages across the site.'),
    )

    ###############
    # Settings
    ###############

    content_walls = StreamField(
        [
            ('content_wall', ContentWallBlock())
        ],
        blank=True,
        verbose_name=_('Content Walls')
    )

    ###############
    # Search
    ###############

    search_fields = [
        index.SearchField('title', partial_match=True, boost=3),
        index.SearchField('search_description', boost=2),
        index.FilterField('title'),
        index.FilterField('id'),
        index.FilterField('live'),
        index.FilterField('owner'),
        index.FilterField('content_type'),
        index.FilterField('path'),
        index.FilterField('depth'),
        index.FilterField('locked'),
        index.FilterField('first_published_at'),
        index.FilterField('last_published_at'),
        index.FilterField('latest_revision_created_at'),
        index.FilterField('index_show_subpages'),
        index.FilterField('index_order_by'),
        # index.FilterField('custom_template'),
        index.FilterField('category_terms'),
    ]

    ###############
    # Panels
    ###############

    content_panels = Page.content_panels + [
        ImageChooserPanel('cover_image'),
    ]

    body_content_panels = []

    bottom_content_panels = []

    category_panels = [
        FieldPanel('category_terms', widget=CategorySelectWidget()),
        FieldPanel('tags'),
    ]

    layout_panels = [
        # MultiFieldPanel(
        #     [
        #         FieldPanel('custom_template')
        #     ],
        #     heading=_('Visual Design')
        # ),
        MultiFieldPanel(
            [
                FieldPanel('index_show_subpages'),
                FieldPanel('index_num_per_page'),
                FieldPanel('index_order_by'),
                FieldPanel('index_categories', widget=forms.CheckboxSelectMultiple()),
            ],
            heading=_('Show Child Pages')
        )
    ]

    promote_panels = []

    settings_panels = Page.settings_panels + [
        StreamFieldPanel('content_walls'),
    ]

    integration_panels = []

    def __init__(self, *args, **kwargs):
        """
        Inject custom choices and defaults into the form fields
        to enable customization by subclasses.
        """
        super().__init__(*args, **kwargs)
        klassname = self.__class__.__name__.lower()
        template_choices = FRONTEND_TEMPLATES_PAGES.get('*', ()) + \
            FRONTEND_TEMPLATES_PAGES.get(klassname, ())

        self._meta.get_field('index_order_by').choices = self.index_order_by_choices
        # self._meta.get_field('custom_template').choices = template_choices
        if not self.id:
            self.index_order_by = self.index_order_by_default
            self.index_show_subpages = self.index_show_subpages_default

    @cached_classmethod
    def get_edit_handler(cls):
        """
        Override to "lazy load" the panels overriden by subclasses.
        """
        panels = [
            ObjectList(
                cls.content_panels + cls.body_content_panels + cls.bottom_content_panels,
                heading=_('Content')
            ),
            ObjectList(cls.category_panels, heading=_('Category')),
            ObjectList(cls.layout_panels, heading=_('Layout')),
            # ObjectList(cls.promote_panels, heading=_('SEO'), classname="seo"),
            ObjectList(cls.settings_panels, heading=_('Settings'), classname="settings"),
        ]

        if cls.integration_panels:
            panels.append(ObjectList(
                cls.integration_panels,
                heading='Integrations',
                classname='integrations'
            ))

        return TabbedInterface(panels).bind_to(model=cls)

    # def get_template(self, request, *args, **kwargs):
    #     """
    #     Override parent to serve different templates based on querystring.
    #     """
    #     if 'amp' in request.GET and hasattr(self, 'amp_template'):
    #         seo_settings = SeoSettings.for_site(request.site)
    #         if seo_settings.amp_pages:
    #             if request.is_ajax():
    #                 return self.ajax_template or self.amp_template
    #             return self.amp_template

    #     if self.custom_template:
    #         return self.custom_template

    #     return super(CoralPage, self).get_template(request, args, kwargs)

    def get_index_children(self):
        """
        Returns query of subpages as defined by `index_` variables.
        """
        if self.index_query_pagemodel:
            querymodel = resolve_model_string(self.index_query_pagemodel, self._meta.app_label)
            query = querymodel.objects.child_of(self).live()
        else:
            query = self.get_children().live()
        if self.index_order_by:
            return query.order_by(self.index_order_by)
        return query

    def get_content_walls(self, check_child_setting=True):
        current_content_walls = []
        if check_child_setting:
            for wall in self.content_walls:
                if wall.value['show_content_wall_on_children']:
                    current_content_walls.append(wall.value)
        else:
            current_content_walls = self.content_walls

        try:
            return list(current_content_walls) + self.get_parent().specific.get_content_walls()
        except AttributeError:
            return list(current_content_walls)

    def get_context(self, request, *args, **kwargs):
        """
        Add child pages and paginated child pages to context.
        """
        context = super().get_context(request)

        if self.index_show_subpages:
            # Get child pages
            all_children = self.get_index_children()
            # Filter by category terms if applicable
            if len(request.GET) > 0 and self.index_categories.exists():
                # Look up comma separated CategoryTerm slugs i.e. `/?c=term1-slug,term2-slug`
                terms = []
                get_c = request.GET.get('c', None)
                if get_c:
                    terms = get_c.split(',')
                # Else look up individual querystrings i.e. `/?category-slug=term1-slug`
                else:
                    for category in self.index_categories.all().only('slug'):
                        get_term = request.GET.get(category.slug, None)
                        if get_term:
                            terms.append(get_term)
                if len(terms) > 0:
                    selected_terms = CategoryTerm.objects.filter(slug__in=terms)
                    context['selected_terms'] = selected_terms
                    if len(selected_terms) > 0:
                        try:
                            for term in selected_terms:
                                all_children = all_children.filter(category_terms=term)
                        except AttributeError:
                            logger.warning(
                                "Tried to filter by CategoryTerm, but <%s.%s ('%s')>.get_index_children() did not return a queryset or is not a queryset of CoralPage models.",  # noqa
                                self._meta.app_label,
                                self.__class__.__name__,
                                self.title
                            )
            paginator = Paginator(all_children, self.index_num_per_page)
            pagenum = request.GET.get('p', 1)
            try:
                paged_children = paginator.page(pagenum)
            except (PageNotAnInteger, EmptyPage, InvalidPage) as e:  # noqa
                paged_children = paginator.page(1)

            context['index_paginated'] = paged_children
            context['index_children'] = all_children
        context['content_walls'] = self.get_content_walls(check_child_setting=False)
        return context


class CoralSEOPage(CoralPage):
    """
    General use page with caching, templating, and SEO functionality.
    All pages should inherit from this.
    """
    class Meta:
        verbose_name = _('Coral SEO Page')
        # abstract = True

    # Do not allow this page type to be created in wagtail admin
    is_creatable = False

    # ###############
    # # SEO fields
    # ###############

    og_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Open Graph preview image'),
        help_text=_("The image shown when linking to this page on social media. If blank, defaults to article cover image, or logo in Settings > Layout > Logo"),  # noqa
    )
    # struct_org_type = models.CharField(
    #     default='',
    #     blank=True,
    #     max_length=255,
    #     choices=schema.SCHEMA_ORG_CHOICES,
    #     verbose_name=_('Organization type'),
    #     help_text=_('If blank, no structured data will be used on this page.')
    # )
    # struct_org_name = models.CharField(
    #     default='',
    #     blank=True,
    #     max_length=255,
    #     verbose_name=_('Organization name'),
    #     help_text=_('Leave blank to use the site name in Settings > Sites')
    # )
    # struct_org_logo = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     verbose_name=_('Organization logo'),
    #     help_text=_('Leave blank to use the logo in Settings > Layout > Logo')
    # )
    # struct_org_image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     verbose_name=_('Photo of Organization'),
    #     help_text=_('A photo of the facility. This photo will be cropped to 1:1, 4:3, and 16:9 aspect ratios automatically.'),  # noqa
    # )
    # struct_org_phone = models.CharField(
    #     blank=True,
    #     max_length=255,
    #     verbose_name=_('Telephone number'),
    #     help_text=_('Include country code for best results. For example: +1-216-555-8000')
    # )
    # struct_org_address_street = models.CharField(
    #     blank=True,
    #     max_length=255,
    #     verbose_name=_('Street address'),
    #     help_text=_('House number and street. For example, 55 Public Square Suite 1710')
    # )
    # struct_org_address_locality = models.CharField(
    #     blank=True,
    #     max_length=255,
    #     verbose_name=_('City'),
    #     help_text=_('City or locality. For example, Cleveland')
    # )
    # struct_org_address_region = models.CharField(
    #     blank=True,
    #     max_length=255,
    #     verbose_name=_('State'),
    #     help_text=_('State, province, county, or region. For example, OH')
    # )
    # struct_org_address_postal = models.CharField(
    #     blank=True,
    #     max_length=255,
    #     verbose_name=_('Postal code'),
    #     help_text=_('Zip or postal code. For example, 44113')
    # )
    # struct_org_address_country = models.CharField(
    #     blank=True,
    #     max_length=255,
    #     verbose_name=_('Country'),
    #     help_text=_('For example, USA. Two-letter ISO 3166-1 alpha-2 country code is also acceptible https://en.wikipedia.org/wiki/ISO_3166-1'),  # noqa
    # )
    # struct_org_geo_lat = models.DecimalField(
    #     blank=True,
    #     null=True,
    #     max_digits=10,
    #     decimal_places=8,
    #     verbose_name=_('Geographic latitude')
    # )
    # struct_org_geo_lng = models.DecimalField(
    #     blank=True,
    #     null=True,
    #     max_digits=10,
    #     decimal_places=8,
    #     verbose_name=_('Geographic longitude')
    # )
    # struct_org_hours = StreamField(
    #     [
    #         ('hours', OpenHoursBlock()),
    #     ],
    #     blank=True,
    #     verbose_name=_('Hours of operation')
    # )
    # struct_org_actions = StreamField(
    #     [
    #         ('actions', StructuredDataActionBlock())
    #     ],
    #     blank=True,
    #     verbose_name=_('Actions')
    # )
    # struct_org_extra_json = models.TextField(
    #     blank=True,
    #     verbose_name=_('Additional Organization markup'),
    #     help_text=_('Additional JSON-LD inserted into the Organization dictionary. Must be properties of https://schema.org/Organization or the selected organization type.'),  # noqa
    # )

    ###############
    # Search
    ###############

    search_fields = CoralPage.search_fields + [
        index.SearchField('seo_title', partial_match=True, boost=3),        
    ]

    ###############
    # Panels
    ###############

    # content_panels = super.content_panels + [
    #     ImageChooserPanel('cover_image'),
    # ]

    # body_content_panels = []

    # bottom_content_panels = []

    # category_panels = [
    #     FieldPanel('category_terms', widget=CategorySelectWidget()),
    #     FieldPanel('tags'),
    # ]

    # layout_panels = [
    #     MultiFieldPanel(
    #         [
    #             FieldPanel('custom_template')
    #         ],
    #         heading=_('Visual Design')
    #     ),
    #     MultiFieldPanel(
    #         [
    #             FieldPanel('index_show_subpages'),
    #             FieldPanel('index_num_per_page'),
    #             FieldPanel('index_order_by'),
    #             FieldPanel('index_categories', widget=forms.CheckboxSelectMultiple()),
    #         ],
    #         heading=_('Show Child Pages')
    #     )
    # ]

    promote_panels = [
        MultiFieldPanel(
            [
                FieldPanel('slug'),
                FieldPanel('seo_title'),
                FieldPanel('search_description'),
                ImageChooserPanel('og_image'),
            ],
            _('Page Meta Data')
        ),
        # MultiFieldPanel(
        #     [
        #         HelpPanel(
        #             heading=_('About Organization Structured Data'),
        #             content=_("""The fields below help define brand, contact, and storefront
        #             information to search engines. This information should be filled out on
        #             the site’s root page (Home Page). If your organization has multiple locations,
        #             then also fill this info out on each location page using that particular
        #             location’s info."""),
        #         ),
        #         FieldPanel('struct_org_type'),
        #         FieldPanel('struct_org_name'),
        #         ImageChooserPanel('struct_org_logo'),
        #         ImageChooserPanel('struct_org_image'),
        #         FieldPanel('struct_org_phone'),
        #         FieldPanel('struct_org_address_street'),
        #         FieldPanel('struct_org_address_locality'),
        #         FieldPanel('struct_org_address_region'),
        #         FieldPanel('struct_org_address_postal'),
        #         FieldPanel('struct_org_address_country'),
        #         FieldPanel('struct_org_geo_lat'),
        #         FieldPanel('struct_org_geo_lng'),
        #         StreamFieldPanel('struct_org_hours'),
        #         StreamFieldPanel('struct_org_actions'),
        #         FieldPanel('struct_org_extra_json'),
        #     ],
        #     _('Structured Data - Organization')
        # ),
    ]

    # settings_panels = Page.settings_panels + [
    #     StreamFieldPanel('content_walls'),
    # ]

    # integration_panels = []

    @cached_classmethod
    def get_edit_handler(cls):
        """
        Override to "lazy load" the panels overriden by subclasses.
        """
        panels = [
            ObjectList(
                cls.content_panels + cls.body_content_panels + cls.bottom_content_panels,
                heading=_('Content')
            ),
            ObjectList(cls.category_panels, heading=_('Category')),
            ObjectList(cls.layout_panels, heading=_('Layout')),
            ObjectList(cls.promote_panels, heading=_('SEO'), classname="seo"),
            ObjectList(cls.settings_panels, heading=_('Settings'), classname="settings"),
        ]

        if cls.integration_panels:
            panels.append(ObjectList(
                cls.integration_panels,
                heading='Integrations',
                classname='integrations'
            ))

        return TabbedInterface(panels).bind_to(model=cls)

    # def get_struct_org_name(self):
    #     """
    #     Gets org name for sturctured data using a fallback.
    #     """
    #     if self.struct_org_name:
    #         return self.struct_org_name
    #     return self.get_site().site_name

    # def get_struct_org_logo(self):
    #     """
    #     Gets logo for structured data using a fallback.
    #     """
    #     if self.struct_org_logo:
    #         return self.struct_org_logo
    #     else:
    #         layout_settings = LayoutSettings.for_site(self.get_site())
    #         if layout_settings.logo:
    #             return layout_settings.logo
    #     return None


class CoralWebPage(CoralSEOPage):
    """
    Provides a body and body-related functionality.
    This is abstract so that subclasses can override the body StreamField.
    """
    class Meta:
        verbose_name = _('Coral Web Page')
        abstract = True

    template = 'pages/web_page.html'

    # Child pages should override based on what blocks they want in the body.
    # Default is CONTENT_STREAMBLOCKS which is the fullest editor experience.
    body = StreamField(CONTENT_STREAMBLOCKS, null=True, blank=True)

    # Search fields
    search_fields = (
        CoralPage.search_fields +
        [index.SearchField('body')]
    )

    # Panels
    body_content_panels = [
        StreamFieldPanel('body'),
    ]

    @property
    def body_preview(self):
        """
        A shortened version of the body without HTML tags.
        """
        # add spaces between tags for legibility
        body = str(self.body).replace('>', '> ')
        # strip tags
        body = strip_tags(body)
        # truncate and add ellipses
        preview = body[:200] + "..." if len(body) > 200 else body
        return mark_safe(preview)

    @property
    def page_ptr(self):
        """
        Overwrite of `page_ptr` to make it compatible with wagtailimportexport.
        """
        return self.base_page_ptr

    @page_ptr.setter
    def page_ptr(self, value):
        self.base_page_ptr = value


