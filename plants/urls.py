from django.urls import path
from . import views

app_name = 'plants'

urlpatterns = [
    path('', views.home, name='home'),
    path('plants/', views.PlantListView.as_view(), name='plant_list'),
    path('plants/<int:pk>/', views.PlantDetailView.as_view(), name='plant_detail'),
    path('plants/<int:plant_id>/add/', views.add_user_plant, name='add_user_plant'),
    path('plants/<int:plant_id>/comment/', views.add_comment, name='add_comment'),
] 