import asyncio
import os
from aiogram import Bot, Dispatcher, types
from google import genai
from aiohttp import web

# 1. TOKENLAR
TELEGRAM_TOKEN = "8851213930:AAESw7UESMY7L_U_kO4LVQL16B0azG_xG2g"
GEMINI_API_KEY = "AIzaSyAsywyQvlNncxWZHmDgGp9a4B6xyBuCcSI"

# 2. INIZALIZATSIYA
client = genai.Client(api_key=GEMINI_API_KEY)
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

# Render uchun veb-server handle funksiyasi
async def handle(request):
    return web.Response(text="AI Content Maker is running perfectly!")

# AI Kontent yaratish qismi
@dp.message()
async def generate_content(message: types.Message):
    kutish_xabari = await message.answer("🔄 Daxshatli zo'r kontent tayyorlanyapti, iltimos kuting...")
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Sen daxshatli zo'r kontent meykarsan. Quyidagi mavzuda ijtimoiy tarmoqlar uchun jozibali, qiziqarli va sifatli kontent, post yoki matn tayyorlab ber: {message.text}"
        )
        await kutish_xabari.delete()
        await message.answer(response.text)
    except Exception as e:
        await kutish_xabari.edit_text("❌ Kontent yaratishda xatolik yuz berdi. Keyinroq urinib ko'ring.")

# Renderda parallel ishlashni ta'minlovchi funksiya
async def on_startup():
    asyncio.create_task(dp.start_polling(bot))

async def main():
    app = web.Application()
    app.router.add_get('/', handle)
    
    # Botni polling rejimida fonda ishga tushiramiz
    await on_startup()
    
    # Veb-serverni asosiy oqimda yuritamiz (Render portni ko'rishi uchun)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get('PORT', 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    
    # Server doimiy ishlab turishi uchun cheksiz sikl
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
