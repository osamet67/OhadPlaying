from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from logger.handlers import LogHandler, ConsoleHandler

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

class CsrfExemptResource( Resource ):
    def __init__( self, handler, authentication = None ):
         super( CsrfExemptResource, self ).__init__( handler, authentication )
         self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tools.views.home', name='home'),
    url(r'^account/(?P<account_id>\d+)/(?P<agent_id>[a-zA-Z0-9_.]+)/$', 'logger.views.account'),
    url(r'^console/$', 'logger.views.console'),
    url(r'^console/(?P<expression>.*)', CsrfExemptResource( ConsoleHandler )),
    url(r'^log/(?P<expression>.*)', CsrfExemptResource( LogHandler )),
    #url(r'^log/(?P<expression>.*)', 'logger.handlers.db'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
