from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text= "Сводка за день📊")], 
    [KeyboardButton(text= "Действия📝")]
], resize_keyboard = True)

main_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text= "Главное меню")]
], resize_keyboard = True)

action = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text= "Добавить")], 
    [KeyboardButton(text= "Удалить")]
], resize_keyboard = True)
