import asyncio
import os
from aiogram import Bot, Dispatcher, types
from google import genai
from aiohttp import web

# 1. TOKENLAR
TELEGRAM_TOKEN = "8857220516:AAFGPn651vKdDLHovx1xi-1ENztgMVgeA5c"
GEMINI_API_KEY = "AIzaSyAsywyQvlNncxWZHmDgGp9a4B6xyBuCcSI"

# 2. GEMINI MIJOZI VA BOT INIZALIZATSIYASI
client = genai.Client(api_key=GEMINI_API_KEY)
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

# Render serveri botni "uyg'oq" saqlashi uchun kerakli qism
async def handle(request):
    return web.Response(text="Bot is running!")

# Asosiy ishga tushirish funksiyasi
async def main():
    # Veb serverni birinchi bo'lib to'liq yurgizamiz (Render portni topishi uchun)
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    
    port = int(os.environ.get('PORT', 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"Bot serverda {port}-portda ishga tushdi...")
    
    # Keyin esa botni polling rejimida ishga tushiramiz
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
