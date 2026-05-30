import asyncio
from aiogram import Bot, Dispatcher, types
from google import genai

# TOKENLAR
TELEGRAM_TOKEN = "8754069714:AAFSFCLKu-HN7BIcT900GaRllbV3KjjQsBM"
GEMINI_API_KEY = "AIzaSyAsywyQvlNncxWZHmDgGp9a4B6xyBuCcSI"

# INIZALIZATSIYA
client = genai.Client(api_key=GEMINI_API_KEY)
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

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
        print(f"Xatolik yuz berdi: {e}")
        await kutish_xabari.edit_text("❌ Kontent yaratishda xatolik yuz berdi. Keyinroq urinib ko'ring.")

async def main():
    print("Bot muvaffaqiyatli ishga tushdi va xabarlarni kutyapti...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
