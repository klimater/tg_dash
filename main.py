import asyncio
import logging

from config import TOKKEN

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

bot = Bot(token=TOKKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.info("Bot is starting...")
    asyncio.run(main())