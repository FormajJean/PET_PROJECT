from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('home/', home_window, name='home'),
    path('home/add', CreatePPLView.as_view(), name='add')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
