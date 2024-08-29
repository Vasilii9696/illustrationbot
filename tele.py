import asyncio
import os

import aiogram
from telethon import TelegramClient, events
from aiogram import Bot
from aiogram.utils.exceptions import BadRequest, BotBlocked
from funcs import read_file
from database import Database
from main import bot
from choosekatgory import userkats, choose_category

api_id =
api_hash = ""
session_name = "botvacansiy"

# Удаление старого файла сессии, если он существует
# if os.path.exists(f"{session_name}.session"):
#    os.remove(f"{session_name}.session")

client = TelegramClient(session_name, api_id, api_hash, system_version="4.16.30-vxCUSTOM")

database = Database("database.db")

bans = ["моё портфолио", "меня зовут", "я могу", "продам", "предлагаю свои услуги", "настрою", "я твoй  таргeтолoг",
        "сделаю для вас"]


def checker(mess):
    bans = read_file("banf.txt")
    for i in bans.split("$"):
        if i.strip() in mess:
            return False
    return True


@client.on(events.NewMessage)
async def main(event):
    message = event.message
    text = message.text
    if str(message.chat_id)[0] != '-':
        return print('e')
    d = 0
    if message.sender is not None:
        f = message.sender.username
    else:
        f = ''
    if checker(message.text.lower()) and f != "ChatKeeperBot" and "🔤" not in message.text:
        kats = choose_category(message.text.lower())
        if not kats or kats == []:
            return
        users: list = database.get_users_ru()
        stringk = ''
        for i in set(kats):
            stringk += f"#{i} "
        for user in users:
            if userkats(user, kats):
                try:
                    try:
                        await bot.send_message(user,
                                               f'Новое сообщение с вакансиями {stringk}\n\n{text}\n\nИз группы @{message.chat.username}\nОт пользователя @{message.sender.username}\nСсылка: https://t.me/{message.sender.username}/{message.id}')
                    except aiogram.utils.exceptions.UserDeactivated:
                        pass
                except Exception as e:
                    print(e)
                    pass


client.start()
client.run_until_disconnected()