"""
Bases, mixins, and utilites for blocks.
"""

from django import forms
from django.template.loader import render_to_string
from django.utils.encoding import force_str
from django.utils.functional import cached_property
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from wagtail.core import blocks
from wagtail.core.models import Collection
from wagtail.core.utils import resolve_model_string
from wagtail.documents.blocks import DocumentChooserBlock

# from coral.settings import cr_settings


class MultiSelectBlock(blocks.FieldBlock):
    """
    Renders as MultipleChoiceField, used for adding checkboxes,
    radios, or multiselect inputs in the streamfield.
    """

    def __init__(self, required=True, help_text=None, choices=None, widget=None, **kwargs):
        self.field = forms.MultipleChoiceField(
            required=required,
            help_text=help_text,
            choices=choices,
            widget=widget,
        )
        super().__init__(**kwargs)

    def get_searchable_content(self, value):
        return [force_str(value)]


class CategoryTermChooserBlock(blocks.FieldBlock):
    """
    Enables choosing a CategoryTerm in the streamfield.
    Lazy loads the target_model from the string to avoid recursive imports.
    """
    widget = forms.Select

    def __init__(self, required=False, label=None, help_text=None, *args, **kwargs):
        self._required = required
        self._help_text = help_text
        self._label = label
        super().__init__(*args, **kwargs)

    @cached_property
    def target_model(self):
        return resolve_model_string('blocks.CategoryTerm')

    @cached_property
    def field(self):
        return forms.ModelChoiceField(
            queryset=self.target_model.objects.all().order_by('category__name', 'name'),
            widget=self.widget,
            required=self._required,
            label=self._label,
            help_text=self._help_text,
        )

    def to_python(self, value):
        """
        Convert the serialized value back into a python object.
        """
        if isinstance(value, int):
            return self.target_model.objects.get(pk=value)
        return value

    def get_prep_value(self, value):
        """
        Serialize the model in a form suitable for wagtail's JSON-ish streamfield
        """
        if isinstance(value, self.target_model):
            return value.pk
        return value

class ButtonMixin(blocks.StructBlock):
    """
    Standard style and size options for buttons.
    """
    button_title = blocks.CharBlock(
        max_length=255,
        required=True,
        label=_('Button Title'),
    )
    button_style = blocks.ChoiceBlock(
        choices=(
            ('btn-primary', 'Primary'),
            ('btn-secondary', 'Secondary'),
            ('btn-success', 'Success'),
            ('btn-danger', 'Danger'),
            ('btn-warning', 'Warning'),
            ('btn-info', 'Info'),
            ('btn-link', 'Link'),
            ('btn-light', 'Light'),
            ('btn-dark', 'Dark'),
            ('btn-outline-primary', 'Outline Primary'),
            ('btn-outline-secondary', 'Outline Secondary'),
            ('btn-success', 'Outline Success'),
            ('btn-outline-danger', 'Outline Danger'),
            ('btn-outline-warning', 'Outline Warning'),
            ('btn-outline-info', 'Outline Info'),
            ('btn-outline-light', 'Outline Light'),
            ('btn-outline-dark', 'Outline Dark'),
        ),
        default='btn-primary',
        required=False,
        label=_('Button Style'),
    )
    button_size = blocks.ChoiceBlock(
        choices=(
            ('btn-sm', 'Small'),
            ('', 'Default'),
            ('btn-lg', 'Large'),
        ),
        default='',
        required=False,
        label=_('Button Size'),
    )


class CollectionChooserBlock(blocks.FieldBlock):
    """
    Enables choosing a wagtail Collection in the streamfield.
    """
    target_model = Collection
    widget = forms.Select

    def __init__(self, required=False, label=None, help_text=None, *args, **kwargs):
        self._required = required
        self._help_text = help_text
        self._label = label
        super().__init__(*args, **kwargs)

    @cached_property
    def field(self):
        return forms.ModelChoiceField(
            queryset=self.target_model.objects.all().order_by('name'),
            widget=self.widget,
            required=self._required,
            label=self._label,
            help_text=self._help_text,
        )

    def to_python(self, value):
        """
        Convert the serialized value back into a python object.
        """
        if isinstance(value, int):
            return self.target_model.objects.get(pk=value)
        return value

    def get_prep_value(self, value):
        """
        Serialize the model in a form suitable for wagtail's JSON-ish streamfield
        """
        if isinstance(value, self.target_model):
            return value.pk
        return value


class CoralAdvSettings(blocks.StructBlock):
    """
    Common fields each block should have,
    which are hidden under the block's "Advanced Settings" dropdown.
    """
    # placeholder, real value get set in __init__()
    custom_template = blocks.Block()

    custom_css_class = blocks.CharBlock(
        default='',
        required=False,
        max_length=255,
        label=_('Custom CSS Class'),
    )
    custom_id = blocks.CharBlock(
        default='',
        required=False,
        max_length=255,
        label=_('Custom ID'),
    )

    class Meta:
        form_template = 'wagtailadmin/block_forms/base_block_settings_struct.html'
        label = _('Advanced Settings')

    def __init__(self, local_blocks=None, template_choices=None, **kwargs):
        if not local_blocks:
            local_blocks = ()

        local_blocks += (
            (
                'custom_template',
                blocks.ChoiceBlock(
                    choices=template_choices,
                    default=None,
                    required=False,
                    label=_('Template'))
            ),
        )

        super().__init__(local_blocks, **kwargs)


