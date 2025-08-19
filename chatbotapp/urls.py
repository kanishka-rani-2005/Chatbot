
from django.contrib import admin
from django.urls import path
from . import views
<<<<<<< HEAD

urlpatterns = [
    path("", views.chatbot_view, name="chatbot"),
]
=======
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', RedirectView.as_view(url='/register/', permanent=False)),

    path("login/chatbot/", views.chatbot_view, name="chatbot"),
    path('login/',views.login_view, name="login"),
    path('register/',views.register_view, name="register"),
    path('logout/', views.login_view, name='logout'),
   ]
>>>>>>> b35d541 (Removed secret file from Git tracking)
