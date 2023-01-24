from aiogram.types import InlineKeyboardMarkup

from keyboards.inline.back_btn import gen_back_btn

profile_kb = InlineKeyboardMarkup(row_width=1)
profile_kb.add(gen_back_btn(prev_state='start_state'))
