# No arquivo urls.py do seu aplicativo 'trees'
from django.urls import path
from .views import login_view, dashboard

app_name = 'trees'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),  # Defina a URL para a página de dashboard
]
