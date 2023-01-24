from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_reply_kb():
    start_kb = InlineKeyboardMarkup(row_width=1)
    start_kb.add(InlineKeyboardButton(text='Каталог', callback_data='menu_state'),
                 InlineKeyboardButton(text='Баланс', callback_data='balance_state'),
                 InlineKeyboardButton(text='Профиль', callback_data='profile_state'))
    return start_kb

