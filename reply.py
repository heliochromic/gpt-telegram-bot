import logging
import os

from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
from aiogram.utils import executor

import ai_engine

os.environ['TELEGRAM_API_TOKEN'] = '6218436341:AAFW8Zu-PZ2KNLypWJ1-4EQL3lBJix0h4Vc'
API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class CreateImg(StatesGroup):
    waiting_for_prompt = State()
    waiting_for_image = State()


@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    help_text = "/get_sticker - command to get a random sticker \n/create_img - command to generate an image based on a prompt.\nyou can also ask any question by putting a quesion mark at the end"
    await message.reply(help_text)


@dp.message_handler(commands=['create_img'])
async def cmd_create_img(message: types.Message):
    await message.reply("Enter the prompt")
    await CreateImg.waiting_for_prompt.set()
    # response = await bot.wait_for(types.Message, chat_id=message.chat.id)


@dp.message_handler(state=CreateImg.waiting_for_prompt)
async def process_prompt(message: Message, state: FSMContext):
    print("yeah")
    photo_url = ai_engine.generate_image(message.text)
    photo = types.InputFile.from_url(photo_url)
    await message.reply_photo(photo=photo)
    # Your code to create the image using the prompt goes here
    await state.finish()


@dp.message_handler()
async def qa(message: types.Message):
    question = message.text
    if question.endswith("?") or question.endswith("."):
        reply = ai_engine.handle_message(question)
        print(question)
        await message.reply(reply)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
