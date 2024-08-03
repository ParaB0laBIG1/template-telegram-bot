from aiogram.filters import BaseFilter
from aiogram.types import Message


# class IsDigit(BaseFilter):

#     async def __call__(self, message: Message) -> bool:
#         if message.text.isnumeric() or (message.text.count(".")) == 1 and message.text:
#             return True
#         return False
    


"""С помощью регулярных выражений"""
import re

from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsDigit(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        pattern = re.compile(r"^\d+(\.\d+)?$")
        return False if not pattern.match(message.text) else True