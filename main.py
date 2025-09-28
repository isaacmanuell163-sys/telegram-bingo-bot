import os
from telegram.ext import Updater, CommandHandler

# Token del bot (Render lo obtiene desde variable de entorno BOT_TOKEN)
BOT_TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    user = update.effective_user.first_name
    update.message.reply_text(f"👋 Hola {user}, tu bot ya está funcionando en Render 🚀")

if __name__ == "__main__":
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    print("🤖 Bot corriendo...")
    updater.start_polling()
    updater.idle()
