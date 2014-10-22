from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib import auth
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jeaponline.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index$', 'bbs.views.index'),
    url(r'^home$', 'bbs.views.home'),
    url(r'^signup$', 'bbs.views.signup'),
    url(r'^signin$', 'django.contrib.auth.views.login',{'template_name': 'signin.html'}),
    url(r'^$', 'bbs.views.index', name='index'),
)
