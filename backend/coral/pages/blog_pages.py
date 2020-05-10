from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from wagtail.search import index
from wagtail.core.fields import StreamField

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
)

from blocks.models import (
    CONTENT_STREAMBLOCKS,
    LAYOUT_STREAMBLOCKS,
    # STREAMFORM_BLOCKS,
    ContentWallBlock,
    OpenHoursBlock,
    StructuredDataActionBlock,
)

from .core_pages import CoralWebPage

class CoralBlogPage(CoralWebPage):
    """
    Article, suitable for news or blog content.
    """
    class Meta:
        verbose_name = _('Coral Blog Page')

    template = 'pages/blog_page.html'
    amp_template = 'pages/blog_page.amp.html'

    # Override body to provide simpler content
    body = StreamField(CONTENT_STREAMBLOCKS, null=True, blank=True)

    caption = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_('Caption'),
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        editable=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Author'),
    )
    author_display = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_('Display author as'),
        help_text=_('Override how the author’s name displays on this article.'),
    )
    date_display = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Display publish date'),
    )

    def get_author_name(self):
        """
        Gets author name using a fallback.
        """
        if self.author_display:
            return self.author_display
        if self.author:
            return self.author.get_full_name()
        return ''

    def get_pub_date(self):
        """
        Gets published date.
        """
        if self.date_display:
            return self.date_display
        return ''

    def get_description(self):
        """
        Gets the description using a fallback.
        """
        if self.search_description:
            return self.search_description
        if self.caption:
            return self.caption
        if self.body_preview:
            return self.body_preview
        return ''

    search_fields = (
        CoralWebPage.search_fields +
        [
            index.SearchField('caption', boost=2),
            index.FilterField('author'),
            index.FilterField('author_display'),
            index.FilterField('date_display'),
        ]
    )

    content_panels = CoralWebPage.content_panels + [
        FieldPanel('caption'),
        MultiFieldPanel(
            [
                FieldPanel('author'),
                FieldPanel('author_display'),
                FieldPanel('date_display'),
            ],
            _('Publication Info')
        )
    ]


class CoralBlogIndexPage(CoralWebPage):
    """
    Shows a list of blog sub-pages.
    """
    class Meta:
        verbose_name = _('Coral Blog Index Page')

    template = 'pages/blog_index_page.html'

    index_show_subpages_default = True

    index_order_by_default = '-date_display'
    index_order_by_choices = (('-date_display', 'Display publish date, newest first'),) + \
        CoralWebPage.index_order_by_choices

    show_images = models.BooleanField(
        default=True,
        verbose_name=_('Show images'),
    )
    show_captions = models.BooleanField(
        default=True,
    )
    show_meta = models.BooleanField(
        default=True,
        verbose_name=_('Show author and date info'),
    )
    show_preview_text = models.BooleanField(
        default=True,
        verbose_name=_('Show preview text'),
    )

    layout_panels = CoralWebPage.layout_panels + [
        MultiFieldPanel(
            [
                FieldPanel('show_images'),
                FieldPanel('show_captions'),
                FieldPanel('show_meta'),
                FieldPanel('show_preview_text'),
            ],
            heading=_('Child page display')
        ),
    ]
