from aiogram import *
from aiogram.types import *

TOKEN = '6988144483:AAGjxtlLjWSE8fi1QwtAfD0O0sHwamrf788'
bot = Bot(TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
menu = KeyboardButton('SoundWord menu')
b1 = KeyboardButton('Товары')
b2 = KeyboardButton('Заказы')
b3 = KeyboardButton('Помощь')
b4 = KeyboardButton('/description')
kb.add(menu).add(b1).insert(b2).add(b3).insert(b4)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    caption = """Добро пожаловать на наш официальный бот <b>SoundWord!</b>🎵
Ниже в меню выберете что вам нужно⬇️:"""
    P1 = InputFile('image/image.psd.png')
    await bot.send_photo(message.chat.id, photo=P1, caption=caption, parse_mode='HTML', reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['description'])
async def description(message: types.Message):
    await message.answer(
        'Это официальный бот SoundWord. Через него вы можете делать привычные покупки как и на нашем сайте.')
    await message.delete()


@dp.message_handler()
async def swnemu(message: types.Message):
    if 'SoundWord menu' in message.text:
        await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp)
