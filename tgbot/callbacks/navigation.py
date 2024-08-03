from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def start(msg: Message) -> None:
    await msg.answer("Hello, world!")