import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext

# Temporary configuration - REMOVE THIS BEFORE SHARING CODE
TEMPORARY_TESTING_TOKEN = "7544944442:AAHpTW0HNRYyFUOIK8ahTviuF5FV-eNRVE8"  # <<< REVOKE THIS LATER
CHANNEL_USERNAME = "@your_test_channel"  # Change these for testing
GROUP_USERNAME = "@your_test_group"
TWITTER_USERNAME = "@your_test_twitter"

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url=f"t.me/{CHANNEL_USERNAME[1:]}")],
        [InlineKeyboardButton("👥 Join Group", url=f"t.me/{GROUP_USERNAME[1:]}")],
        [InlineKeyboardButton("🐦 Follow Twitter", url=f"twitter.com/{TWITTER_USERNAME[1:]}")],
        [InlineKeyboardButton("✅ I've joined all", callback_data='joined')]
    ]
    
    update.message.reply_text(
        f"👋 Welcome {user.first_name}!\n\n"
        "To get your 10 SOL test airdrop:\n"
        "1. Join our channel\n"
        "2. Join our group\n"
        "3. Follow our Twitter\n"
        "4. Submit your SOL wallet\n\n"
        "Click below then tap '✅ I've joined all':",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ... [rest of the code remains the same as previous example] ...

if __name__ == '__main__':
    print("⚠️ WARNING: Using temporary testing token - REVOKE THIS IN @BotFather AFTER TESTING ⚠️")
    main()
