from django.urls import path
from . import views



urlpatterns = [
    path('addVideo/',views.GetuploadedVideo.as_view(),name='getVideo'),
]