from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline import language_keyboard

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer(
        "🛒 Бот для заказов из Poizon",
        reply_markup=language_keyboard()
    )

@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await message.answer("Список команд: /new_order, /my_orders, /cancel")
