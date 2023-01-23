from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from keyboards.inline.menu import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer('Меню', reply_markup=menu)