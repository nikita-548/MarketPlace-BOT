import datetime

from asgiref.sync import sync_to_async

from admin_panel.telebot.models import Product, Users
from django.db.models import Count
from django.db.models import F


@sync_to_async()
def get_product(product_id):
    return Product.objects.filter(id=product_id).first()


@sync_to_async()
def get_all_ids():
    return Product.objects.values_list('id', flat=True)


@sync_to_async()
def get_product_quantity(product_id):
    return Product.objects.filter(id=product_id).first()

@sync_to_async()
def get_numbers_of_products():
    return Product.objects.count()
@sync_to_async()
def create_user(user_id, name, username):
    Users.objects.get_or_create(user_id=user_id,
                                name=name,
                                username=username)


@sync_to_async()
def get_user_data(user_id):
    return Users.objects.filter(user_id=user_id).first()


@sync_to_async()
def update_balance(user_id, add_to_balance):
    Users.objects.filter(user_id=user_id).update(balance=F('balance') + add_to_balance)


@sync_to_async()
def buy_product(user_id, product_id, price):
    Users.objects.filter(user_id=user_id).update(balance=F('balance') - price, bought=F('bought') + 1)
    Product.objects.filter(id=product_id).update(product_quantity=F('product_quantity') - 1)
