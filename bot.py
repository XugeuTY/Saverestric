from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Start command
def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Classplus (Org Code Required)", callback_data='classplus')],
        [InlineKeyboardButton("Awadh Ojha App (Nothing Required)", callback_data='awadh')],
        [InlineKeyboardButton("Khan Sir (Nothing Required)", callback_data='khansir')],
        [InlineKeyboardButton("ICS Coaching (Any Random Login)", callback_data='ics')],
        # Add more buttons as per your requirement
        [InlineKeyboardButton("🔙 Back", callback_data='back'), InlineKeyboardButton("❌ Close", callback_data='close')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Choose an option:', reply_markup=reply_markup)

# Handle button clicks
def button(update: Update, context):
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
    # Replace 'YOUR_BOT_TOKEN' with your BotFather token
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    # Start polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
