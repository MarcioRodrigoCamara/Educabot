import time
from telegram import Update, constants
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from config import TOKEN, logger
from faq import GerenciadorFAQ
from ia import MotorIA

# Instâncias globais
faq_manager = GerenciadorFAQ()
motor_ia = MotorIA(faq_manager)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler para o comando /start."""
    user = update.effective_user
    logger.info(f"Usuário {user.id} iniciou o bot.")
    await update.message.reply_html(
        rf"Olá {user.mention_html()}! 👋"
        "\n\nEu sou o <b>EducaBot 4.0</b>, seu assistente virtual para o Educacenso da SEEDF."
        "\n\nComo posso ajudar você hoje? Pode me fazer qualquer pergunta sobre o censo escolar!"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler para o comando /help."""
    help_text = (
        "<b>Comandos disponíveis:</b>\n"
        "/start - Iniciar conversa\n"
        "/help - Ver esta ajuda\n"
        "/reload - Atualizar base de dados (Admin)\n\n"
        "Basta digitar sua dúvida e eu tentarei encontrar a melhor resposta no FAQ oficial."
    )
    await update.message.reply_html(help_text)

async def reload_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler para o comando /reload."""
    logger.info("Comando /reload recebido.")
    faq_manager.recarregar()
    motor_ia.recarregar()
    await update.message.reply_text("✅ Base de dados e motor de IA recarregados com sucesso!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler para mensagens de texto."""
    if not update.message or not update.message.text:
        return

    pergunta = update.message.text
    start_time = time.time()

    # Mostrar indicador de "digitando"
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id, 
        action=constants.ChatAction.TYPING
    )

    # Buscar resposta na IA
    resposta = motor_ia.buscar(pergunta)
    
    elapsed_time = time.time() - start_time
    logger.info(f"Pergunta: '{pergunta}' | Tempo: {elapsed_time:.2f}s")

    if resposta:
        await update.message.reply_text(resposta)
    else:
        await update.message.reply_text(
            "Desculpe, não encontrei uma resposta exata para sua pergunta no FAQ do Educacenso. "
            "Poderia tentar reformular ou entrar em contato com a coordenação?"
        )

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler global de erros."""
    logger.error(f"Erro no bot: {context.error}", exc_info=context.error)
    if isinstance(update, Update) and update.effective_message:
        await update.effective_message.reply_text(
            "Ops! Ocorreu um erro interno ao processar sua solicitação. Tente novamente mais tarde."
        )

def create_application() -> Application:
    """Cria e configura a aplicação do Telegram."""
    if not TOKEN:
        logger.error("TELEGRAM_TOKEN não configurado!")
        
    application = Application.builder().token(TOKEN).build()

    # Adicionar handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("reload", reload_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Adicionar error handler
    application.add_error_handler(error_handler)

    return application
