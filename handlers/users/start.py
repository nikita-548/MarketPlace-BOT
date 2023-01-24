from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from keyboards.inline.start import start_reply_kb
from loader import dp, bot
from utils.db_api.db_commands import create_user

from data.Texts import Texts


# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#    await message.answer('Меню', reply_markup=menu)


@dp.message_handler(CommandStart())
async def start_cmd(message: types.Message):
    name = message.from_user.first_name
    name += message.from_user.last_name if message.from_user.last_name is not None else ''
    username = message.from_user.username if message.from_user.username is not None else ''

    await create_user(user_id=message.from_user.id, name=name, username=username)
    reply = start_reply_kb()
    text = Texts['start_state']
    await bot.send_message(chat_id=message.from_user.id,
                           text=text,
                           reply_markup=reply)


@dp.callback_query_handler(text='start_state')
async def start_cmd(callback: types.CallbackQuery):
    reply = start_reply_kb()
    text = Texts['start_state']
    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.from_user.id,
                                text=text,
                                reply_markup=reply)
