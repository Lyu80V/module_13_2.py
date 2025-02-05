from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

token = '720'
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    print('Введите команду /start, чтобы начать общение.')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)