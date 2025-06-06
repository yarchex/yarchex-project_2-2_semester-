from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from services.poizon_parser import parse_poizon_item
from utils.redis_cache import cache
from models.order import Order
import logging

logger = logging.getLogger(__name__)

class OrderStates(StatesGroup):
    waiting_for_link = State()
    waiting_for_payment = State()
    waiting_for_size = State()

@dp.message_handler(commands=['new_order'])
async def cmd_new_order(message: types.Message):
    await OrderStates.waiting_for_link.set()
    await message.answer("🔗 Отправьте ссылку на товар в Poizon:")

@dp.message_handler(state=OrderStates.waiting_for_link)
async def process_poizon_link(message: types.Message, state: FSMContext):
    try:
        # Кэшируем запрос
        item_data = await cache.get_or_set(
            f"poizon:{message.text}",
            lambda: parse_poizon_item(message.text),
            ttl=300
        )
        
        await state.update_data(item_data)
        await OrderStates.waiting_for_size.set()
        
        # Формируем клавиатуру с размерами
        sizes_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for size in item_data['available_sizes']:
            sizes_kb.add(size)
            
        await message.answer("Выберите размер:", reply_markup=sizes_kb)
        
    except Exception as e:
        logger.error(f"Error processing Poizon link: {e}")
        await message.answer("❌ Ошибка обработки ссылки")
        await state.finish()
