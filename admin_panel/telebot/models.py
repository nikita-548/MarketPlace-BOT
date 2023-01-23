from django.contrib.auth import get_user_model
from django.db import models
from django.utils.html import mark_safe

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

    product_image = models.ImageField(upload_to='images/')
