import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context):
    logger.info("Start function triggered")
    keyboard = [
        [InlineKeyboardButton("Classplus (Org Code Required)", callback_data='classplus')],
        [InlineKeyboardButton("Awadh Ojha App (Nothing Required)", callback_data='awadh')],
        [InlineKeyboardButton("Khan Sir (Nothing Required)", callback_data='khansir')],
        [InlineKeyboardButton("ICS Coaching (Any Random Login)", callback_data='ics')],
        [InlineKeyboardButton("🔙 Back", callback_data='back'), InlineKeyboardButton("❌ Close", callback_data='close')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Choose an option:', reply_markup=reply_markup)
    logger.info("Message sent to user")

def button(update: Update, context):
    query = update.callback_query
    query.answer()
    data = query.data

    logger.info(f"Button clicked: {data}")

    if data == 'close':
        query.edit_message_text(text="Bot Closed!")
    elif data == 'back':
        start(update, context)
    else:
        query.edit_message_text(text=f"You clicked: {data}")

def main():
    bot_token = os.getenv("TELEGRAM_TOKEN")
    if not bot_token:
        print("Error: The 'TELEGRAM_TOKEN' environment variable is missing.")
        return

    updater = Updater(bot_token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
