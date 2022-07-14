import os
from telegram import Update
from telegram.ext import *
import dotenv
import requests
import json

BASEDIR = os.path.abspath(os.path.dirname(__file__))
dotenv.read_dotenv(os.path.join(BASEDIR, os.pardir, '.env'))
BOTURL = os.environ.get("BASE_BOT_URL")
APPROVEDCOUNSELLORCHATID = []
print("Bot is waking up.")

def create_session(data) -> None:
    requests.post(BOTURL + 'create/', json = data)

async def join_session(session, thisChatId) -> None:
    if session["counsellorChatId"] == None:
        session["counsellorChatId"] = thisChatId
    else:
        session["clientChatId"] = thisChatId
    session["vacant"] = False
    requests.post(BOTURL + 'update/' + str(session["id"]), json = session)
    context.bot_data[clientChatId] = {"session_partner": counsellorChatId, "session": session}
    context.bot_data[counsellorChatId] = {"session_partner": clientChatId, "session": session}
    await context.bot.send_message(chat_id = clientChatId, text = "You are connected. Say hi!")
    await context.bot.send_message(chat_id = counsellorChatId, text = "You are connected. Say hi!")

async def start_command(update: Update, context: CallbackContext) -> int:
    thisChatId = update.effective_chat.id
    if thisChatId in APPROVEDCOUNSELLORCHATID:
        await update.message.reply_text("Please hold while we connect you to a client.")
        session = json.loads(requests.get(BOTURL + 'vacancy/client').text)
        await join_session(session, thisChatId) if session else create_session({"counsellorChatId": thisChatId})
    else:
        await update.message.reply_text(
            "Hi! Welcome to lifeline bot.\n"
            "Please hold while we connect you to a counseller.")
        session = json.loads(requests.get(BOTURL + 'vacancy/counsellor').text)
        await join_session(session, thisChatId) if session else create_session({"clientChatId": thisChatId})

    return 0

async def end_command(update: Update, context: CallbackContext) -> int:
    session = context.bot_data[update.effective_chat.id]["session"]
    session["ended"] = True
    requests.post(BOTURL + 'update/' + str(session["id"]), json = session)
    context.bot_data.pop(session['counsellorChatId']);
    context.bot_data.pop(session['clientChatId']);
    await context.bot.send_message(chat_id = session["clientChatId"], text='Goodbye')
    await context.bot.send_message(chat_id = session["counsellorChatId"], text='Goodbye')

    return ConversationHandler.END

async def echo_command(update: Update, context: CallbackContext) -> None:
    senderChatId = update.effective_chat.id
    receiverChatId = context.bot_data[senderChatId]["session_partner"]
    await context.bot.send_message(chat_id = context.bot_data[senderChatId]["session_partner"], text = update.message.text)

def error_handler(update: Update, context: CallbackContext):
    print(f"Update {update} caused an error {context.error}")

def main() -> None:
    application = Application.builder().token(os.environ.get("BOT_API_KEY")).build()

    conv_handler = ConversationHandler(
        entry_points = [CommandHandler("start", start_command)],
        states = {
        },
        fallbacks = [
            MessageHandler(filters.TEXT & ~filters.COMMAND, echo_command),
            CommandHandler("end", end_command)
        ],
    )

    application.add_handler(conv_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_command))
    application.add_error_handler(error_handler)
    application.run_polling(stop_signals=None)

if __name__ == "__main__":
    main()
