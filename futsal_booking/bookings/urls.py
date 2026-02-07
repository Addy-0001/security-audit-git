from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('available-slots/', views.available_slots, name='available_slots'),
    path('create-booking/', views.create_booking, name='create_booking'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('booking/<uuid:booking_id>/',
         views.booking_detail, name='booking_detail'),
    path('booking/<uuid:booking_id>/cancel/',
         views.cancel_booking, name='cancel_booking'),
    path('api/check-availability/', views.check_slot_availability,
         name='check_availability'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
