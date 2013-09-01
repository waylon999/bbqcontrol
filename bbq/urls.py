from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from bbq import views

urlpatterns = patterns('',
    (r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^bbq/?$', views.BbqList.as_view(), name='bbq-list'),
    url(r'^bbq/(?P<pk>[0-9]+)/$', views.BbqDetail.as_view(), name='bbq-detail'),
)
if settings.DEBUG:
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                     {'document_root': settings.STATIC_ROOT}),

urlpatterns = format_suffix_patterns(urlpatterns)
