import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import Message, FSInputFile

from downloader import download

load_dotenv()
bot = Bot(os.environ["BOT_TOKEN"])
dp = Dispatcher()
# @dp.message()
# async def echo(message: Message):
#     await message.answer(message.text or "Send me text")

@dp.message()
async def on_message(message: Message):
    await message.answer("Качаю...")
    path = download(message.text)
    await message.answer_video(FSInputFile(path))

asyncio.run(dp.start_polling(bot))


