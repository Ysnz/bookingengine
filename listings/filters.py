from django_filters import rest_framework as filters
from .models import HotelRoom


class HotelRoomFilter(filters.FilterSet):
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")
    check_in = filters.DateFilter(
        field_name="check_in", exclude=True, lookup_expr="gte"
    )
    check_out = filters.DateFilter(
        field_name="check_out", exclude=True, lookup_expr="lte"
    )

    class Meta:
        model = HotelRoom
        fields = ["check_in", "check_out", "max_price"]
