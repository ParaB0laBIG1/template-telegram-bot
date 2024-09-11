"""File for launching a bot"""
import os
import logging

from dotenv import load_dotenv

from aiogram import Dispatcher, Bot
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from tgbot.callbacks import navigation


def setup_logging():
    log_level = logging.INFO

    logging.basicConfig(
        level=log_level,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")


async def main():
    setup_logging() 
    load_dotenv(".env")
    bot = Bot(token=os.getenv("BOT_TOKEN"), 
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    dp.workflow_data.update(bot=bot)

    dp.include_routers(
        navigation.router
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Бот був вимкнений!")
