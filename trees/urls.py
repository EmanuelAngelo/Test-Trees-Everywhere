from django.urls import path
from . import views

app_name = 'trees'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('planted_tree_list/', views.planted_tree_list, name='planted_tree_list' ),
    path('add_planted_tree/', views.add_planted_tree, name='add_planted_tree'),
    path('<int:id>/<int:year>/<int:month>/<int:day>/<slug:post>',views.planted_tree_detail, name='planted_tree_detail'),
    path('api/planted-trees/', views.PlantedTreeListAPIView.as_view(), name='planted-tree-list')
]
