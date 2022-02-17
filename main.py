from aiogram import Bot, Dispatcher, executor, types
import pyqrcode
import sqlite3

bot = Bot(token='5127273389:AAG65RT7dwceCun9MCJgGuXsVk8084fPT7I')
dp = Dispatcher(bot)

name = ''

@dp.message_handler(commands=['reg'])
async def register(message: types.Message):
    await message.answer('What is your name?')
    name = message.text
    db = sqlite3.connect('server.db')
    cursor = db.cursor()
    cursor.execute("INSERT INTO 'some_info' ('name') VALUES (?)", (name,))
    db.commit()
    name.reply('Thank you!')


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello, how can I help you?")


@dp.message_handler(commands=['picture'])
async def logo(message: types.Message):
    await message.answer_photo("https://wallpaperaccess.com/full/664980.jpg")


@dp.message_handler(commands=['qr'])
async def qr(message):
    message.text = input('введи текст')
    text = pyqrcode.create(message.text)
    text.png('code.png', scale=5)
    await bot.send_photo(chat_id=message.chat.id, photo=open('code.png', 'rb'))


@dp.message_handler()
async def logo(message: types.Message):
    await message.answer(message.text)


executor.start_polling(dp)
