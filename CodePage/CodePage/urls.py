from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CodePage.views.home', name='home'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^','CodePage.views.index'),

)
