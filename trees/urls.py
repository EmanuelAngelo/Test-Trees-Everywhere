# No arquivo urls.py do seu aplicativo 'trees'
from django.urls import path
from . import views

app_name = 'trees'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.planted_tree_list, name='planted_tree_list' ),
    path('<int:year>/<int:month>/<int:day>/<slug:post>',views.planted_tree_detail, name='planted_tree_detail'),
    path('api/planted-trees/', views.PlantedTreeListAPIView.as_view(), name='planted-tree-list')
]
