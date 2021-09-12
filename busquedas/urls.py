from django.urls import path
from . import views

urlpatterns = [
    path('', views.busquedas, name="Busquedas"),
    path('smart_search', views.smart_search, name ="smart_search"),
    path('show_sm/<residuo_id>', views.show_sm, name="show_sm" ),
    path('recycle_search', views.recycle_search, name ="recycle_search"),
    path('show_rm/<residuo_id>', views.show_rm, name="show_rm" ),
    path('clean_container', views.clean_container, name="clean_container" ),
]
