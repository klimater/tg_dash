from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text= "Сводка за день📊")], 
    [KeyboardButton(text= "Показать продажи за сегодня📝")]
], resize_keyboard = True)

main_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text= "Главное меню")]
], resize_keyboard = True)
