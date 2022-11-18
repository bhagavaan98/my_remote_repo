from django.urls import path
from . import views
urlpatterns=[
    path('done/',views.deposit1_details),
    path('dtwo/',views.deposit2_details),
    path('dthree/',views.deposit3_details),
]