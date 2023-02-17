from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contacts,name='contacts'),
    # path('add/',views.addition,name='addition')
]