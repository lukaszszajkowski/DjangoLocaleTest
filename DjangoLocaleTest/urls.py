from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf.urls.i18n import i18n_patterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoLocaleTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home', name='home'),
)
