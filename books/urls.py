from django.urls import path
from . import views

from .views import list,detail,create,delete,update

urlpatterns = [
    # path("shop",list.as_view(),name = 'list_view'),
    # path("",detail.as_view(),name = 'detail_view'),

    path('', views.lib, name='lib'),
    path('shopping', views.list_view, name='list_view'),
    path('<title>', views.detailed_view, name='detailed_view'),
    path('<title>/update', views.update_view, name='update_view'),
    path('<title>/delete', views.delete_view, name='delete_view'),
]