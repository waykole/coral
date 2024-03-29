"""
Enhancements to wagtail.contrib.forms.
"""
import csv
import os
import re
from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from wagtail.contrib.forms.views import SubmissionsListView as WagtailSubmissionsListView
from wagtail.contrib.forms.forms import FormBuilder
from wagtail.contrib.forms.models import AbstractFormField

# from coral.settings import cr_settings
from .utils import attempt_protected_media_value_conversion

FORM_FIELD_CHOICES = (
    (_('Text'), (
        ('singleline', _('Single line text')),
        ('multiline', _('Multi-line text')),
        ('email', _('Email')),
        ('number', _('Number - only allows integers')),
        ('url', _('URL')),
    ),),
    (_('Choice'), (
        ('checkboxes', _('Checkboxes')),
        ('dropdown', _('Drop down')),
        ('radio', _('Radio buttons')),
        ('multiselect', _('Multiple select')),
        ('checkbox', _('Single checkbox')),
    ),),
    (_('Date & Time'), (
        ('date', _('Date')),
        ('time', _('Time')),
        ('datetime', _('Date and time')),
    ),),
    (_('File Upload'), (
        ('file', _('Secure File - login required to access uploaded files')),
    ),),
    (_('Other'), (
        ('hidden', _('Hidden field')),
    ),),
)

PROTECTED_MEDIA_UPLOAD_WHITELIST = []
PROTECTED_MEDIA_UPLOAD_BLACKLIST = ['.sh', '.exe', '.bat', '.ps1', '.app', '.jar', '.py', '.php', '.pl', '.rb'],  # noqa


# Files

class SecureFileField(forms.FileField):
    custom_error_messages = {
        'blacklist_file': _('Submitted file is not allowed.'),
        'whitelist_file': _('Submitted file is not allowed.')
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.error_messages.update(self.custom_error_messages)

    def validate(self, value):
        super(SecureFileField, self).validate(value)
        if value:
            self._check_whitelist(value)
            self._check_blacklist(value)

    def _check_whitelist(self, value):
        if PROTECTED_MEDIA_UPLOAD_WHITELIST:
            if os.path.splitext(value.name)[1].lower() not in PROTECTED_MEDIA_UPLOAD_WHITELIST:  # noqa
                raise ValidationError(self.error_messages['whitelist_file'])

    def _check_blacklist(self, value):
        if PROTECTED_MEDIA_UPLOAD_BLACKLIST:
            if os.path.splitext(value.name)[1].lower() in PROTECTED_MEDIA_UPLOAD_BLACKLIST:  # noqa
                raise ValidationError(self.error_messages['blacklist_file'])


# Date

class CoralDateInput(forms.DateInput):
    template_name = 'formfields/date.html'


class CoralDateField(forms.DateField):
    widget = CoralDateInput()


# Datetime

class CoralDateTimeInput(forms.DateTimeInput):
    template_name = 'formfields/datetime.html'


class CoralDateTimeField(forms.DateTimeField):
    widget = CoralDateTimeInput()
    input_formats = ['%Y-%m-%dT%H:%M', '%m/%d/%Y %I:%M %p', '%m/%d/%Y %I:%M%p', '%m/%d/%Y %H:%M']


# Time

class CoralTimeInput(forms.TimeInput):
    template_name = 'formfields/time.html'


class CoralTimeField(forms.TimeField):
    widget = CoralTimeInput()
    input_formats = ['%H:%M', '%I:%M %p', '%I:%M%p']


class CoralFormBuilder(FormBuilder):
    """
    Enhance wagtail FormBuilder with additional custom fields.
    """

    def create_file_field(self, field, options):
        return SecureFileField(**options)

    def create_date_field(self, field, options):
        return CoralDateField(**options)

    def create_datetime_field(self, field, options):
        return CoralDateTimeField(**options)

    def create_time_field(self, field, options):
        return CoralTimeField(**options)


class CoralSubmissionsListView(WagtailSubmissionsListView):
    def get_csv_response(self, context):
        filename = self.get_csv_filename()
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = 'attachment;filename={}'.format(filename)

        writer = csv.writer(response)
        writer.writerow(context['data_headings'])
        for data_row in context['data_rows']:
            modified_data_row = []
            for cell in data_row:
                modified_cell = attempt_protected_media_value_conversion(self.request, cell)
                modified_data_row.append(modified_cell)

            writer.writerow(modified_data_row)
        return response


class CoralFormField(AbstractFormField):
    class Meta:
        abstract = True

    field_type = models.CharField(
        verbose_name=_('field type'),
        max_length=16,
        choices=FORM_FIELD_CHOICES,
        blank=False,
        default='Single line text'
    )


class SearchForm(forms.Form):
    s = forms.CharField(
        max_length=255,
        required=False,
        label=_('Search'),
    )
    t = forms.CharField(
        widget=forms.HiddenInput,
        max_length=255,
        required=False,
        label=_('Page type'),
    )


def get_page_model_choices():
    """
    Returns a list of tuples of all creatable Coral pages
    in the format of ("Custom Coral Page", "CustomCoralPage")
    """
    from pages.models import get_page_models
    return (
        (
            page.__name__,
            re.sub(
                r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))',
                r' \1',
                page.__name__
            )
        ) for page in get_page_models() if page.is_creatable
    )
