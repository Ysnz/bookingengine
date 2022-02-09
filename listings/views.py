from django.shortcuts import render

# Create your views here.
from rest_framework import status, views, generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Listing, BookingInfo, HotelRoom
from .serializers import (
    ListingSerializer,
    BookingInfoSerializer,
    AvailableListingsSerializer,
)
from .filters import HotelRoomFilter


class ListingView(views.APIView):
    serializer_class = ListingSerializer

    def get(self, request):
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True)

        data = serializer.data

        response_payload = {
            "status": {"message": "success", "code": f"{status.HTTP_200_OK} OK"},
            "listings": data,
        }

        return Response(response_payload, status=status.HTTP_200_OK)


class BookingInfoView(views.APIView):
    serializer_class = BookingInfoSerializer

    def get(self, request):
        bookingInfo = BookingInfo.objects.all().order_by("price")
        serializer = BookingInfoSerializer(bookingInfo, many=True)

        data = serializer.data

        response_payload = {
            "status": {"message": "success", "code": f"{status.HTTP_200_OK} OK"},
            "bookingInfos": data,
        }

        return Response(response_payload, status=status.HTTP_200_OK)


class AllHotelRoomsView(views.APIView):
    serializer_class = AvailableListingsSerializer

    def get(self, request):
        hotelRoom = HotelRoom.objects.all().order_by("price")
        serializer = AvailableListingsSerializer(hotelRoom, many=True)

        data = serializer.data

        response_payload = {
            "status": {"message": "success", "code": f"{status.HTTP_200_OK} OK"},
            "hotelRooms": data,
        }

        return Response(response_payload, status=status.HTTP_200_OK)


class AvailableListingsView(generics.ListAPIView):
    serializer_class = AvailableListingsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HotelRoomFilter
    queryset = HotelRoom.objects.all().order_by("price")
