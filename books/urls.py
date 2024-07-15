from django.urls import path
from . import views

urlpatterns = [
    path('', views.lib, name='lib'),

    path('shopping', views.list_view, name='list_view'),
    path('<id>', views.detailed_view, name='detailed_view'),
    path('<id>/update', views.update_view, name='update_view'),
    path('<id>/delete', views.delete_view, name='delete_view'),
]