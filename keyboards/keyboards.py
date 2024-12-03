from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text= "Сводка📊")], 
    [KeyboardButton(text= "Показать продажи за сегодня🔨")]
], resize_keyboard = True)
