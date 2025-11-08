from telegram.ext import Application, MessageHandler, filters

TELEGRAM_TOKEN = "********"  # Your API Key here

# Réponses pré-définies en anglais
RESPONSES = {
    "hello": "👋 Hello! I'm Uni-Pal, your hackathon assistant!",
    "hi": "👋 Hi! How can I help you with the hackathon?",
    "deadline": "📅 Submission deadline: October 28, 2025",
    "workshop": "🏫 Workshop: Wednesday October 22, 7-9 PM at University of Jordan (Uruk)",
    "prizes": "🏆 Prizes: Certificates, financial prizes, gifts for winning teams",
    "submit": "📹 Submit: 2-4 minute video + GitHub code link",
    "theme": "🤖 Theme: AI for university students or universities",
    "default": "ℹ️ I can help with: deadline, workshop, prizes, submit, theme"
}

async def handle_message(update, context):
    user_message = update.message.text.lower()
    print(f" Message: {user_message}")
    
    # Find the answer
    if "deadline" in user_message:
        reply = RESPONSES["deadline"]
    elif "workshop" in user_message:
        reply = RESPONSES["workshop"]
    elif "prize" in user_message:
        reply = RESPONSES["prizes"]
    elif "submit" in user_message:
        reply = RESPONSES["submit"]
    elif "theme" in user_message:
        reply = RESPONSES["theme"]
    elif "hello" in user_message or "hi" in user_message:
        reply = RESPONSES["hello"]
    else:
        reply = RESPONSES["default"]
    
    await update.message.reply_text(reply)
    print(f" Réponse: {reply}")

def main():
    print(" Starting Uni-Pal Simple Bot...")
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print(" Bot started successfully! Waiting for messages...")
    application.run_polling()

if __name__ == "__main__":

    main()


