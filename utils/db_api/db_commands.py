import datetime

from asgiref.sync import sync_to_async

from admin_panel.telebot.models import Product
from django.db.models import Count

@sync_to_async()
def get_product(product_id):
    return Product.objects.filter(id=product_id).first()

@sync_to_async()
def get_numbers_of_products():
    return Product.objects.count()