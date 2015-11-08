from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CodePage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^front-edit/', include('front.urls')),
    url(r'^index_id','CodePage.views.index_id'),
    url(r'^update-content','CodePage.views.update_content'),
    url(r'^','CodePage.views.index'),

)
