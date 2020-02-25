from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('add/', views.CreateView.as_view(), name = 'create'),
    path('<int:pk>/delete', views.DeleteView.as_view(), name = 'delete'),
    path('<int:pk>/comment/', views.CommentView.as_view(), name = 'comment'),
    path('<int:pk>/update', views.add_users, name = 'add_users')
]
