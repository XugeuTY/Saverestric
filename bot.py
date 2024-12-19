import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Start command
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Classplus (Org Code Required)", callback_data='classplus')],
        [InlineKeyboardButton("Awadh Ojha App (Nothing Required)", callback_data='awadh')],
        [InlineKeyboardButton("Khan Sir (Nothing Required)", callback_data='khansir')],
        [InlineKeyboardButton("ICS Coaching (Any Random Login)", callback_data='ics')],
        [InlineKeyboardButton("🔙 Back", callback_data='back'), InlineKeyboardButton("❌ Close", callback_data='close')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Choose an option:', reply_markup=reply_markup)

# Handle button clicks
async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'close':
        await query.edit_message_text(text="Bot Closed!")
    elif data == 'back':
        await start(update, context)  # Restart
    else:
        await query.edit_message_text(text=f"You clicked: {data}")

# Main function
async def main():
    # Get bot token from environment variable
    bot_token = os.getenv("TELEGRAM_TOKEN")
    if not bot_token:
        print("Error: The 'TELEGRAM_TOKEN' environment variable is missing.")
        return

    # Create Application
    application = Application.builder().token(bot_token).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Start polling
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    # Run the main async function
    asyncio.run(main())  # This is the correct way to start it
