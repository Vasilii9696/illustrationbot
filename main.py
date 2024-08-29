from typing import List

import aiogram
import aiohttp
from aiogram import Bot, Dispatcher, executor, types
from config import database, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import sqlite3
import asyncio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.exceptions import BadRequest
from upwork import get_job_descriptions
from keyboards.inline_buttons import kategories, menu_buttons, home_buttons, originals, kategoryk, kategoryo
from asyncio import exceptions


async def get_users(id):
    if await get_users1(id) or await get_users2(id):
        return True
    return False


async def get_users2(id):
    try:
        if id == :
            return True
        chat_members = await bot.get_chat_member(, id)
        if chat_members["status"] == 'left':
            print('fsdfdsf')
            return False
        return True

    except BadRequest as e:
        print(e)
        return False


async def get_users1(id):
    try:

        chat_members = await bot.get_chat_member(, id)
        if chat_members["status"] == 'left':
            print('fsdfdsf')
            return False
        return True

    except BadRequest as e:
        print(e)
        return False


logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


class Choose_time(StatesGroup):
    chtime = State()


bcackb = InlineKeyboardMarkup(row_width=1)
bcackb.add(InlineKeyboardButton(text=f'Назад', callback_data='backb'))

beg_ch = InlineKeyboardMarkup(row_width=1)
beg_ch.add(InlineKeyboardButton(text=f'Приступить к настройке', callback_data='begin'))

bcackb2 = InlineKeyboardMarkup(row_width=1)
bcackb2.add(InlineKeyboardButton(text=f'Назад', callback_data='backb2'))

bcackb3 = InlineKeyboardMarkup(row_width=1)
bcackb3.add(InlineKeyboardButton(text=f'Назад', callback_data='backb3'))

bcackb4 = InlineKeyboardMarkup(row_width=1)
bcackb4.add(InlineKeyboardButton(text=f'Назад', callback_data='backb4'))


class StartS(StatesGroup):
    begin_ch = State()
    inpk = State()
    inpl = State()
    choose_time = State()


ktext = """
Добро пожаловать! Пожалуйста, выберите категорию, которая вас интересует 👇🏻"""

ortext = """
Прекрасный выбор! Кроме того, наш сервис также предлагает заказы из разных уголков мира 

Вы можете выбрать поиск заказов по рынку РФ, иностранному рынку или же оба варианта вместе - главное, убедитесь в возможности принимать оплату из-за рубежа. Выберите, какие предложения вам интереснее:
"""

dictkats = {
    '0': "neiro",
    '1': "design"
}

katsdn = {'0': '✅', '1': ' ', '2': '✅'}
katsdd = {'0': ' ', '1': '✅', '2': '✅'}
katsdr = {'0': '✅', '1': ' ', '2': '✅'}
katsde = {'0': ' ', '1': '✅', '2': '✅'}

dictkats2 = {
    '0': "russian",
    '1': "american"
}

katsegorieslist = ["target",
                   "smm",
                   "site",
                   "contecst",
                   "producer",
                   "assistent",
                   "repetitor",
                   "analitics",
                   "photographer",
                   "houses",
                   "reels",
                   "designer"
                   ]

redacted_text = """Категория выбрана✅

Бот начал работу

Теперь нужно немного подождать, в течение суток бот обработает объявления и пришлет вам вакансии

‼️Пожалуйста, не нажимайте категории повторно несколько раз"""

start_text = """
Добро пожаловать текст1 


"""

time_text = """
 Вы сделали прекрасный выбор категорий и источников заказов, осталось совсем чуть-чуть! 

Пожалуйста, укажите временной промежуток (по мск), в который вы хотели бы получать уведомления о новых заказах от 0 до 24 в следующем формате: 8-18 (данный формат означает рабочий день с 8:00 до 18:00 по мск)
Чтобы получать заказы все время, введите 0-24 👇🏻"""

rukv_text = """
Здесь должна быть памятка
"""

menu_t = """

"""
kattext = ""

aboutb = """
здесь будет текст о боте
"""

rukv_t = """
🗝️ РУКОВОДСТВО 

️"""

about_text = """
🗝️ О ПРОЕКТЕ:

"""


 # kategory = InlineKeyboardMarkup(row_width=1)
 # kategory.add(
 #     InlineKeyboardButton(text=f'Таргет', callback_data='d0'),
 #     InlineKeyboardButton(text=f'SMM ', callback_data='d1'),
 #     InlineKeyboardButton(text=f'Сайты ', callback_data='d2'),
 #     InlineKeyboardButton(text=f'Контекст ', callback_data='d3'),
 #     InlineKeyboardButton(text=f'Продюсер', callback_data='d4'),
 #     InlineKeyboardButton(text=f'Ассистент ', callback_data='d5'),
 #     InlineKeyboardButton(text=f'Репетитор ', callback_data='d6'),
 #     InlineKeyboardButton(text=f'Аналитика ', callback_data='d7'),
 #     InlineKeyboardButton(text=f'Фотограф ', callback_data='d8'),
 #     InlineKeyboardButton(text=f'Недвижимость ', callback_data='d9'),
 #     InlineKeyboardButton(text=f'Всё ', callback_data='d10')
 # )

