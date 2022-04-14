from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import Movies, Booking
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def func(request):

    return JsonResponse({"welcome to Product ShowTime":{"Url to get whole movie list":"base_url/latest_shows",
                                        "Url for booking" :"base_url/booking/<primary key of that movie>",
                                        "Url to get your all latest bookings" : "base_url/show_booked"},
                        "Note": "User authentication necessary for booking and getting booked shows data"})


# API: 1
def latest_shows(request):

    # For extracting all the available Shows

    list = []
    movie_list = Movies.objects.all()
    for i in movie_list:
        list.append({"title":i.title,"ID":i.id})
    return JsonResponse({"Movie_list":list})


# API: 2
def booking(request,pk):
    # API for booking ticket with id as pk
    movie_instance = Movies.objects.get(id=pk)

    if request.user.is_authenticated:
        user_instance = request.user
        if Booking.objects.filter(Q(booked_by=user_instance) & Q(movie=movie_instance)).exists():
            return JsonResponse({"status":f"{movie_instance} is already booked by you"})
        else:
            booking_instance=Booking.objects.create(booked_by=user_instance,movie=movie_instance)
            booking_instance.save()
            return JsonResponse({"status":f"Booking confirm for {movie_instance}"})
    else:
        return JsonResponse({"Movie_name":movie_instance.title, "Status":"Booking denied, user found unauthenticated"})


# API: 3
@login_required()
def show_booked(request):
    # API to show all booking of current User
    list = []
    user_instance = request.user
    booking_list = Booking.objects.filter(booked_by=user_instance)
    for i in booking_list:
        list.append(i.movie.title)
    if len(list) == 0:
        return JsonResponse({"Your_booking":"None"})
    else:
        return JsonResponse({"Your_booking":list})
