from aiogram import Bot, Dispatcher, executor, types
from setting import *
import test
import requests
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
token: str = token_bot
API = 'https://api.telegram.org/bot'
api_url_dog= 'https://random.dog/woof.json'
api_url_fox= 'https://randomfox.ca/floof/'
bot = Bot(token)
dp = Dispatcher(bot)
chat_id=560682705
id=0
#chat_id=442035403
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
button_cat: KeyboardButton = KeyboardButton('Picture of Fox')
button_dog: KeyboardButton = KeyboardButton('Picture of Dog')
button_credits: KeyboardButton = KeyboardButton('Credits')

keyboard.add(button_cat, button_dog,button_credits)
def return_chat_id():
    return id
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    id= message.from_user.id
    await message.answer(f'Какую картинку хотите получить?', reply_markup=keyboard)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer('Данный бот отправляет картинки с животными, нажмите кнопку с нужным животным!')


@dp.message_handler(text=['Picture of Fox'])
async def fox(message: types.Message):
    fox_response=requests.get(api_url_fox)
    fox_link = fox_response.json()["link"]
    if fox_response.status_code == 200:
        await requests.get(f'{API}{token}/sendPhoto?chat_id={chat_id}&photo={fox_link}')
    else:
        await message.answer('Error')


@dp.message_handler(text=['Picture of Dog'])
async def dog(message: types.Message):
    # dog_response=requests.get(api_url_dog)
    # if dog_response.status_code == 200:
    #     await message.answer(dog_response.text)
    # else:
    #     await message.answer('Error')
    dog_response = requests.get(api_url_dog)
    dog_link = dog_response.json()["url"]
    if dog_response.status_code == 200:
        await requests.get(f'{API}{token}/sendPhoto?chat_id={chat_id}&photo={dog_link}')
    else:
        await message.answer('Error')

@dp.message_handler(text=['Credits'])

async def credits(message: types.Message):
    await message.answer('hi,my name is daniil smirnov')






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)