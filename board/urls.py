from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:question_pk>/', views.detail, name='detail'),
    path('<int:question_pk>/update/', views.update, name='update'),
    path('<int:question_pk>/delete/', views.delete, name='delete'),
] 