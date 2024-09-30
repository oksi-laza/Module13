from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = ''  # получили в ТГ от BotFather
bot = Bot(token=api)  # переменная бота - она будет хранить объект бота, 'token' будет равен вписанному ключу в 'api'
dp = Dispatcher(bot, storage=MemoryStorage())  # создадим объект 'Dispatcher' и наш объект бота в качестве аргумента


class UserState(StatesGroup):
    """age: возраст, growth: рост, weight: вес"""
    age = State()
    growth = State()
    weight = State()


# Создали клавиатуру в переменной 'kb', создали и добавили две кнопки в одной строке,
# указали параметр для подстраивания клавиатуры под размеры интерфейса устройства
kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')]],
                         resize_keyboard=True)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)  # добавили параметр reply_markup


@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()    # ожидаем ввода возраста в атрибут 'UserState.age'


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)    # эта функция обновляет данные в состоянии age на message.text
    await message.answer('Введите свой рост:')
    await UserState.growth.set()    # ожидаем ввода роста в атрибут 'UserState.growth'


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)    # эта функция обновляет данные в состоянии growth на message.text
    await message.answer('Введите свой вес:')
    await UserState.weight.set()    # ожидаем ввода веса в атрибут 'UserState.weight'


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)    # эта функция обновляет данные в состоянии weight на message.text
    data = await state.get_data()    # запомнили в переменную data все ранее введённые состояния
    # calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161    # для женщин
    calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5    # для мужчин
    await message.answer(f'Ваша норма калорий {calories} в сутки')
    await state.finish()    # финишировали машину состояний


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)  # запуск бота
