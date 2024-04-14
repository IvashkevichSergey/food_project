from django.db.models import Prefetch
from rest_framework import generics

from food.models import Food, FoodCategory
from food.serializers import FoodListSerializer


class FoodListApiView(generics.ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        prefetched_data = Prefetch(
            "food",
            queryset=Food.objects.filter(is_publish=True)
        )
        return FoodCategory.objects.\
            prefetch_related(prefetched_data).\
            filter(food__is_publish=True).distinct()
