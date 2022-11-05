from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "LetsGoo Admin Panel"
admin.site.site_title = "LetsGoo Admin Portal"
admin.site.index_title = "Welcome to LetsGoo!"

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^/(?P<stream_path>(.*?))/$',views.dynamic_stream,name="videostream"),  
    #url(r'^stream/$',views.indexscreen),
    path('', include('letsgo.urls')),
    path("live_chat/",include('live_chat.urls')),
    path("live_stream/",include('live_stream.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)