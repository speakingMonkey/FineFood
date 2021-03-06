from django.conf.urls import patterns, include, url
from FineFood import settings
from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static
import App

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FineFood.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'',include('App.urls')),
    url(r'^site_medias/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
    url(r'^uploads/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.UPLOAD_PATH})
)

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)