@dp.message_handler(commands=['start'])
async def start(message: types.Message, state: FSMContext):
    if not await get_users(message.from_user.id):
        return await bot.send_message(message.from_user.id, 'вы не в клубе')

    if not database.user_exist(message.from_user.id):
        with open('photo_2024-06-06_15-03-20.jpg', 'rb') as photo1_file:
            await bot.send_photo(message.from_user.id, photo1_file, caption="""Добро пожаловать! Прежде чем мы покажем вам номера с самыми интересными заказами и проектами, позвольте нам узнать немного больше о ваших предпочтениях ♥️ 

мы предлагаем разнообразные категории заказов, чтобы каждый гость мог найти то, что ему по душе. Пожалуйста, выберите категорию, которая вас интересует 👇🏻""",
                                 reply_markup=kategoryk)
            await StartS.inpk.set()
    else:
        with open('photo_2024-06-06_15-03-20.jpg', 'rb') as photo1_file:
            await bot.send_photo(message.from_user.id, photo1_file, caption=start_text)


@dp.message_handler(text="🤑 Категории заявок")
async def tp3(message: types.Message):
    if not await get_users(message.from_user.id):
        return
    await bot.send_message(message.from_user.id, "Выберите категорию:",
                           reply_markup=kategories(message.from_user.id, database))


@dp.message_handler(commands=["category"])
async def ckatss(message: types.Message):
    if not await get_users(message.from_user.id):
        return
    with open('photo_2024-06-06_15-03-20.jpg', 'rb') as photo1_file:
        await bot.send_photo(message.from_user.id, photo1_file, caption=ktext,
                             reply_markup=kategories(message.from_user.id, database))


@dp.callback_query_handler(text="begin", state=StartS.begin_ch)
async def begch(call: types.CallbackQuery, state: FSMContext):
    if not await get_users(call.from_user.id):
        return
    await call.message.edit_caption("""Прекрасный выбор! Кроме того, наш сервис также предлагает заказы из разных уголков мира ♥️ 
 
Вы можете выбрать поиск заказов по рынку РФ, иностранному рынку или же оба варианта вместе - главное, убедитесь в возможности принимать оплату из-за рубежа. Выберите, какие предложения вам интереснее:""",
                                    reply_markup=kategoryk)
    await StartS.inpk.set()


@dp.message_handler(commands=["source"])
async def okatss(call: types.CallbackQuery):
    if not await get_users(call.from_user.id):
        return
    with open('photo_2024-06-06_15-03-20.jpg', 'rb') as photo1_file:
        await bot.send_photo(call.from_user.id, photo1_file, caption=ktext,
                             reply_markup=originals(call.from_user.id, database))


@dp.callback_query_handler(text="backb")
async def back_b(call: types.CallbackQuery):
    if not await get_users(call.from_user.id):
        return
    await call.message.edit_caption(start_text, reply_markup=home_buttons)


@dp.callback_query_handler(text="backb", state=Choose_time)
async def back_b1(call: types.CallbackQuery, state: FSMContext):
    if not await get_users(call.from_user.id):
        return
    await state.finish()
    await call.message.edit_caption("Успешно отменено")


@dp.callback_query_handler(text="backb2")
async def back_b2(call: types.CallbackQuery):
    if not await get_users(call.from_user.id):
        return
    await call.message.delete()
    with open('photo_2024-06-06_15-03-20.jpg', 'rb') as photo1_file:
        await bot.send_photo(call.from_user.id, photo1_file, caption=start_text, reply_markup=home_buttons)


@dp.callback_query_handler(text="backb3")
async def back_b(call: types.CallbackQuery):
    if not await get_users(call.from_user.id):
        return
    await call.message.edit_caption(menu_t, reply_markup=menu_buttons)


@dp.callback_query_handler(text="backb4")
async def back_42(call: types.CallbackQuery):
    if not await get_users(call.from_user.id):
        return
    await call.message.delete()
    with open('photo_2024-06-06_15-03-20.jpg', 'rb') as photo1_file:
        await bot.send_photo(call.from_user.id, photo1_file, caption=menu_t, reply_markup=menu_buttons)


@dp.callback_query_handler(text_startswith="ori")
async def orss(call: types.CallbackQuery):
    if not await get_users(call.from_user.id):
        return
    print('gdfgfdg')
    if call.data == "ori2":
        database.updateint("russian", "✅", call.from_user.id)
        database.updateint("american", "✅", call.from_user.id)
    else:
        if str(database.select_ints(call.from_user.id, dictkats2[call.data[3:]]).strip()) == "✅":
            print('gdfgfdg')
            database.updateint(dictkats2[call.data[3:]], " ", call.from_user.id)
        else:
            database.updateint(dictkats2[call.data[3:]], "✅", call.from_user.id)
            # await bot.send_message(call.from_user.id, redacted_text)
    await call.message.edit_caption(ortext, reply_markup=originals(call.from_user.id, database))


