from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'/all/', 'article.views.articles'),
    url(r'/get/(?P<article_id>\d+)/', 'article.views.article'),
   # url(r'^hello_template_simple$','article.views.hello_template_simple'),
    #url(r'^hello_class_view$', HelloTemplate.as_view()),
    # url(r'^demo/', include('demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
