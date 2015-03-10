from django.conf.urls import patterns, include, url
from marketing.views import HomePage
#from django.contrib import admin

urlpatterns = patterns('',
	
	# Marketing pages
	url(r'^$', HomePage.as_view(), name="home"),
    # Examples:
    # url(r'^$', 'crmeasy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
