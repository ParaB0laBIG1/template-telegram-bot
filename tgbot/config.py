import os
from aiogram import Bot
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode


bot = Bot(token=os.getenv("BOT_TOKEN"), 
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))