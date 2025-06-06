from aiogram import types
from aiogram.dispatcher import FSMContext
from filters.admin_filter import IsAdminFilter
from models.order import Order

@dp.message_handler(IsAdminFilter(), commands=["stats"])
async def cmd_stats(message: types.Message):
    stats = Order.get_stats()  # Метод для получения статистики
    await message.answer(
        f"📊 Статистика:\n"
        f"• Всего заказов: {stats['total']}\n"
        f"• На сумму: {stats['total_amount']} ¥"
    )

@dp.message_handler(IsAdminFilter(), commands=["broadcast"])
async def cmd_broadcast(message: types.Message, state: FSMContext):
    await message.answer("Введите сообщение для рассылки:")
    await state.set_state("broadcast_message")

@dp.message_handler(state="broadcast_message")
async def process_broadcast(message: types.Message, state: FSMContext):
    users = Order.get_all_users()  # Получаем всех пользователей
    for user in users:
        try:
            await bot.send_message(user.id, message.text)
        except Exception as e:
            logging.error(f"Broadcast error for {user.id}: {e}")
    await state.finish()
