import asyncio
import os
from aiogram import Bot, Dispatcher, types
from google import genai
from aiohttp import web

# 1. TOKENLAR
TELEGRAM_TOKEN = "8857220596:AAFGPn651vKdDLHovx1xi-1ENztgMVgeA5c"
GEMINI_API_KEY = "AIzaSyASywyQvlNncxWZHmDgGp9a4B6xYbuCcSI"

# 2. GEMINI MIJOZI
client = genai.Client(api_key=GEMINI_API_KEY)
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
    print("Bot muvaffaqiyatli ishga tushdi va xabarlarni kutmoqda...")
    await dp.start_polling(bot)

# Render port so'rashini aldash uchun veb-server (soxta sahifa)
    import os
    from aiohttp import web
    
    async def handle(request):
        return web.Response(text="Bot is running smoothly!")
        
    app = web.Application()
    app.router.add_get('/', handle)
    
    runner = web.AppRunner(app)
    await runner.setup()
    
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    
    # Botingiz xabarlarni qabul qilishi uchun asosiy qism
    await dp.start_polling(bot)

# Render port so'rashini aldash uchun veb-server (soxta sahifa)
    import os
    from aiohttp import web
    
    async def handle(request):
        return web.Response(text="Bot is running smoothly!")
        
    app = web.Application()
    app.router.add_get('/', handle)
    
    runner = web.AppRunner(app)
    await runner.setup()
    
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    
    # Botingiz xabarlarni qabul qilishi uchun asosiy qism
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    
    
