from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'medicine.views.home', name='home'),
    # url(r'^medicine/', include('medicine.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
