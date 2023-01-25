from aiogram import types
from admin_panel.admin_panel.settings import MEDIA_ROOT
from data.Texts import Texts
from keyboards.inline.catalog import catalog_keyboard, callback_data_catalog
from keyboards.inline.start import start_reply_kb
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from utils.db_api.db_commands import get_product, get_numbers_of_products, get_all_ids, get_user_data, buy_product
import os


@dp.callback_query_handler(Text(equals='menu_state'))
async def show_catalog(call: types.CallbackQuery):
    local_id = 0
    product_id = await local_to_real_id(0)
    product = await get_product(product_id=product_id)
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.from_user.id)
    text = f'Название продукта: {product.product_name}\n' \
           f"Описание: {product.product_description}\n" \
           f'Стоимость: {product.product_price}'

    image = types.InputFile(os.path.join(MEDIA_ROOT, str(product.product_image)))
    await bot.send_photo(call.from_user.id, caption=text, photo=image,
                         reply_markup=await catalog_keyboard(product_id=local_id))


async def local_to_real_id(product_id: int) -> int:
    real_ids_product_list = await get_all_ids()
    return list(real_ids_product_list)[product_id]


@dp.callback_query_handler(callback_data_catalog.filter(action=["back", "next"]))
async def show_next_product(call: types.CallbackQuery, callback_data: dict):
    action = callback_data['action']
    current_local_product_id = int(callback_data['product_id'])
    numbers_of_product = await get_numbers_of_products()
    new_local_product_id = 0
    if action == 'next':
        new_local_product_id = (int(current_local_product_id) + 1) % int(numbers_of_product)
    elif action == 'back':
        new_local_product_id = (int(current_local_product_id) - 1) % int(numbers_of_product)

    new_product_id = await local_to_real_id(new_local_product_id)
    product = await get_product(new_product_id)
    text = f'Название продукта: {product.product_name}\n' \
           f'Описание: {product.product_description}\n' \
           f'Стоимость: {product.product_price}'
    photo = types.InputMedia(media=types.InputFile(os.path.join(MEDIA_ROOT, str(product.product_image))), caption=text)
    await call.message.edit_media(media=photo, reply_markup=await catalog_keyboard(product_id=new_local_product_id))


@dp.callback_query_handler(Text(equals='go_to_menu'))
async def go_to_menu_from_catalog(call: types.CallbackQuery):
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.from_user.id)
    reply = start_reply_kb()
    text = Texts['start_state']
    await call.message.answer(text=text, reply_markup=reply)


@dp.callback_query_handler(callback_data_catalog.filter(action=["buy"]))
async def buy_function(call: types.CallbackQuery, callback_data: dict):

    current_local_product_id = int(callback_data['product_id'])
    product_id = await local_to_real_id(current_local_product_id)
    product = await get_product(product_id=product_id)
    user = await get_user_data(call.from_user.id)

    if product.product_quantity == 0:
        await call.answer('Товара нет в наличии', show_alert=True)
    elif product.product_price > user.balance:
        await call.answer('Недостаточно средств', show_alert=True)
    else:
        await buy_product(call.from_user.id, product_id, product.product_price)
        await call.answer('Товар приобретен', show_alert=True)
