from django.urls import path

from . import views

urlpatterns = [
    # /food/
    path('', views.index, name='index'),
    # /food/1
    path("<int:item_id>/", views.detail, name="detail"),
    path('item/', views.item, name='index'),
    # add item
    path('add/', views.create_item, name='create_item'),
    # Edit item
    path('update/<int:item_id>/', views.update_item, name='update_item'),
]