import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

from aimodel import vv


load_dotenv()
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer("Hello, Send me a voice message and I will convert it to text")


@dp.message(F.voice)
async def voice_handler(message: Message, bot: Bot) -> None:
    await bot.download(
        message.voice,
        destination="voice.ogg"
        )

    await message.reply(vv())


async def main() -> None:
    token = os.getenv("TELEGRAM_BOT")
    if not token:
        raise RuntimeError("Add TELEGRAM_BOT to your .env file")

    bot = Bot(token=token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
