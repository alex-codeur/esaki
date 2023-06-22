from django.urls import path

from . import views
from accounts import views as user_view

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register_view, name='register_view'),
    path('profile/', views.profile_view, name="profile_view"),
    path('profile/update/', user_view.profile_update, name="profile_update")
]