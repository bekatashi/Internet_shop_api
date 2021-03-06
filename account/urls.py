from django.urls import path, include
from . import views

from rest_auth.views import LoginView

urlpatterns = [

    path('accounts/register/', views.RegistrationView.as_view()),
    path('accounts/', include('rest_auth.urls')),
    path('accounts/logout/', views.LogoutView.as_view()),
    path('accounts/activate/<uuid:activation_code>', views.ActivationView.as_view()),
    path('accounts/create_seller/', views.CreateSuperUserView.as_view()),
    path('accounts/<int:pk>', views.UserDetailView.as_view()),
    path('accounts/', views.UserListView.as_view())
]
