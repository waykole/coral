"""
Custom wagtail settings used by Coral CMS.
Settings are user-configurable on a per-site basis (multisite).
Global project or developer settings should be defined in coral.settings.py .
"""

import json
from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import HelpPanel, FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

from common import schema

from blocks.models import (
    # CONTENT_STREAMBLOCKS,
    # LAYOUT_STREAMBLOCKS,
    # # STREAMFORM_BLOCKS,
    # ContentWallBlock,
    OpenHoursBlock,
    StructuredDataActionBlock,
)

# from coral.settings import cr_settings


@register_setting(icon='fa-facebook-official')
class SocialMediaSettings(BaseSetting):
    """
    Social media accounts.
    """
    class Meta:
        verbose_name = _('Social Media')

    facebook = models.URLField(
        blank=True,
        verbose_name=_('Facebook'),
        help_text=_('Your Facebook page URL'),
    )
    twitter = models.URLField(
        blank=True,
        verbose_name=_('Twitter'),
        help_text=_('Your Twitter page URL'),
    )
    instagram = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_('Instagram'),
        help_text=_('Your Instagram username, without the @'),
    )
    youtube = models.URLField(
        blank=True,
        verbose_name=_('YouTube'),
        help_text=_('Your YouTube channel or user account URL'),
    )
    linkedin = models.URLField(
        blank=True,
        verbose_name=_('LinkedIn'),
        help_text=_('Your LinkedIn page URL'),
    )
    googleplus = models.URLField(
        blank=True,
        verbose_name=_('Google'),
        help_text=_('Your Google+ page or Google business listing URL'),
    )

    @property
    def twitter_handle(self):
        """
        Gets the handle of the twitter account from a URL.
        """
        return self.twitter.strip().strip('/').split('/')[-1]

    @property
    def social_json(self):
        """
        Returns non-blank social accounts as a JSON list.
        """
        socialist = [
            self.facebook,
            self.twitter,
            self.instagram,
            self.youtube,
            self.linkedin,
            self.googleplus,
        ]
        socialist = list(filter(None, socialist))
        return json.dumps(socialist)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('facebook'),
                FieldPanel('twitter'),
                FieldPanel('instagram'),
                FieldPanel('youtube'),
                FieldPanel('linkedin'),
                FieldPanel('googleplus'),
            ],
            _('Social Media Accounts'),
        )
    ]


