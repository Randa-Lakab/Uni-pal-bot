import os
from telegram.ext import Application, MessageHandler, filters
from openai import OpenAI

# Remplace avec TES clés API
TELEGRAM_TOKEN = "8396315351:AAHLRQtIHItHJx434NTsDKh1TubGxSxiXog"  
OPENAI_API_KEY = "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"   # 👈 Remplace par ta clé OpenAI

# Configure OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# Les informations du hackathon (ta "mémoire")
SYSTEM_PROMPT = """You are "Uni-Pal", a helpful Telegram assistant for participants of the Uni Agents 2025 hackathon.

IMPORTANT HACKATHON INFORMATION:
- Theme: Artificial Intelligence for university students or universities
- Final submission deadline: October 28, 2025
- What to submit: 2-4 minute demo video + complete code (GitHub link)
- Prizes: Certified participation certificates, financial prizes, gifts for winning teams
- Project ownership: The idea belongs to the participating team
- Workshop dates: Wednesday October 22, from 7-9 PM
- Workshop location: The University of Jordan - University Street (Uruk)

RULES:
1. Answer questions using ONLY the information above
2. If you don't know, say: "I'm sorry, I don't have that information right now."
3. Be friendly and encouraging!"""

async def handle_message(update, context):
    try:
        user_message = update.message.text
        print(f" Message reçu: {user_message}")
        
        # Appel à OpenAI (nouvelle syntaxe)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150
        )
        
        bot_reply = response.choices[0].message.content
        await update.message.reply_text(bot_reply)
        print(f"🤖 Réponse envoyée: {bot_reply}")
        
    except Exception as e:
        print(f" Erreur: {e}")
        await update.message.reply_text("Désolé, une erreur s'est produite.")

def main():
    print(" Démarrage du bot Uni-Pal...")
    
    # Crée l'application Telegram
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Ajoute le handler pour les messages texte
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print(" Bot démarré avec succès! En attente de messages...")
    
    # Lance le bot
    application.run_polling()

if __name__ == "__main__":
    main()