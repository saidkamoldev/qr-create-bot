import psutil
from telegram.ext import Updater, CommandHandler

# Botning tokeni
TOKEN = 'BotningTokeni'

# Botni yaratamiz
updater = Updater(bot_token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# /mac buyrug'i uchun funksiya
def get_mac(update, context):
    interfaces = psutil.net_if_addrs()
    mac_addresses = {}

    for interface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == psutil.AF_LINK:
                mac_addresses[interface] = addr.address

    if mac_addresses:
        message = "Qurilma MAC manzillari:\n"
        for interface, mac in mac_addresses.items():
            message += f"{interface}: {mac}\n"
    else:
        message = "MAC manzillar topilmadi."

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# /mac buyrug'ini tanlab olish
mac_handler = CommandHandler('mac', get_mac)
dispatcher.add_handler(mac_handler)

# Botni ishga tushiramiz
updater.start_polling()
updater.idle()


# from telegram.ext import Updater, CommandHandler

# # Botning tokeni
# TOKEN = '6984738941:AAGKGDNcngaXH2akTOT54bApRHOZaSOUgoY'

# # Botni yaratamiz
# updater = Updater(token=TOKEN, use_context=True)
# dispatcher = updater.dispatcher

# # /start buyrug'i uchun funksiya
# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Salom! Bu Telegram bot misoli.")

# # /start buyrug'ini tanlab olis
# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)

# # Botni ishga tushiramiz
# updater.start_polling()
# updater.idle()