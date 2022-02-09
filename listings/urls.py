from unicodedata import name
from django.urls import path

from .views import (
    ListingView,
    BookingInfoView,
    HotelRoomsView,
    AvailableListingsView,
)

urlpatterns = [
    path("listings/", ListingView.as_view()),
    path("bookingInfos/", BookingInfoView.as_view()),
    path("allRooms/", HotelRoomsView.as_view()),
    path("available_listings/", AvailableListingsView.as_view()),
]
