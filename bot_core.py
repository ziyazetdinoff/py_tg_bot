import asyncio
import telegram


async def start():
    bot = telegram.Bot("TOKEN")
    async with bot:
        print(await bot.get_me())