from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode


# Введите токен телеграмм бота
TOKEN = "ваш токен"  # Замените на ваш токен

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создание роутера
router = Router()
dp.include_router(router)


# Определение группы состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Создание клавиатуры
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Рассчитать")],
        [KeyboardButton(text="Информация")]
    ],
    resize_keyboard=True  # Автоматическая подстройка под размер экрана
)


# Обработчик команды /start
@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "Привет! Я бот, помогающий твоему здоровью. Выберите действие:",
        reply_markup=keyboard,  # Используем созданную клавиатуру
        parse_mode=ParseMode.HTML
        # Можно использовать HTML для форматирования текста
    )


# Обработчик для начала процесса подсчета калорий
@router.message(F.text.lower() == "рассчитать")
async def set_age(message: types.Message, state: FSMContext):
    await message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)


# Обработчик для ввода роста
@router.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост (в см):")
    await state.set_state(UserState.growth)


# Обработчик для ввода веса
@router.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес (в кг):")
    await state.set_state(UserState.weight)


# Обработчик для подсчета и отправки результата
@router.message(UserState.weight)
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


# Обработчик для кнопки "Информация"
@router.message(F.text.lower() == 'информация')
async def info_handler(message: types.Message):
    await message.answer(
        "Я помогу вам рассчитать вашу суточную норму калорий. Нажмите 'Рассчитать', чтобы начать.")


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

