from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def start(msg: Message) -> None:
    bot = await (router.parent_router.workflow_data['bot']).get_me()

    await msg.answer(f"Hello, world!\nMy name is {bot.username}")
    