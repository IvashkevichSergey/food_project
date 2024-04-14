from django.contrib import admin

from food.models import FoodCategory, Food


@admin.register(Food)
class ContactsAdmin(admin.ModelAdmin):
    pass


@admin.register(FoodCategory)
class ProductsAdmin(admin.ModelAdmin):
    pass
