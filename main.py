import asyncio

from aiogram import executor
from aiogram.dispatcher.filters import Text

from config import dp
from handlers.scheduler import schedule_command, scheduler


async def startup(_):
    """
    запускаем дополнительные сторонние сервисы(БД, напоминалки и тд)
    """
    # отправляет нашу асинхронную напоминалку в бекраунд,
    # в общий список асинхронных задач
    asyncio.create_task(scheduler())


if __name__ == "__main__":
    dp.register_message_handler(schedule_command, Text(equals="напомни"))

    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=startup
    )
