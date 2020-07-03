
from django.urls import path
from menu.views import DrinkListView, CoffeeCreateView, BubbleteaCreateView, DrinkUpdateView, DrinkDeleteView

app_name = 'menu'

urlpatterns = [
    path('', DrinkListView.as_view(), name = 'list'),
    path('add/', CoffeeCreateView.as_view(), name = 'add_coffee'),
    path('add/', BubbleteaCreateView.as_view(), name = 'add_bubbletea'),
    path('update/<int:pk>/', DrinkUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>/', DrinkDeleteView.as_view(), name = 'delete'),
]

