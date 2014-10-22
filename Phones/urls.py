from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib import auth
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Phones.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index$', 'phoneonline.views.index'),
    url(r'^about$', 'phoneonline.views.about'),
    url(r'^store$', 'phoneonline.views.store'),
    url(r'^blog$', 'phoneonline.views.blog'),
    url(r'^contact$', 'phoneonline.views.contact'),
    url(r'^single$', 'phoneonline.views.single'),
    url(r'^home$', 'phoneonline.views.home'),
    url(r'^signup$', 'phoneonline.views.signup'),
    url(r'^signin$', 'django.contrib.auth.views.login',{'template_name': 'signin.html'}),
    url(r'^$', 'phoneonline.views.index', name='index'),
)
