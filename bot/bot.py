import os
from telegram import Update
from telegram.ext import *
import dotenv
import requests

BASEDIR = os.path.abspath(os.path.dirname(__file__))
dotenv.read_dotenv(os.path.join(BASEDIR, os.pardir, '.env'))
BOTURL = os.environ.get("BASE_BOT_URL")
print("Bot is waking up.")

async def start_command(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        "Hi! Welcome to lifeline bot.\n"
        "Please hold while we connect you to a counseller.")
    return 1

async def end_command(update: Update, context: CallbackContext) -> int:
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Goodbye')
    return ConversationHandler.END

async def echo_command(update: Update, context: CallbackContext) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def error_handler(update: Update, context: CallbackContext):
    print(f"Update {update} caused an error {context.error}")

def main() -> None:
    application = Application.builder().token(os.environ.get("BOT_API_KEY")).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start_command)],
        states={
        },
        fallbacks=[CommandHandler("end", end_command)],
    )

    application.add_handler(conv_handler)
    application.run_polling(stop_signals=None)

if __name__ == "__main__":
    main()