class CoralAdvTrackingSettings(CoralAdvSettings):
    """
    CoralAdvSettings plus additional tracking fields.
    """
    ga_tracking_event_category = blocks.CharBlock(
        default='',
        required=False,
        max_length=255,
        label=_('Tracking Event Category'),
    )
    ga_tracking_event_label = blocks.CharBlock(
        default='',
        required=False,
        max_length=255,
        label=_('Tracking Event Label'),
    )


class CoralAdvColumnSettings(CoralAdvSettings):
    """
    BaseBlockSettings plus additional column fields.
    """
    column_breakpoint = blocks.ChoiceBlock(
        choices=(
            ('', 'Always expanded'),
            ('sm', 'sm - Expand on small screens (phone, 576px) and larger'),
            ('md', 'md - Expand on medium screens (tablet, 768px) and larger'),
            ('lg', 'lg - Expand on large screens (laptop, 992px) and larger'),
            ('xl', 'xl - Expand on extra large screens (wide monitor, 1200px)'),
        ),
        default='md',
        required=False,
        verbose_name=_('Column Breakpoint'),
        help_text=_('Screen size at which the column will expand horizontally or stack vertically.'),  # noqa
    )


class BaseBlock(blocks.StructBlock):
    """
    Common attributes for all blocks used in Coal CMS.
    """
    # subclasses can override this to determine the advanced settings class
    advsettings_class = CoralAdvSettings

    # placeholder, real value get set in __init__() from advsettings_class
    settings = blocks.Block()

    def __init__(self, local_blocks=None, **kwargs):
        """
        Construct and inject settings block, then initialize normally.
        """
        klassname = self.__class__.__name__.lower()
        FRONTEND_TEMPLATES_BLOCKS = {
            'cardblock': (
                ('blocks/card_block.html', 'Card'),
                ('blocks/card_head.html', 'Card with header'),
                ('blocks/card_foot.html', 'Card with footer'),
                ('blocks/card_head_foot.html', 'Card with header and footer'),
                ('blocks/card_blurb.html', 'Blurb - rounded image and no border'),
                ('blocks/card_img.html', 'Cover image - use image as background'),
            ),
            'cardgridblock': (
                ('blocks/cardgrid_group.html', 'Card group - attached cards of equal size'),
                ('blocks/cardgrid_deck.html', 'Card deck - separate cards of equal size'),
                ('blocks/cardgrid_columns.html', 'Card masonry - fluid brick pattern'),
            ),
            'pagelistblock': (
                ('blocks/pagelist_block.html', 'General, simple list'),
                ('blocks/pagelist_list_group.html', 'General, list group navigation panel'),
                ('blocks/pagelist_article_media.html', 'Article, media format'),
                ('blocks/pagelist_article_card_group.html',
                    'Article, card group - attached cards of equal size'),
                ('blocks/pagelist_article_card_deck.html',
                'Article, card deck - separate cards of equal size'),
                ('blocks/pagelist_article_card_columns.html',
                'Article, card masonry - fluid brick pattern'),
            ),
            'pagepreviewblock': (
                ('blocks/pagepreview_card.html', 'Card'),
                ('blocks/pagepreview_form.html', 'Form inputs'),
            ),
            # templates that are available for all block types
            '*': (
                ('', 'Default'),
            ),
        }
        choices = FRONTEND_TEMPLATES_BLOCKS.get('*', ()) + \
            FRONTEND_TEMPLATES_BLOCKS.get(klassname, ())

        if not local_blocks:
            local_blocks = ()

        local_blocks += (('settings', self.advsettings_class(template_choices=choices)),)

        super().__init__(local_blocks, **kwargs)

    def render(self, value, context=None):
        template = value['settings']['custom_template']

        if not template:
            template = self.get_template(context=context)
            if not template:
                return self.render_basic(value, context=context)

        if context is None:
            new_context = self.get_context(value)
        else:
            new_context = self.get_context(value, parent_context=dict(context))

        return mark_safe(render_to_string(template, new_context))


class BaseLayoutBlock(BaseBlock):
    """
    Common attributes for all blocks used in Coral CMS.
    """
    # Subclasses can override this to provide a default list of blocks for the content.
    content_streamblocks = []

    def __init__(self, local_blocks=None, **kwargs):
        if not local_blocks and self.content_streamblocks:
            local_blocks = self.content_streamblocks

        if local_blocks:
            local_blocks = (('content', blocks.StreamBlock(local_blocks, label=_('Content'))),)

        super().__init__(local_blocks, **kwargs)


class LinkStructValue(blocks.StructValue):
    """
    Generates a URL for blocks with multiple link choices.
    """
    @property
    def url(self):
        page = self.get('page_link')
        doc = self.get('doc_link')
        ext = self.get('other_link')
        if page:
            return page.url
        elif doc:
            return doc.url
        else:
            return ext


class BaseLinkBlock(BaseBlock):
    """
    Common attributes for creating a link within the CMS.
    """
    page_link = blocks.PageChooserBlock(
        required=False,
        label=_('Page link'),
    )
    doc_link = DocumentChooserBlock(
        required=False,
        label=_('Document link'),
    )
    other_link = blocks.CharBlock(
        required=False,
        max_length=255,
        label=_('Other link'),
    )

    advsettings_class = CoralAdvTrackingSettings

    class Meta:
        value_class = LinkStructValue
