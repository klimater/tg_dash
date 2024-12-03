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
""", reply_markup=kb.main_menu)

#команда главного меню
@dp.message(F.text == "Главное меню")
async def cmd_main(message: Message):
    await message.answer("""
Что хочешь сделать?
""", reply_markup = kb.menu)

#Обработчик ловит текст "Сводка📊"
@dp.message(F.text == "Сводка за день📊")
async def message_svodka(message: Message):
    await message.answer(" СВОДКА", reply_markup = kb.main_menu)

#Обработчик ловит текст "Показать продажи за сегодня📝"
@dp.message(F.text == "Действия📝")
async def message_action(message: Message):
    await message.answer("данные", reply_markup = kb.action)


# Добавление товара
@dp.message(F.text == "Добавить")
async def message_svodka(message: Message):
    await message.answer(" СВОДКА", reply_markup= kb.menu)

# Удаление товара
@dp.message(F.text == "Удалить")
async def message_svodka(message: Message):
    await message.answer(" СВОДКА", reply_markup= kb.menu)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logging.info("Bot is starting...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")