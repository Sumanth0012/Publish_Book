from django.urls import path
from . import views

from .views import list,detail,create,delete,update

urlpatterns = [
    # path('shop/',list.as_view(),name = 'list_view'),
    # path("<str:pk>/",detail.as_view(), name = 'book'),
    # path("",create.as_view(), name = 'book-cr'),
    # path("<str:pk>/update/",update.as_view(), name = 'book-up'),
    # path("<str:pk>/delete/",delete.as_view(), name = 'book-del'),

    path('', views.lib, name='lib'),
    path('shop/', views.list_view, name='list_view'),
    path('<id>/', views.detailed_view, name='detailed_view'),
    path('<id>/update/', views.update_view, name='update_view'),
    path('<id>/delete/', views.delete_view, name='delete_view'),
]