from aiogram import types
from aiogram.dispatcher.filters import Text

from data.Texts import gen_profile_text
from keyboards.inline.profile import profile_kb
from loader import dp, bot
from utils.db_api.db_commands import get_user_data


@dp.callback_query_handler(Text(equals='profile_state'))
async def profile(callback: types.CallbackQuery):
    user_data = await get_user_data(callback.from_user.id)
    text = gen_profile_text(user_data.name,
                            user_data.balance,
                            user_data.bought,
                            user_data.username)

    await bot.edit_message_text(text=text,
                                message_id=callback.message.message_id,
                                chat_id=callback.from_user.id,
                                reply_markup=profile_kb)
