from unicodedata import name
from django.urls import path

from .views import (
    ListingView,
    BookingInfoView,
    AllHotelRoomsView,
    AvailableListingsView,
)

urlpatterns = [
    path("listings/", ListingView.as_view()),
    path("bookingInfos/", BookingInfoView.as_view()),
    path("allRooms/", AllHotelRoomsView.as_view()),
    path("available_listings/", AvailableListingsView.as_view()),
]
