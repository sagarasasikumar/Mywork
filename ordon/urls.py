from django.conf.urls import include, url
from django.contrib import admin
from website import views

urlpatterns =[
    # Examples:
    # url(r'^$', 'ordon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
