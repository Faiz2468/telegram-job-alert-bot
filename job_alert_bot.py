import os
import logging
from dotenv import load_dotenv
from telegram import Update, Bot
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# CONFIGURATION & LOGGING
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# BOT COMMAND HANDLERS
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message and list commands."""
    await update.message.reply_text(
        "👋 Hello! I’m your Job Alert Bot.\n\n"
        "Here are the available commands:\n"
        "/start - Welcome message\n"
        "/help - Show this help\n"
        "/setkeyword <keyword> - Set job search keyword\n"
        "/showkeyword - Show your current keyword"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """List available commands."""
    await update.message.reply_text(
        "/start - Welcome message\n"
        "/help - Show this help\n"
        "/setkeyword <keyword> - Set job search keyword\n"
        "/showkeyword - Show your current keyword"
    )

async def set_keyword(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Set a keyword for job alerts."""
    if not context.args:
        await update.message.reply_text("⚠ Please provide a keyword. Example: /setkeyword Python")
        return
    keyword = " ".join(context.args)
    context.user_data["keyword"] = keyword
    await update.message.reply_text(f"✅ Keyword set to: {keyword}")

async def show_keyword(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show the current keyword."""
    keyword = context.user_data.get("keyword")
    if keyword:
        await update.message.reply_text(f"📌 Current keyword: {keyword}")
    else:
        await update.message.reply_text("❌ No keyword set yet. Use /setkeyword <keyword>.")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle normal text messages."""
    await update.message.reply_text("💡 I only understand commands. Use /help to see options.")

# MAIN FUNCTION
def main():
    # Load environment variables
    load_dotenv()
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("Set TELEGRAM_TOKEN in .env file")

    # Check which bot we are running
    bot_info = Bot(token).get_me()
    print(f"🤖 Bot username: @{bot_info.username}")

    logger.info("python-telegram-bot version: %s", __import__("telegram").__version__)
    logger.info("Starting bot...")

    # Create bot application
    app = ApplicationBuilder().token(token).build()

    # Register commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("setkeyword", set_keyword))
    app.add_handler(CommandHandler("showkeyword", show_keyword))

    # Handle text messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    # Start bot
    app.run_polling()

if __name__ == "__main__":
    main()
