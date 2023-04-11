from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

urlpatterns = [
    path('home/', Home_window.as_view(), name='home'),
    path('home/seacrh/', Search.as_view(), name= 'search'),
    path('home/add/', CreatePPLView.as_view(), name='add'),
    path('home/for_employees/', for_employees, name = 'for_employees'),
    path('home/for_employers/', for_employers, name = 'for_employers')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

LOGOUT_REDIRECT_URL = 'layout:home'
