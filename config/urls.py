from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('api.urls')),
#     path('schema/', SpectacularSwaggerView.as_view(), name='schema'),
#     re_path(r'^swagger(?P<format>\.json|\.yaml)$', SpectacularSwaggerView.as_view(), name='swagger'),
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
