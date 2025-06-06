from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage
from config.settings import settings
from middlewares.throttling import ThrottlingMiddleware
from filters.admin_filter import IsAdminFilter

# Инициализация
bot = Bot(token=settings.BOT_TOKEN)
storage = RedisStorage.from_url(settings.REDIS_URL)
dp = Dispatcher(bot, storage=storage)

# Подключение middleware и фильтров
dp.middleware.setup(ThrottlingMiddleware())
dp.filters_factory.bind(IsAdminFilter)

# Регистрация роутеров
from routers import commands, callback_handlers, handlers

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
