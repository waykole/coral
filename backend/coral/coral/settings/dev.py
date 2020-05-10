from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+(4uwew+q_#$g1to$czb#)#n_7^!gbdhl%wc%t&1%^oe-nn%$q'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
    # "template_profiler_panel",
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
#     'debug_toolbar.panels.profiling.ProfilingPanel',
#     "template_profiler_panel.panels.template.TemplateProfilerPanel",
# ]


try:
    from .local import *
except ImportError:
    pass
