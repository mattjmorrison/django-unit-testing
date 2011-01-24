from django.conf import settings
from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    (r'', include('sample_app.urls')),
)
