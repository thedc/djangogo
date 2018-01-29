from django.conf.urls import include, url
from django.contrib import admin
from views import l1

urlpatterns = [
    # Examples:
    # url(r'^$', 'test1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^l1/$',l1)
]