@register_setting(icon='fa-desktop')
class LayoutSettings(BaseSetting):
    """
    Branding, navbar, and theme settings.
    """
    class Meta:
        verbose_name = _('Layout')

    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Logo'),
        help_text=_('Brand logo used in the navbar and throughout the site')
    )
    favicon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='favicon',
        verbose_name=_('Favicon'),
    )
    navbar_color_scheme = models.CharField(
        blank=True,
        max_length=50,
        choices=(
            ('navbar-light', 'Light - for use with a light-colored navbar'),
            ('navbar-dark', 'Dark - for use with a dark-colored navbar'),
        ),
        default='navbar-light',
        verbose_name=_('Navbar color scheme'),
        help_text=_('Optimizes text and other navbar elements for use with light or dark backgrounds.'),  # noqa
    )
    navbar_class = models.CharField(
        blank=True,
        max_length=255,
        default='bg-light',
        verbose_name=_('Navbar CSS class'),
        help_text=_('Custom classes applied to navbar e.g. "bg-light", "bg-dark", "bg-primary".'),
    )
    navbar_fixed = models.BooleanField(
        default=False,
        verbose_name=_('Fixed navbar'),
        help_text=_('Fixed navbar will remain at the top of the page when scrolling.'),
    )
    navbar_wrapper_fluid = models.BooleanField(
        default=True,
        verbose_name=_('Full width navbar'),
        help_text=_('The navbar will fill edge to edge.'),
    )
    navbar_content_fluid = models.BooleanField(
        default=False,
        verbose_name=_('Full width navbar contents'),
        help_text=_('Content within the navbar will fill edge to edge.'),
    )
    navbar_collapse_mode = models.CharField(
        blank=True,
        max_length=50,
        choices=(
            ('', 'Never show menu - Always collapse menu behind a button'),
            ('navbar-expand-sm', 'sm - Show on small screens (phone size) and larger'),
            ('navbar-expand-md', 'md - Show on medium screens (tablet size) and larger'),
            ('navbar-expand-lg', 'lg - Show on large screens (laptop size) and larger'),
            ('navbar-expand-xl', 'xl - Show on extra large screens (desktop, wide monitor)'),
        ),
        default='navbar-expand-lg',
        verbose_name=_('Collapse navbar menu'),
        help_text=_('Control on what screen sizes to show and collapse the navbar menu links.'),
    )
    navbar_format = models.CharField(
        blank=True,
        max_length=50,
        choices=(
            ('', 'Default Bootstrap Navbar'),
            ('coral-navbar-center', 'Centered logo at top'),
        ),
        default='',
        verbose_name=_('Navbar format'),
    )
    navbar_search = models.BooleanField(
        default=True,
        verbose_name=_('Search box'),
        help_text=_('Show search box in navbar')
    )
    frontend_theme = models.CharField(
        blank=True,
        max_length=50,
        choices=(
            ('', 'Default - Classic Bootstrap'),
            ('cerulean', 'Cerulean - A calm blue sky'),
            ('cosmo', 'Cosmo - An ode to Metro'),
            ('cyborg', 'Cyborg - Jet black and electric blue'),
            ('darkly', 'Darkly - Flatly in night mode'),
            ('flatly', 'Flatly - Flat and modern'),
            ('journal', 'Journal - Crisp like a new sheet of paper'),
            ('litera', 'Litera - The medium is the message'),
            ('lumen', 'Lumen - Light and shadow'),
            ('lux', 'Lux - A touch of class'),
            ('materia', 'Materia - Material is the metaphor'),
            ('minty', 'Minty - A fresh feel'),
            ('pulse', 'Pulse - A trace of purple'),
            ('sandstone', 'Sandstone - A touch of warmth'),
            ('simplex', 'Simplex - Mini and minimalist'),
            ('sketchy', 'Sketchy - A hand-drawn look for mockups and mirth'),
            ('slate', 'Slate - Shades of gunmetal gray'),
            ('solar', 'Solar - A dark spin on Solarized'),
            ('spacelab', 'Spacelab - Silvery and sleek'),
            ('superhero', 'Superhero - The brave and the blue'),
            ('united', 'United - Ubuntu orange and unique font'),
            ('yeti', 'Yeti - A friendly foundation'),
        ),
        default='',
        verbose_name=_('Theme variant'),
        help_text="Change the color palette of your site with Bulma theme.",
    )

    panels = [
        MultiFieldPanel(
            [
                ImageChooserPanel('logo'),
                ImageChooserPanel('favicon'),
            ],
            heading=_('Branding')
        ),
        MultiFieldPanel(
            [
                FieldPanel('navbar_color_scheme'),
                FieldPanel('navbar_class'),
                FieldPanel('navbar_fixed'),
                FieldPanel('navbar_wrapper_fluid'),
                FieldPanel('navbar_content_fluid'),
                FieldPanel('navbar_collapse_mode'),
                FieldPanel('navbar_format'),
                FieldPanel('navbar_search'),
            ],
            heading=_('Site Navbar Layout')
        ),
        MultiFieldPanel(
            [
                FieldPanel('frontend_theme'),
            ],
            heading=_('Theming')
        ),
    ]


