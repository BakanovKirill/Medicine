from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'medicine.views.index', name='index'),
    # url(r'^medicine/', include('medicine.foo.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    url(r'^profiles/edit/', 'medicine.views.edit_profile',
        name='edit_profile'),

    url(r'^doctors/add/', 'medicine.views.add_doctor',
        name='add_doctor'),

    url(r'^ajax/patients/(?P<doctor_id>\d+)/$', 'medicine.views.ajax_patients_list', {}, name="ajax_patients_list"),

    url(r'^admin/', include(admin.site.urls)),

)
