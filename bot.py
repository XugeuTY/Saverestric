from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Your bot token
TOKEN = "7324404875:AAHP2emM_PcwSL7dZnJ0iZ_I1M6QSRjrLxs"

# Function to handle the '/start' command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Create the keyboard with buttons
    keyboard = [
        [InlineKeyboardButton("APPX ALL API", callback_data="appx_all_api")],
        [InlineKeyboardButton("ABHINAV MATHS", callback_data="abhinav_maths")],
        [InlineKeyboardButton("ADDA 247", callback_data="adda_247")],
        [InlineKeyboardButton("CDS JOURNEY", callback_data="cds_journey")],
        [InlineKeyboardButton("CLASSPLUS", callback_data="classplus")],
        [InlineKeyboardButton("AWADH OJHA APP", callback_data="awadh_ojha")],
        [InlineKeyboardButton("KHAN SIR", callback_data="khan_sir")],
        [InlineKeyboardButton("ICS COACHING", callback_data="ics_coaching")],
        [InlineKeyboardButton("IFAS ACADEMY", callback_data="ifas_academy")],
        [InlineKeyboardButton("JRF ADDA", callback_data="jrf_adda")],
        [InlineKeyboardButton("MY PATHSALA", callback_data="my_pathsala")],
        [InlineKeyboardButton("PHYSICS WALLAH", callback_data="physics_wallah")],
        [InlineKeyboardButton("SSC CGL PINNACLE", callback_data="ssc_cgl_pinnacle")],
        [InlineKeyboardButton("QUALITY EDUCATION", callback_data="quality_education")],
        [InlineKeyboardButton("STUDY IQ", callback_data="study_iq")],
        [InlineKeyboardButton("TEST PAPER", callback_data="test_paper")],
        [InlineKeyboardButton("VERBAL MATH", callback_data="verbal_math")],
        [InlineKeyboardButton("UTKARSH CLASSES", callback_data="utkarsh_classes")]
    ]
    
    # Create the inline keyboard markup
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send a message with the keyboard
    await update.message.reply_text('Choose an option:', reply_markup=reply_markup)

# Function to handle button presses
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # Acknowledge the button press
    
    # Handle each button press
    if query.data == "appx_all_api":
        await query.edit_message_text(text="You selected APPX ALL API")
    elif query.data == "abhinav_maths":
        await query.edit_message_text(text="You selected ABHINAV MATHS")
    elif query.data == "adda_247":
        await query.edit_message_text(text="You selected ADDA 247")
    elif query.data == "cds_journey":
        await query.edit_message_text(text="You selected CDS JOURNEY")
    elif query.data == "classplus":
        await query.edit_message_text(text="You selected CLASSPLUS. Please enter the Org Code.")
    elif query.data == "awadh_ojha":
        await query.edit_message_text(text="You selected AWADH OJHA APP")
    elif query.data == "khan_sir":
        await query.edit_message_text(text="You selected KHAN SIR")
    elif query.data == "ics_coaching":
        await query.edit_message_text(text="You selected ICS COACHING. Please enter the login details.")
    elif query.data == "ifas_academy":
        await query.edit_message_text(text="You selected IFAS ACADEMY. Please enter the login details.")
    elif query.data == "jrf_adda":
        await query.edit_message_text(text="You selected JRF ADDA")
    elif query.data == "my_pathsala":
        await query.edit_message_text(text="You selected MY PATHSALA")
    elif query.data == "physics_wallah":
        await query.edit_message_text(text="You selected PHYSICS WALLAH. Please enter the token.")
    elif query.data == "ssc_cgl_pinnacle":
        await query.edit_message_text(text="You selected SSC CGL PINNACLE")
    elif query.data == "quality_education":
        await query.edit_message_text(text="You selected QUALITY EDUCATION")
    elif query.data == "study_iq":
        await query.edit_message_text(text="You selected STUDY IQ")
    elif query.data == "test_paper":
        await query.edit_message_text(text="You selected TEST PAPER")
    elif query.data == "verbal_math":
        await query.edit_message_text(text="You selected VERBAL MATH")
    elif query.data == "utkarsh_classes":
        await query.edit_message_text(text="You selected UTKARSH CLASSES")

# Main function to run the bot
def main():
    # Create the Application instance
    application = Application.builder().token(TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    
    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
