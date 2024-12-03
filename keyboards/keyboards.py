from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text= "Сводка за день📊")], 
    [KeyboardButton(text= "Показать продажи за сегодня📝")]
], resize_keyboard = True)
