from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# Введите токен телеграмм бота
TOKEN = "ваш токен"  # Замените на ваш токен

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создание роутера
router = Router()
dp.include_router(router)

# Определение группы состояний
class UserStates(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Обработчик команды /start
@router.message(CommandStart())
async def message_handler(message: types.Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью. "
                         "Напиши Calories, чтобы начать подсчет калорий.")

# Обработчик для начала процесса подсчета калорий
@router.message(F.text.lower() == "calories")
async def set_age(message: types.Message, state: FSMContext):
    await message.answer("Введите свой возраст:")
    await state.set_state(UserStates.age)

# Обработчик для ввода роста
@router.message(UserStates.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост (в см):")
    await state.set_state(UserStates.growth)

# Обработчик для ввода веса
@router.message(UserStates.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес (в кг):")
    await state.set_state(UserStates.weight)

# Обработчик для подсчета и отправки результата
@router.message(UserStates.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    try:
        age = int(data['age'])
        growth = int(data['growth'])
        weight = float(data['weight'])

        # Формула Миффлина-Сан Жеора для мужчин
        calories = 10 * weight + 6.25 * growth - 5 * age + 5

        await message.answer(
            f"Ваша суточная норма калорий: {calories:.0f} ккал")
    except ValueError:
        await message.answer(
            "Ошибка в введенных данных. Пожалуйста, убедитесь, что вы ввели числовые значения.")

    # Финиширование машины состояний
    await state.clear()


# Обработчик любого сообщения
@router.message()
async def all_messages(message: types.Message):
    await message.answer(
        "Введите команду /start, чтобы начать общение, или напишите 'Calories' для подсчета калорий.")


# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())

