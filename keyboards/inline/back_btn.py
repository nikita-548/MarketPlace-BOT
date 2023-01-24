from aiogram.types import InlineKeyboardButton


def gen_back_btn(prev_state):
    return InlineKeyboardButton(text='Назад', callback_data=str(prev_state))
