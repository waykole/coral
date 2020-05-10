from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.core.models import Page

from wagtail.search import index
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
)

from blocks.models import (
    CONTENT_STREAMBLOCKS,
)

from pages.core_pages import CoralPageMixin, CoralPageMeta


# class HomePage(Page):
#     pass

class HomePage(CoralPageMixin, Page, metaclass=CoralPageMeta):   
    """
    Home Page
    """
    class Meta:
        verbose_name = _('Coral Home Page')

    # parent_page_types = []
    template = 'pages/home_page.html'

    body = StreamField(CONTENT_STREAMBLOCKS, null=True, blank=True)

    content_panels = [
        StreamFieldPanel('body'),
    ]


