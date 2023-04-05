from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

urlpatterns = [
    path('home/', home_window, name='home'),
    path('home/add/', CreatePPLView.as_view(), name='add'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

LOGOUT_REDIRECT_URL = 'layout:home'
