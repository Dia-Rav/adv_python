from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import yandex_images_download
from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
from aiohttp import ClientSession
import socket


Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)

secret_token = '2020198962:AAGv-nDRd6FRKmEj_2ALWGPCEaWMGPngMXw'  # строка вида: 123456789:ABCDEFGHJABCDEFGHJABCDEFGHJABCDEFGHJ

bot = Bot(token=secret_token)
dp = Dispatcher(bot)

async def on_startup(_):
    print ('я что-то делаю')

async def fetch_ip(service, session):
    async with session.get(service.url) as resp:
        json = await resp.json()
        return json[service.ip_attr]
    # получение ip


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm Koyash!\nPowered by aiogram.")


@dp.message_handler(commands='ip')
async def get_text_messages(messege: types.Message):
    async with ClientSession() as session:
        tasks = [asyncio.create_task(fetch_ip(service, session))
                 for service in SERVICES]
        done, pending = await asyncio.wait(tasks, timeout=None,
                                           return_when=FIRST_COMPLETED)

    for i in done:      
        await messege.reply(i)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup = on_startup)


