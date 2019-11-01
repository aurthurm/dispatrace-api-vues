from django.contrib import admin
from django.urls import path, re_path, include
from .views import IndexView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

# Serve Vue Application
IndexView = never_cache(TemplateView.as_view(template_name='index.html'))

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView, name="index"),
    path('api/', include('api.urls', namespace="dispatrace-api")),
]

if settings.DEBUG:
    import os
    from django.views.generic.base import RedirectView
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)