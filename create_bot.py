import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from asyncpg_lite import DatabaseManager
from decouple import config
from openai import OpenAI

local_client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

# получаем список администраторов из .env
admins = [int(admin_id) for admin_id in config('ADMINS').split(',')]

# инициализируем логирование и выводим в переменную для отдельного использования в нужных местах
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# инициализируем объект, который будет отвечать за взаимодействие с базой данных
db_manager = DatabaseManager(db_url=config('PG_LINK'), deletion_password=config('ROOT_PASS'))

# инициализируем объект бота, передавая ему parse_mode=ParseMode.HTML по умолчанию
bot = Bot(token=config('BOT_API_KEY'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

# инициализируем объект бота
dp = Dispatcher()