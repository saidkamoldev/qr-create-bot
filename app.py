import logging
import qrcode
from PIL import Image
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import logging
import os
import django
from django.core.management import call_command

from aiogram import executor

# from functions.check_balance import check_and_notify
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from colorama import init
init()
from colorama import Fore, Back, Style


# Telegram bot tokenini o'zgartiring
TOKEN = '6497324812:AAHLokg8EYlLzbE6l9ZY6tgowTZ-NLhDrdc'

# Botni yaratamiz
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# /start buyrug'i
@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer("Assalomu alaykum! QR kod yaratish uchun URLni yuboring.")

async def start_keyboard(status) -> InlineKeyboardMarkup:
    try:
        if not status:
            markup = InlineKeyboardMarkup()

            uz = InlineKeyboardButton(text=_("Hoziroq boshlash"), callback_data="Uzbek")
            markup.add(uz)
            return markup
        else:
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            offer = KeyboardButton(text=_("🚘 Avto mashina"))
            settings = KeyboardButton(text=_("⚙️ Kompaniyamiz haqida"))
        #     filials = KeyboardButton(text=_("Реферальная система "))
            support = KeyboardButton(text=_("☎️ Biz bilan aloqa"))
            # finaly = KeyboardButton(text=_("☎️ Обратная связь"))
            markup.row(offer, settings)

            markup.add(support)
            return markup
    except:
        print("error")


# Foydalanuvchidan URL olish
@dp.message_handler()
async def on_receive_url(message: types.Message):
    url = message.text

    # QR kodni yaratish
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="red", back_color="black")

    # QR kodni faylga saqlash
    qr_image.save("qr_code.png")

    # QR kodni yuborish
    with open("qr_code.png", "rb") as qr_file:
        await message.reply_photo(qr_file)

    await on_start(message)

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)

# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
# from aiogram.types import ParseMode
# import qrcode


# # Telegram bot tokenini o'zgartiring
# TOKEN = '6608772847:AAFKFIOccbr_XViuWeOAkUH-EXO_U91l-p8'

# # Botni yaratamiz
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)
# dp.middleware.setup(LoggingMiddleware())

# # /start buyrug'i
# @dp.message_handler(commands=['start'])
# async def on_start(message: types.Message):
#     await message.answer("Assalomu alaykum! QR kod yaratish uchun /generate buyrug'ini yuboring.")

# # /generate buyrug'i
# @dp.message_handler(lambda message: message.text.startswith('/generate '))
# async def on_generate_url(message: types.Message):
#     url = message.text.replace('/generate ', '')  # Foydalanuvchidan URL olish
#     if url:
#         qr = qrcode.QRCode(
#             version=1,
#             error_correction=qrcode.constants.ERROR_CORRECT_L,
#             box_size=10,
#             border=4,
#         )
#         qr.add_data(url)
#         qr.make(fit=True)
#         qr_image = qr.make_image(fill_color="black", back_color="white")

#         # QR kod rasmini yuborish
#         with open("qr_code.png", "wb") as qr_file:
#             qr_image.save(qr_file)
#         with open("qr_code.png", "rb") as qr_file:
#             await message.reply_photo(qr_file)
#     else:
#         await message.reply("Iltimos, valid URL kiriting.")


# if __name__ == "__main__":
#     from aiogram import executor
#     executor.start_polling(dp, skip_updates=True)







# import tkinter as tk
# import qrcode
# import aiogram
# from PIL import Image, ImageTk
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

# # Telegram bot tokenini o'zgartiring
# TOKEN = '6608772847:AAFKFIOccbr_XViuWeOAkUH-EXO_U91l-p8'

# def start(update: Update, context: CallbackContext):
#     update.message.reply_text("Assalomu alaykum! QR kod yaratish uchun /generate buyrug'ini yuboring.")

# def generate_qr_code(update: Update, context: CallbackContext):
#     url = update.message.text.replace('/generate ', '')  # Foydalanuvchidan URL olish
#     if url:
#         qr = qrcode.QRCode(
#             version=1,
#             error_correction=qrcode.constants.ERROR_CORRECT_L,
#             box_size=10,
#             border=4,
#         )
#         qr.add_data(url)
#         qr.make(fit=True)
#         qr_image = qr.make_image(fill_color="black", back_color="white")

#         # Convert the QR code image to a format compatible with Telegram
#         qr_image.save("qr_code.png")  # Rasmni saqlash
#         update.message.reply_photo(photo=open("qr_code.png", "rb"))
#     else:
#         update.message.reply_text("Iltimos, valid URL kiriting.")

# def main():
#     updater = Updater(TOKEN=TOKEN, use_context=True)
#     dispatcher = updater.dispatcher

#     # Botga /start buyrug'ini qo'shamiz
#     dispatcher.add_handler(CommandHandler("start", start))
#     # Botga /generate buyrug'ini qo'shamiz
#     dispatcher.add_handler(CommandHandler("generate", generate_qr_code))
#     # Botni ishga tushuramiz
#     updater.start_polling()
#     updater.idle()

# if __name__ == "__main__":
#     main()


# import tkinter as tk
# import qrcode
# from PIL import Image, ImageTk
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
# from telegram import Filters
# from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters


# # Telegram bot tokenini o'zgartiring
# TOKEN = '6608772847:AAFKFIOccbr_XViuWeOAkUH-EXO_U91l-p8'

# def start(update: Update, context: CallbackContext):
#     update.message.reply_text("Assalomu alaykum! QR kod yaratish uchun /generate buyrug'ini yuboring.")

# def generate_qr_code(update: Update, context: CallbackContext):
#     url = update.message.text.replace('/generate ', '')  # Foydalanuvchidan URL olish
#     if url:
#         qr = qrcode.QRCode(
#             version=1,
#             error_correction=qrcode.constants.ERROR_CORRECT_L,
#             box_size=10,
#             border=4,
#         )
#         qr.add_data(url)
#         qr.make(fit=True)
#         qr_image = qr.make_image(fill_color="black", back_color="white")

#         # Convert the QR code image to a format compatible with Telegram
#         qr_image.save("qr_code.png")  # Rasmni saqlash
#         update.message.reply_photo(photo=open("qr_code.png", "rb"))
#     else:
#         update.message.reply_text("Iltimos, valid URL kiriting.")

# def main():
#     updater = Updater(token=TOKEN, use_context=True)
#     dispatcher = updater.dispatcher

#     # Botga /start buyrug'ini qo'shamiz
#     dispatcher.add_handler(CommandHandler("start", start))
#     # Botga /generate buyrug'ini qo'shamiz
#     dispatcher.add_handler(CommandHandler("generate", generate_qr_code))
#     # Botni ishga tushuramiz
#     updater.start_polling()
#     updater.idle()

# if __name__ == "__main__":
#     main()
