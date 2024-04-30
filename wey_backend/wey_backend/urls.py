from django.contrib import admin
from django.urls import path,include



from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path('api/', include('account.urls')),
    path('api/conversion/', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('api/posts/', include('post.urls')),
    path('api/search/', include('search.urls')),
    path('api/notification/',include('notification.urls'))
]


# URL pour servir les fichiers d'attachement
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)