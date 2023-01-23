import logging
from os import getenv

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv


logger = logging.basicConfig(level=logging.INFO)
load_dotenv()
bot = Bot(getenv('BOT_TOKEN'))
dp = Dispatcher(bot)
