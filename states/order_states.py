from aiogram.dispatcher.filters.state import StatesGroup, State

class OrderStates(StatesGroup):
    waiting_for_link = State()
    waiting_for_size = State()
    waiting_for_payment = State()
    waiting_for_address = State()
    confirmation = State()
