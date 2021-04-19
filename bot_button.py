from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_hello(message: types.Message):
      await bot.send_message(message.from_user.id, 'Привет\nЧто будем делать?',
                             reply_markup=kb.greet_kb)

@dp.message_handler(commands=['but'])
async def process_help(message: types.Message):
      await bot.send_message(message.from_user.id, 'Дополнительные кнопки', reply_markup=kb.markup3)

@dp.message_handler(commands=['hi'])
async def process_help(message: types.Message):
      await bot.send_message(message.from_user.id, 'Наши кнопки', reply_markup=kb.markup_requests)

@dp.message_handler(commands=['help'])
async def process_help(message: types.Message):
      await bot.send_message(message.from_user.id, 'Нужна помощь?')

@dp.message_handler()
async def process_reply(message: types.Message):
      await message.reply('Ваш текст сообщения!!!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)