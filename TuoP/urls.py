from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'TuoP.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls',namespace='blog')),
    url(r'^sso/', include('sso.urls',namespace='sso')),
    url(r'^tca/', include('tca.urls',namespace='tca')),
]
