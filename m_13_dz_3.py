from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart

# Введите токен телеграмм бота
TOKEN = "ваш токен"  # Замените на ваш токен

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создание роутера
router = Router()
dp.include_router(router)


# Обработчик команды /start
@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

# Обработчик любого сообщения
@router.message()
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())