"""File for launching a bot"""
import logging
import os
from contextlib import suppress

from dotenv import load_dotenv
from aiogram import Dispatcher, Bot, F

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.bot import DefaultBotProperties

from tgbot.keyboards.builders import inline_builder
from tgbot.callbacks import navigation
from tgbot import config


def setup_logging():
    log_level = logging.INFO

    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")



async def main():
    setup_logging() 
    load_dotenv(".env")

    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(
        navigation.router
    )
    await dp.start_polling(config.bot)


if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Бот був вимкнений!")