@dp.callback_query_handler(text_startswith="kat")
async def katss(call: types.CallbackQuery):
    if not await get_users(call.from_user.id):
        return
    if call.data.strip() == "kat2":
        database.updateint("neiro", "✅", call.from_user.id)
        database.updateint("design", "✅", call.from_user.id)
    else:
        if database.select_ints(call.from_user.id, dictkats[call.data[3:]]) == "✅":
            database.updateint(dictkats[call.data[3:]], "", call.from_user.id)
        else:
            database.updateint(dictkats[call.data[3:]], "✅", call.from_user.id)
            # await bot.send_message(call.from_user.id, redacted_text)
    await call.message.edit_caption(ktext, reply_markup=kategories(call.from_user.id, database))


@dp.callback_query_handler(text_startswith="mori", state=StartS.inpl)
async def orss2(call: types.CallbackQuery, state: FSMContext):
    if not await get_users(call.from_user.id):
        return
    await state.update_data(ori=call.data[4:])
    await call.message.edit_caption(time_text)
    await StartS.choose_time.set()


@dp.callback_query_handler(text_startswith="mkat", state=StartS.inpk)
async def katss2(call: types.CallbackQuery, state: FSMContext):
    if not await get_users(call.from_user.id):
        return
    await state.update_data(kat=call.data[4:])
    await call.message.edit_caption("""Прекрасный выбор! Кроме того, наш сервис также предлагает заказы из разных уголков мира ♥️ 

Вы можете выбрать поиск заказов по рынку РФ, иностранному рынку или же оба варианта вместе - главное, убедитесь в возможности принимать оплату из-за рубежа. Выберите, какие предложения вам интереснее:""",
                                    reply_markup=kategoryo)
    await StartS.inpl.set()


@dp.message_handler(commands=["time"])
async def timeh(call: types.CallbackQuery, state: FSMContext):
    if not await get_users(call.from_user.id):
        return
    await bot.send_message(call.from_user.id, time_text, reply_markup=bcackb)
    await Choose_time.chtime.set()


@dp.message_handler(state=Choose_time.chtime)
async def timeh(message: types.Message, state: FSMContext):
    if not await get_users(message.from_user.id):
        return
    database.updateint("time", message.text, message.from_user.id)
    await bot.send_message(message.from_user.id, """ 

Нажмите на МЕНЮ и изучите весь сервис, пока мы приступаем к поиску лучших заказов для вас! Желаем приятного пребывания 🫶🏻""")
    await state.finish()


@dp.message_handler(state=StartS.choose_time)
async def timehm(message: types.Message, state: FSMContext):
    if not await get_users(message.from_user.id):
        return
    datas = await state.get_data()
    kn = katsdn[datas.get("kat")]
    kd = katsdd[datas.get("kat")]
    kr = katsdr[datas.get("ori")]
    ke = katsde[datas.get("ori")]
    database.add_us(message.from_user.id, kn, kd, kr, ke, message.text)
    await bot.send_message(message.from_user.id, "Успешно")
    await state.finish()


@dp.message_handler(commands=["guide"])
async def rukvo(call: types.CallbackQuery, state: FSMContext):
    if not await get_users(call.from_user.id):
        return
    await bot.send_message(call.from_user.id, rukv_text)


@dp.callback_query_handler(text="menu")
async def menu(call: types.CallbackQuery, state: FSMContext):
    if not await get_users(call.from_user.id):
        return
    await call.message.edit_caption(menu_t, reply_markup=menu_buttons)


@dp.callback_query_handler(text="menu")
async def menu(call: types.CallbackQuery, state: FSMContext):
    if not await get_users(call.from_user.id):
        return
    await call.message.edit_caption(menu_t, reply_markup=menu_buttons)


@dp.message_handler(commands=["aboutbot"])
async def menu(message: types.Message, state: FSMContext):
    if not await get_users(message.from_user.id):
        return
    await bot.send_message(message.from_user.id, aboutb)


@dp.callback_query_handler(text="pam")
async def menu(call: types.CallbackQuery, state: FSMContext):
    if not await get_users(call.from_user.id):
        return
    await call.message.delete()
    await bot.send_message(call.from_user.id, rukv_t, reply_markup=bcackb4)


@dp.message_handler(commands=["aboutproject"])
async def menu(call: types.Message, state: FSMContext):
    if not await get_users(call.from_user.id):
        return
    await bot.send_message(call.from_user.id, about_text)


# async def scheduler():
#    while True:
#        # await get_job_descriptions()
#        await asyncio.sleep(30)
#        await dribble()
#        await send_message_withv()
#        await asyncio.sleep(600)


if __name__ == "__main__":
    executor.start_polling(dp)
