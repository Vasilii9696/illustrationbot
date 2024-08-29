from aiogram import Bot

from database import Database
database = Database("database.db")
tok = ''

bot = Bot(token=tok, parse_mode='HTML')
