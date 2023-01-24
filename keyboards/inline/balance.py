from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.back_btn import gen_back_btn


def gen_balance_kb(confirm=False):
    add_balance_btn = InlineKeyboardButton('Пополнить', callback_data='add_balance_state')
    balance_kb = InlineKeyboardMarkup(row_width=1)
    balance_kb.add(gen_back_btn('start_state'))
    if confirm:
        balance_kb.add(add_balance_btn)
    return balance_kb
