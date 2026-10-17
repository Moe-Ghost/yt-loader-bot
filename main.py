import os
import re
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

YOUTUBE_RE = re.compile(r"(?:youtube\.com/(?:watch\?(?:\S*?&)?v=|shorts/)|youtu\.be/)([A-Za-z0-9_-]{11})")

def extract_video_id(text: str)-> str | None:
    match = YOUTUBE_RE.search(text)
    return match.group(1) if match else None

@dp.message()
async def on_message(message: Message):
    video_id = extract_video_id(message.text or "")
    if not video_id:
        await message.answer("Send me a YouTube link")
        return
    await message.answer("Качаю...")
    url = f'https://www.youtube.com/watch?v={video_id}'
    path = await asyncio.to_thread(download, url)
    await message.answer_video(FSInputFile(path))

asyncio.run(dp.start_polling(bot))


