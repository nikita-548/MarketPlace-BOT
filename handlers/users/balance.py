from aiogram import types

from keyboards.inline.balance import gen_balance_kb
from keyboards.inline.start import start_reply_kb
from loader import dp, bot
from aiogram.dispatcher import FSMContext

from states.states import UserState
from data.Texts import Texts
from utils.db_api.db_commands import update_balance


@dp.callback_query_handler(text='balance_state_from_catalog')
async def balance_state_from_catalog(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserState.add_balance_state)
    text = Texts['balance_state']
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)

    new_message = await bot.send_message(chat_id=callback.from_user.id,
                           text=text,
                           reply_markup=gen_balance_kb())

    await state.update_data(prev_msg_id=new_message.message_id,
                            add_to_balance=0)


@dp.callback_query_handler(text='balance_state')
async def balance_state(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserState.add_balance_state)
    text = Texts['balance_state']

    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.from_user.id,
                                text=text,
                                reply_markup=gen_balance_kb())
    await state.update_data(prev_msg_id=callback.message.message_id,
                            add_to_balance=0)


@dp.callback_query_handler(text='add_balance_state')
@dp.callback_query_handler(state=UserState.add_balance_state)
async def send_state_msg(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if callback.data != 'add_balance_state':
        text = Texts['start_state']
        reply = start_reply_kb()
    else:
        text = f"Вы пополнили баланс на {data['add_to_balance']}"
        reply = gen_balance_kb()
        await update_balance(callback.from_user.id, data['add_to_balance'])
    await state.finish()
    await bot.edit_message_text(message_id=callback.message.message_id,
                                chat_id=callback.from_user.id,
                                text=text,
                                reply_markup=reply)


@dp.message_handler(state=UserState.add_balance_state)
async def balance_state_add(message: types.Message, state: FSMContext):
    prev_msg_id = await state.get_data()
    if not message.text.isdigit():
        await bot.edit_message_text(chat_id=message.from_user.id,
                                    message_id=prev_msg_id['prev_msg_id'],
                                    text=f'Введите целое число, а не {message.text}',
                                    reply_markup=gen_balance_kb())
        await bot.delete_message(message.from_user.id, message_id=message.message_id)
    else:
        await bot.edit_message_text(chat_id=message.from_user.id,
                                    message_id=prev_msg_id['prev_msg_id'],
                                    text=f'Добавить к балансу {message.text} ?',
                                    reply_markup=gen_balance_kb(confirm=True))
        await state.update_data(add_to_balance=int(message.text))
        await bot.delete_message(message.from_user.id, message_id=message.message_id)
