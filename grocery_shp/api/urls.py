from django.urls import path
from .import views

urlpatterns= [
        path('', views.ApiOverview, name='home'),
        path('create/', views.add_items, name='add-items'),
        path('all/',  views.view_items, name= 'view-item'),
        path('update/<int:pk>/', views.update_items, name='update-item'),
        path('item/<int:pk>/delete/', views.delete_items, name='dekete-items'),
]