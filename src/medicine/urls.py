from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'medicine.views.index', name='index'),
    # url(r'^medicine/', include('medicine.foo.urls')),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login'),

    url(r'^profiles/edit/', 'medicine.views.edit_profile',
        name='edit_profile'),
    url(r'^admin/', include(admin.site.urls)),

    (r'^admin/jsi18n', 'django.views.i18n.javascript_catalog'),
)
