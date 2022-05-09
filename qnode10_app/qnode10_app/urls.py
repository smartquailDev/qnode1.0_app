
#from django.contrib import admin
from django.urls import path,re_path,include
from django.conf import settings
from baton.autodiscover import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
     
    re_path(r'^smartbusinessmedia/', include(wagtailadmin_urls),name='wagtail'),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'', include(wagtail_urls)),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