@register_setting(icon='fa-google')
class AnalyticsSettings(BaseSetting):
    """
    Tracking and Google Analytics.
    """
    class Meta:
        verbose_name = _('Tracking')

    ga_tracking_id = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('GA Tracking ID'),
        help_text=_('Your Google Analytics tracking ID (begins with "UA-")'),
    )
    ga_track_button_clicks = models.BooleanField(
        default=False,
        verbose_name=_('Track button clicks'),
        help_text=_('Track all button clicks using Google Analytics event tracking. Event tracking details can be specified in each button’s advanced settings options.'),  # noqa
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('ga_tracking_id'),
                FieldPanel('ga_track_button_clicks'),
            ],
            heading=_('Google Analytics')
        )
    ]


@register_setting(icon='fa-universal-access')
class ADASettings(BaseSetting):
    """
    Accessibility related options.
    """
    class Meta:
        verbose_name = 'Accessibility'

    skip_navigation = models.BooleanField(
        default=False,
        verbose_name=_('Show skip navigation link'),
        help_text=_('Shows a "Skip Navigation" link above the navbar that takes you directly to the main content.'),  # noqa
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('skip_navigation'),
            ],
            heading=_('Accessibility')
        )
    ]


@register_setting(icon='cog')
class GeneralSettings(BaseSetting):
    """
    Various site-wide settings. A good place to put
    one-off settings that don't belong anywhere else.
    """

    from_email_address = models.CharField(

        blank=True,
        max_length=255,
        verbose_name=_('From email address'),
        help_text=_('The default email address this site appears to send from. For example: "sender@example.com" or "Sender Name <sender@example.com>" (without quotes)'),  # noqa
    )
    search_num_results = models.PositiveIntegerField(
        default=10,
        verbose_name=_('Number of results per page'),
    )
    external_new_tab = models.BooleanField(
        default=False,
        verbose_name=_('Open all external links in new tab')
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('from_email_address'),
            ],
            _('Email')
        ),
        MultiFieldPanel(
            [
                FieldPanel('search_num_results'),
            ],
            _('Search Settings')
        ),
        MultiFieldPanel(
            [
                FieldPanel('external_new_tab'),
            ],
            _('Links')
        ),
    ]

    class Meta:
        verbose_name = _('General')


