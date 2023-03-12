from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from blog.views import (HomeScreen,ContactFunc)

urlpatterns = [
    path("",HomeScreen.as_view( template_name='blog/home.html' ) ,name='home'),
    path("admin/", admin.site.urls),
    path("administration/", include('farmer.urls')),
    path("blog/",include('blog.urls')),
    path("account/",include('acc.urls')),
    path("contact/",ContactFunc,name = 'contact'),
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
