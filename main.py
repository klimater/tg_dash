import asyncio
import logging

from CONFIG.config import TOKKEN

import keyboards.keyboards as kb
import states as states
import data_base.database as BD

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

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
async def message_svodka(message: Message, state: FSMContext):
    await state.set_state(states.add_sels.date)
    await message.answer("Введите дату продажи dd.mm.yyyy")

@dp.message(states.add_sels.date)
async def add_sele(message: Message, state: FSMContext):
    await state.update_data(date = message.text)
    await state.set_state(states.add_sels.name)
    await message.answer("Введите название товара")

@dp.message(states.add_sels.name)
async def message_svodka(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(states.add_sels.category)
    await message.answer("Выберите категорию товара", reply_markup = kb.category_but)

@dp.message(states.add_sels.category)
async def message_svodka(message: Message, state: FSMContext):
    await state.update_data(category = message.text)
    await state.set_state(states.add_sels.quantity)
    await message.answer("ВВедите количество проданноо товара")

@dp.message(states.add_sels.quantity)
async def message_svodka(message: Message, state: FSMContext):
    await state.update_data(quantity = message.text)
    await state.set_state(states.add_sels.cost)
    await message.answer("ВВедите стоимость тоавара")

@dp.message(states.add_sels.cost)
async def message_svodka(message: Message, state: FSMContext):
    await state.update_data(cost = message.text)
    data = await state.get_data()
    await message.answer(BD.add_sale_bd(data["date"], data['name'], data['category'], data['quantity'], data['cost']))

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