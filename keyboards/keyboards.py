from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text= "Сводка📊")], 
    [KeyboardButton(text= "Действие🔨")]
], resize_keyboard = True)