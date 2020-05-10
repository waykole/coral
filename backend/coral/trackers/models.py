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

from pages.core_pages import CoralPage


class CoralTrackerPage(CoralPage):
    """
    Generic tracker
    """
    class Meta:
        verbose_name = _('Coral Tracker Page')

    # Do not allow this page type to be created in wagtail admin
    is_creatable = False

    # template = 'pages/tracker_page.html'
    # amp_template = 'pages/tracker_page.amp.html'

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
        CoralPage.search_fields +
        [
            index.SearchField('caption', boost=2),
            index.FilterField('author'),
            index.FilterField('author_display'),
            index.FilterField('date_display'),
        ]
    )

    content_panels = CoralPage.content_panels + [
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


# Required authentication
class CoralOvulationPage(CoralTrackerPage):
    """
    Ovulation tracker page
    """
    class Meta:
        verbose_name = _('Coral Ovulation tracker page')

    template = 'pages/ovulation_page.html'


# Required authentication
class CoralPregnancyPage(CoralTrackerPage):
    """
    Pregnancy tracker page
    """
    class Meta:
        verbose_name = _('Coral Pregnancy tracker page')

    template = 'pages/pregnancy_page.html'


# Required authentication
class CoralChildGrowthPage(CoralTrackerPage):
    """
    Child-Growth tracker page
    """
    class Meta:
        verbose_name = _('Coral Child-Growth tracker page')

    template = 'pages/child_growth_page.html'