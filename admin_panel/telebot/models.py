from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class CreatedModel(models.Model):
    """Абстрактная модель. Добавляет дату создания."""
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата изменения")

    class Meta:
        abstract = True


# id name description price
class Product(CreatedModel):
    product_name = models.CharField(
        verbose_name='Наименование продукта',
        help_text='Наименование продукта',
        max_length=500
    )

    product_description = models.CharField(
        verbose_name='Описание товара',
        help_text='Описание товара',
        max_length=1000
    )

    product_price = models.FloatField(
        verbose_name='Стоимость продукта',
        help_text='Стоимость продукта',
    )

    product_quantity = models.IntegerField(
        verbose_name='Количество товара',
        help_text='Количество товара',
        default=1
    )

    product_image = models.CharField(
        verbose_name='Id фото',
        help_text='Id фото',
        max_length=1000
    )


class Users(models.Model):
    user_id = models.IntegerField(
        verbose_name='Юзер ID',
        help_text='Юзер ID',
        max_length=100
    )
    balance = models.IntegerField(
        verbose_name='Баланс',
        help_text='Баланс',
        default=0,
        max_length=100
    )
    bought = models.IntegerField(
        verbose_name='Количество покупок',
        help_text='Количество покупок',
        default=0,
        max_length=100
    )
    name = models.CharField(
        verbose_name='Имя пользователя',
        help_text='Имя пользователя',
        default='None',
        max_length=100
    )
    username = models.CharField(
        verbose_name='username',
        help_text='username',
        default='None',
        max_length=100
    )
