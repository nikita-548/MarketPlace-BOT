from aiogram import types
from admin_panel.admin_panel.settings import MEDIA_ROOT
from handlers.users.start import start_cmd
from keyboards.inline.catalog import catalog_keyboard, callback_data_catalog
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from utils.db_api.db_commands import get_product, get_numbers_of_products
import os


@dp.callback_query_handler(Text(equals='catalog'))
async def show_catalog(call: types.CallbackQuery):
    product = await get_product(product_id=1)
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.from_user.id)
    text = f'Название продукта: {product.product_name}\n' \
           f"Описание: {product.product_description}\n" \
           f'Стоимость: {product.product_price}'

    image = types.InputFile(os.path.join(MEDIA_ROOT, str(product.product_image)))
    await bot.send_photo(call.from_user.id, caption=text, photo=image,
                         reply_markup=await catalog_keyboard(product_id=1))


@dp.callback_query_handler(callback_data_catalog.filter(action=["back", "next"]))
async def show_next_product(call: types.CallbackQuery, callback_data: dict):
    action = callback_data['action']
    current_product_id = int(callback_data['product_id'])
    numbers_of_product = await get_numbers_of_products()
    new_product_id = 1

    if action == 'next':
        if current_product_id == int(numbers_of_product):
            current_product_id += 1
        new_product_id = (int(current_product_id) + 1) % int(numbers_of_product + 1)

    elif action == 'back':
        if current_product_id == 1:
            current_product_id -= 1
        new_product_id = (int(current_product_id) - 1) % int(numbers_of_product + 1)

    product = await get_product(new_product_id)
    text = f'Название продукта: {product.product_name}\n' \
           f'Описание: {product.product_description}\n' \
           f'Стоимость: {product.product_price}'
    photo = types.InputMedia(media=types.InputFile(os.path.join(MEDIA_ROOT, str(product.product_image))), caption=text)
    await call.message.edit_media(media=photo, reply_markup=await catalog_keyboard(product_id=new_product_id))


@dp.callback_query_handler(Text(equals='go_to_menu'))
async def go_to_menu_from_catalog(call: types.CallbackQuery):
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.from_user.id)
    await start_cmd(call.message)


@dp.callback_query_handler(callback_data_catalog.filter(action=["buy"]))
async def buy_function(call: types.CallbackQuery):
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.from_user.id)
    await call.message.edit_text('Тут будет проверка наличия товара в базе данных')
