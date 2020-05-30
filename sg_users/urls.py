from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('profile/', views.profile, name='sg-profile'),
    path('signup/', views.signup, name='sg-signup'),
    path('signin/', views.signin, name='sg-signin'),
    path('signout/', auth_views.LogoutView.as_view(
        template_name='sg_users/signout.html'), name='sg-signout')
]
