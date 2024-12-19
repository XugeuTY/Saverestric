import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Start command
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Classplus (Org Code Required)", callback_data='classplus')],
        [InlineKeyboardButton("Awadh Ojha App (Nothing Required)", callback_data='awadh')],
        [InlineKeyboardButton("Khan Sir (Nothing Required)", callback_data='khansir')],
        [InlineKeyboardButton("ICS Coaching (Any Random Login)", callback_data='ics')],
        [InlineKeyboardButton("🔙 Back", callback_data='back'), InlineKeyboardButton("❌ Close", callback_data='close')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Choose an option:', reply_markup=reply_markup)

# Handle button clicks
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    data = query.data

    if data == 'close':
        query.edit_message_text(text="Bot Closed!")
    elif data == 'back':
        start(update, context)  # Restart
    else:
        query.edit_message_text(text=f"You clicked: {data}")

# Main function
def main():
    # Get bot token from environment variable
    bot_token = os.getenv("TELEGRAM_TOKEN")
    if not bot_token:
        print("Error: The 'TELEGRAM_TOKEN' environment variable is missing.")
        return

    # Create Updater and Dispatcher
    updater = Updater(bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # Add handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    # Start polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
