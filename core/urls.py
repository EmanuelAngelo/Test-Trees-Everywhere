from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('trees/', include('trees.urls', namespace='trees')),
    path('', RedirectView.as_view(url='/trees/login/', permanent=False)),
]
