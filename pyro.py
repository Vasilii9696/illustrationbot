import asyncio
import time

import aiogram
from aiogram.utils.exceptions import BadRequest, BotBlocked
from pyrogram import Client
from pyrogram import filters
from pyrogram.errors.exceptions import bad_request_400
from pyrogram.types import Message
from funcs import read_file
from database import Database
from main import bot
from choosekatgory import userkats, choose_category

api_id =


api_hash = ""
app = Client("botvacansiy", api_id=api_id, api_hash=api_hash)

database = Database("database.db")

bans = ["моё портфолио", "меня зовут", "я могу", "продам", "предлагаю свои услуги", "настрою", "я твoй  таргeтолoг",
        "сделаю для вас"]


def checker(mess):
    bans = read_file("banf.txt")
    for i in bans:
        if i in mess:
            return False
    return True


@app.on_message()
async def main(client: Client, message: Message):
    text = message.text
    d = 0
    f = message.chat.username
    
    if checker(message.text.lower()) and message.from_user.username != "ChatKeeperBot" and "🔤" not in message.text:

        kats = choose_category(message.text.lower())
        if not kats or kats == []:
            return
        users: list = database.get_users_ru()
        stringk = ''
        for i in set(kats):
            stringk += f"#{i} "
        for user in users:
            if userkats(user, kats):
                print(user)
                try:
                    try:
                        await bot.send_message(user,
                                               f'Новое сообщение с вакансиями {stringk}\n\n{text}\n\nИз группы @{message.chat.username}\nОт пользователя @{message.from_user.username}\nСсылка: {message.link}')
                    except aiogram.utils.exceptions.UserDeactivated:
                        pass
                except Exception as e:
                    print(e)
                    pass

app.run()
