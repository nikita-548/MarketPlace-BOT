from aiogram.dispatcher.filters.state import StatesGroup, State


class UserState(StatesGroup):
    add_balance_state = State()
