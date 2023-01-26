from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

callback_data_catalog = CallbackData('catalog_data', 'action', 'product_id')


async def catalog_keyboard(product_id):
    catalog = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data=callback_data_catalog.new(action='back',
                                                                                       product_id=product_id)),
            InlineKeyboardButton(text='Купить', callback_data=callback_data_catalog.new(action='buy',
                                                                                        product_id=product_id)),
            InlineKeyboardButton(text='Далее', callback_data=callback_data_catalog.new(action='next',
                                                                                       product_id=product_id))
        ],
        [
            InlineKeyboardButton(text='Меню', callback_data='go_to_menu')
        ]
    ])
    return catalog
