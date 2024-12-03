import asyncio
import logging

from config import TOKKEN

import keyboards.keyboards as kb

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

bot = Bot(token=TOKKEN)
dp = Dispatcher()

#Обработчик команды старт
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("""
Привет я бот🤖 учета товаров на скалде.
Давай начнем работу!
Введи эту команду /main
""")

#команда главного меню
@dp.message(Command("main"))
async def cmd_main(message: Message):
    await message.answer("""
Что хочешь сделать?
""", reply_markup = kb.main)

#Обработчик ловит текст "Сводка📊"
@dp.message(F.text == "Сводка📊")
async def message_svodka(message: Message):
    await message.answer(" СВОДКА")

#Обработчик ловит текст "Показать продажи за сегодня📝"
@dp.message(F.text == "Показать продажи за сегодня📝")
async def message_action(message: Message):
    await message.answer("данные")



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logging.info("Bot is starting...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")