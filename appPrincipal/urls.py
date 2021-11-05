from django.urls import path

from appPrincipal import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.home), name="Home"),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)