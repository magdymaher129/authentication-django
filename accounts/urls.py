from django.urls import path
from .views import signup,login,loginBackend,logout
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('signup/', signup,name='signup'),
    path('login/',login,name='login'),
    path('loginBackend/',loginBackend,name='loginBackend'),
    path('logout',logout,name='logout')
]
