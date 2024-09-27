from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = ''  # получили в ТГ от BotFather
bot = Bot(token=api)  # переменная бота - она будет хранить объект бота, 'token' будет равен вписанному ключу в 'api'
dp = Dispatcher(bot, storage=MemoryStorage())  # создадим объект 'Dispatcher' и наш объект бота в качестве аргумента


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)  # запуск бота
