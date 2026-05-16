import asyncio
import os
from aiogram import Bot, Dispatcher, types
from google import genai
from aiohttp import web

# 1. TOKENLAR
TELEGRAM_TOKEN = "8857220596:AAExYxcrW4iB-gmlmHcp4d3dlz3R63tv_YM"
GEMINI_API_KEY = "AIzaSyChNvtSYZ5bqWp2lhEbf71k7AFy0hnDIlg"

# 2. GEMINI MIJOZI
client = genai.Client())
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message()
async def talk_with_ai(message: types.Message):
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=message.text
        )
        await message.answer(response.text)
    except Exception as e:
        print(f"Xato yuz berdi: {e}")
        await message.answer("Biroz kuting, limit tugadi yoki aloqa uzildi.")

# Render serveri botni "uyg'oq" saqlashi uchun kerakli qism
async def handle(request):
    return web.Response(text="Bot is running!")

async def main():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    # Server portini sozlash
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    
    print(f"Bot serverda {port}-portda ishga tushdi...")
    asyncio.create_task(site.start())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
