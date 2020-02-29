from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('<int:pk>/profile/', views.ProfileDetailView.as_view(), name = 'profile_detail'),
    path('profile', views.ProfileView.as_view(), name = 'profile'),
    path('<int:pk>/profile/edit', views.ProfileUpdateView.as_view(), name = 'profile_update'),
]