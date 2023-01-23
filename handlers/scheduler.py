import asyncio

import aioschedule
from aiogram import types

from config import bot


async def schedule_command(message: types.Message):
    """
    Хендлер для того, чтбы получить команду от юзера и сохранить его id
    """
    global chat_id
    chat_id = message.from_user.id
    await message.answer("Хорошо")


async def notify():
    """
    напоминалка
    """
    await bot.send_message(
        chat_id=chat_id,
        text="Привет"
    )


async def scheduler():
    """
    Для того, чтобы по расписанию выполнять напоминалку
    """
    aioschedule.every(3).seconds.do(notify)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
