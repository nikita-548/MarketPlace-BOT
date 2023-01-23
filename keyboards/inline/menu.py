from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    [
        InlineKeyboardButton(text='Каталог', callback_data='catalog')
    ],
    [
        InlineKeyboardButton(text='Баланс', callback_data='test1')
    ],
    [
        InlineKeyboardButton(text='Профиль', callback_data='test2')
    ]
])
