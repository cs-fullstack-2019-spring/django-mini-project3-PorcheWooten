from django.urls import path
from . import views

urlpatterns= [

    path('',views.index, name='index'),
    path('timecard/',views.timecard, name='timecard'),
    path('timecard/edit/<int:id>/', views.editcard, name='edit'),
    path('timecard/delete/<int:id>', views.deletecard, name='delete'),
    ]