from telethon import TelegramClient, events
import os
import asyncio

# Your API ID, hash and bot token from Telegram
api_id = int(os.environ.get("TELEGRAM_API_ID"))
api_hash = os.environ.get("TELEGRAM_API_HASH")
bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Bot started!')

async def main():
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())