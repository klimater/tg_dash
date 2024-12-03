from aiogram.fsm.state import StatesGroup, State

class add_sels(StatesGroup):
    date = State()
    name = State()
    category = State()
    quantity = State()
    cost = State()

class delete_sale(StatesGroup):
    date = State()
    name = State()
    count_elem = State()