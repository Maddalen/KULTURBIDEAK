from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout, password_change, password_change_done
from django.conf import settings
from django.views.generic.base import RedirectView, TemplateView
from django.utils.translation import ugettext_lazy as _
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
   
)
