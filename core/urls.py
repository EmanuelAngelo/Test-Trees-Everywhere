from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trees/', include('trees.urls', namespace='trees')),
]
