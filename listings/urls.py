from unicodedata import name
from django.urls import path

from .views import (
    health_check,
    ListingView,
    BookingInfoView,
    AllRoomsView,
    AvailableListingsView,
)

urlpatterns = [
    path("health_check/", health_check, name="health_check"),
    path("listing/", ListingView.as_view(), name="listings"),
    path("bookingInfo/", BookingInfoView.as_view(), name="bookingInfos"),
    path("allRooms/", AllRoomsView.as_view(), name="allRooms"),
    path("units/", AvailableListingsView.as_view(), name="units"),
]