@register_setting(icon='fa-line-chart')
class SeoSettings(BaseSetting):
    """
    Additional search engine optimization and meta tags
    that can be turned on or off.
    """
    class Meta:
        verbose_name = _('SEO')

    og_meta = models.BooleanField(
        default=True,
        verbose_name=_('Use OpenGraph Markup'),
        help_text=_('Show an optimized preview when linking to this site on Facebook, Linkedin, Twitter, and others. See http://ogp.me/.'),  # noqa
    )
    twitter_meta = models.BooleanField(
        default=True,
        verbose_name=_('Use Twitter Markup'),
        help_text=_('Shows content as a "card" when linking to this site on Twitter. See https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/abouts-cards.'),  # noqa
    )
    struct_meta = models.BooleanField(
        default=True,
        verbose_name=_('Use Structured Data'),
        help_text=_('Optimizes information about your organization for search engines. See https://schema.org/.'),  # noqa
    )
    amp_pages = models.BooleanField(
        default=True,
        verbose_name=_('Use AMP Pages'),
        help_text=_('Generates an alternate AMP version of Article pages that are preferred by search engines. See https://www.ampproject.org/'),  # noqa
    )

    ###############
    # SEO fields
    ###############

    struct_org_type = models.CharField(
        default='',
        blank=True,
        max_length=255,
        choices=schema.SCHEMA_ORG_CHOICES,
        verbose_name=_('Organization type'),
        help_text=_('If blank, no structured data will be used on this page.')
    )
    struct_org_name = models.CharField(
        default='',
        blank=True,
        max_length=255,
        verbose_name=_('Organization name'),
        help_text=_('Leave blank to use the site name in Settings > Sites')
    )
    struct_org_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Organization logo'),
        help_text=_('Leave blank to use the logo in Settings > Layout > Logo')
    )
    struct_org_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Photo of Organization'),
        help_text=_('A photo of the facility. This photo will be cropped to 1:1, 4:3, and 16:9 aspect ratios automatically.'),  # noqa
    )
    struct_org_phone = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('Telephone number'),
        help_text=_('Include country code for best results. For example: +1-216-555-8000')
    )
    struct_org_address_street = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('Street address'),
        help_text=_('House number and street. For example, 55 Public Square Suite 1710')
    )
    struct_org_address_locality = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('City'),
        help_text=_('City or locality. For example, Cleveland')
    )
    struct_org_address_region = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('State'),
        help_text=_('State, province, county, or region. For example, OH')
    )
    struct_org_address_postal = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('Postal code'),
        help_text=_('Zip or postal code. For example, 44113')
    )
    struct_org_address_country = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('Country'),
        help_text=_('For example, USA. Two-letter ISO 3166-1 alpha-2 country code is also acceptible https://en.wikipedia.org/wiki/ISO_3166-1'),  # noqa
    )
    struct_org_geo_lat = models.DecimalField(
        blank=True,
        null=True,
        max_digits=10,
        decimal_places=8,
        verbose_name=_('Geographic latitude')
    )
    struct_org_geo_lng = models.DecimalField(
        blank=True,
        null=True,
        max_digits=10,
        decimal_places=8,
        verbose_name=_('Geographic longitude')
    )
    struct_org_hours = StreamField(
        [
            ('hours', OpenHoursBlock()),
        ],
        blank=True,
        verbose_name=_('Hours of operation')
    )
    struct_org_actions = StreamField(
        [
            ('actions', StructuredDataActionBlock())
        ],
        blank=True,
        verbose_name=_('Actions')
    )
    struct_org_extra_json = models.TextField(
        blank=True,
        verbose_name=_('Additional Organization markup'),
        help_text=_('Additional JSON-LD inserted into the Organization dictionary. Must be properties of https://schema.org/Organization or the selected organization type.'),  # noqa
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('og_meta'),
                FieldPanel('twitter_meta'),
                FieldPanel('struct_meta'),
                FieldPanel('amp_pages'),
                HelpPanel(content=_('If these settings are enabled, the corresponding values in each page’s SEO tab are used.')),  # noqa
            ],
            heading=_('Search Engine Optimization')
        ),
        MultiFieldPanel(
            [
                HelpPanel(
                    heading=_('About Organization Structured Data'),
                    content=_("""The fields below help define brand, contact, and storefront
                    information to search engines. This information should be filled out on
                    the site’s root page (Home Page). If your organization has multiple locations,
                    then also fill this info out on each location page using that particular
                    location’s info."""),
                ),
                FieldPanel('struct_org_type'),
                FieldPanel('struct_org_name'),
                ImageChooserPanel('struct_org_logo'),
                ImageChooserPanel('struct_org_image'),
                FieldPanel('struct_org_phone'),
                FieldPanel('struct_org_address_street'),
                FieldPanel('struct_org_address_locality'),
                FieldPanel('struct_org_address_region'),
                FieldPanel('struct_org_address_postal'),
                FieldPanel('struct_org_address_country'),
                FieldPanel('struct_org_geo_lat'),
                FieldPanel('struct_org_geo_lng'),
                StreamFieldPanel('struct_org_hours'),
                StreamFieldPanel('struct_org_actions'),
                FieldPanel('struct_org_extra_json'),
            ],
            _('Structured Data - Organization')
        ),
    ]


@register_setting(icon='fa-puzzle-piece')
class GoogleApiSettings(BaseSetting):
    """
    Settings for Google API services.
    """
    class Meta:
        verbose_name = _('Google API')

    google_maps_api_key = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('Google Maps API Key'),
        help_text=_('The API Key used for Google Maps.')
    )


@register_setting(icon='fa-puzzle-piece')
class MailchimpApiSettings(BaseSetting):
    """
    Settings for Mailchimp API services.
    """
    class Meta:
        verbose_name = _('Mailchimp API')

    mailchimp_api_key = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('Mailchimp API Key'),
        help_text=_('The API Key used for Mailchimp.')
    )
