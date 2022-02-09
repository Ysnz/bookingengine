import pytest
from django.test import Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from listings.models import HotelRoom, HotelRoomType, Listing, BookingInfo


class ListingTests(APITestCase):
    def test_listing(self):

        url = reverse("listings")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BookingInfoTests(APITestCase):
    def test_listing(self):

        url = reverse("bookingInfos")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AllRoomsTests(APITestCase):
    def test_listing(self):

        url = reverse("allRooms")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AvailableTests(APITestCase):
    def test_listing(self):

        url = reverse("units")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
