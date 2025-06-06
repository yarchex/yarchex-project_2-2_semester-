from aiogram import types
from aiogram.dispatcher import FSMContext
from states.order_states import OrderStates
from services.poizon_parser import parse_poizon_item
from keyboards.builders import size_keyboard

@dp.message_handler(commands=["new_order"], state=None)
async def cmd_new_order(message: types.Message):
    await OrderStates.waiting_for_link.set()
    await message.answer("Отправьте ссылку на товар:")

@dp.message_handler(state=OrderStates.waiting_for_link)
async def process_link(message: types.Message, state: FSMContext):
    item = await parse_poizon_item(message.text)
    await state.update_data(item=item)
    await OrderStates.waiting_for_size.set()
    await message.answer("Выберите размер:", reply_markup=size_keyboard(item["sizes"]))
