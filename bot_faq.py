import json
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Caminho do arquivo JSON
FAQ_PATH = r"C:\Users\2591081\Documents\Bot\CORRETO\faq.json"

# Carrega o conteúdo do JSON corrigido (lista de objetos)
with open(FAQ_PATH, "r", encoding="utf-8") as f:
    faq_data = json.load(f)

# Extrai perguntas e respostas
perguntas = [item["pergunta"] for item in faq_data]
respostas = [item["resposta"] for item in faq_data]

# Vetoriza as perguntas
vectorizer = TfidfVectorizer()
perguntas_tfidf = vectorizer.fit_transform(perguntas)

# Função para buscar a resposta
def encontrar_resposta(mensagem):
    mensagem_tfidf = vectorizer.transform([mensagem])
    similaridades = cosine_similarity(mensagem_tfidf, perguntas_tfidf)
    indice_max = similaridades.argmax()
    score = similaridades[0, indice_max]

    if score > 0.4:
        return respostas[indice_max]
    else:
        hora_atual = datetime.now().hour
        if hora_atual >= 17:
            return (
                "Olá!\n"
                "Sou um assistente virtual e não consegui compreender sua mensagem.\n"
                "Por favor, envie sua dúvida de forma direta, sem saudações como 'olá' ou 'bom dia', "
                "para que eu possa ajudar da melhor maneira possível.\n\n"
                "Se precisar de mais informações ou tiver outras dúvidas, entre em contato pelos nossos canais de atendimento:\n"
                "📞 (61) 3318-2941\n"
                "✉ censodf@edu.se.df.gov.br\n\n"
                "Estamos à disposição para ajudar!"
            )
        else:
            return None  # Antes das 17h, não responde nada

# Função para tratar mensagens
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.strip()
    resposta = encontrar_resposta(texto)

    if resposta:  # Só responde se houver resposta
        await update.message.reply_text(resposta)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Envie sua pergunta e eu tentarei ajudar com base no nosso FAQ.")

# Executar o bot
if __name__ == "__main__":
    # Substitua pelo seu token real
    TOKEN = "7915459145:AAEMrtA88toc58N5fcx_LQWK_K5kTi9RHMU"

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    print("🤖 Bot iniciado...")
    app.run_polling()
