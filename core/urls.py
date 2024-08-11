from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('empresarios/', include('empresarios.urls')),
    path('investidores/', include('investidores.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
