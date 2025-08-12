import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Load .env file
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise RuntimeError("Set TELEGRAM_TOKEN in .env file")

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is alive! Use /setkeyword <keyword> to set your keyword.")

# Command: /setkeyword
async def set_keyword(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠ Please provide a keyword. Example: /setkeyword Python")
        return
    keyword = " ".join(context.args)
    await update.message.reply_text(f"✅ Keyword set to: {keyword}")

# Fallback: reply to ANY message
async def echo_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"📩 I got your message: {update.message.text}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("setkeyword", set_keyword))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_all))

print("Bot is running...")
app.run_polling()
