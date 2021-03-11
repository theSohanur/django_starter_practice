from django.urls import path

from . import views

urlpatterns = [
    # /food/
    path('', views.index, name='index'),
    # /food/1
    path("<int:item_id>/", views.detail, name="detail"),
    path('item/', views.item, name='item'),
    # add item
    path('add/', views.create_item, name='create_item'),
    # Edit item
    path('update/<int:item_id>/', views.update_item, name='update_item'),
    # Delete item
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]