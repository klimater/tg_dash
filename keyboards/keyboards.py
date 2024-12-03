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

category_but = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text= "Аксессуары")], [KeyboardButton(text= "Бытовая техника")],
    [KeyboardButton(text= "Гигиена")], [KeyboardButton(text= "Книги")],
    [KeyboardButton(text= "Красота")], [KeyboardButton(text= "Мебель")],
    [KeyboardButton(text= "Одежда")], [KeyboardButton(text= "Продукты")],
    [KeyboardButton(text= "Сантехника")], [KeyboardButton(text= "Спорт")],
    [KeyboardButton(text= "Туризм")], [KeyboardButton(text= "Электроника")],
    [KeyboardButton(text= "Художественные товары")]
], resize_keyboard = True, one_time_keyboard = True)
