from django.conf.urls import patterns, include, url
#from article.views import HelloTemplate
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^articles',include('article.urls')),
    url(r'^admin',include(admin.site.urls)),
    url(r'^accounts/login','demo.views.login'),
    url(r'^accounts/auth','demo.views.auth_view'),
    url(r'^accounts/logout','demo.views.logout'),
    url(r'^accounts/loggedin','demo.views.loggedin'),
    url(r'^accounts/invalid','demo.views.invalid_login'),
    url(r'^accounts/register','demo.views.register_user'),
    url(r'^accounts/register_success','demo.views.register_success'),
    #url(r'^hello$', 'article.views.hello', name='hello'),
   # url(r'^hello_template_simple$','article.views.hello_template_simple'),
    #url(r'^hello_class_view$', HelloTemplate.as_view()),
    # url(r'^demo/', include('demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
