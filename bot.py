from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Classplus (Org Code Required)", callback_data='classplus')],
        [InlineKeyboardButton("Awadh Ojha App (Nothing Required)", callback_data='awadh')],
        [InlineKeyboardButton("Khan Sir (Nothing Required)", callback_data='khansir')],
        [InlineKeyboardButton("ICS Coaching (Any Random Login)", callback_data='ics')],
        [InlineKeyboardButton("🔙 Back", callback_data='back'), InlineKeyboardButton("❌ Close", callback_data='close')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose an option:", reply_markup=reply_markup)

# Handle button clicks
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    import os
    bot_token = os.environ.get("7324404875:AAHP2emM_PcwSL7dZnJ0iZ_I1M6QSRjrLxs")
    if not bot_token:
        print("Error: TELEGRAM_BOT_TOKEN environment variable is not set.")
        return

    # Create the application
    application = Application.builder().token(bot_token).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Start the bot
    print("Bot is running...")
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
