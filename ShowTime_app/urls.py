from django.urls import path
from . import views

urlpatterns = [
    path("",views.func),
    path("latest_shows",views.latest_shows, name="get_shows"),
    path("booking/<str:pk>/",views.booking, name="booking"),
    path("show_booked", views.show_booked, name="show_booked")
    ]

