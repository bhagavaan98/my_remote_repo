from django.urls import path
from . import views
urlpatterns=[
    path('wone/',views.withdraw1_details),
    path('wtwo/',views.withdraw2_details),
    path('wthree/',views.withdraw3_details),
]