import uvicorn
from fastapi import FastAPI, Request, Response, status
from telegram import Update
from contextlib import asynccontextmanager

from config import TOKEN, WEBHOOK_URL, PORT, logger
from bot import create_application

# Inicializar aplicação do Telegram
telegram_app = create_application()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gerencia o ciclo de vida da aplicação FastAPI (Webhook Setup)."""
    # Configurar Webhook ao iniciar
    if TOKEN and WEBHOOK_URL:
        webhook_path = f"/webhook/{TOKEN}"
        full_url = f"{WEBHOOK_URL}{webhook_path}"
        logger.info(f"Configurando Webhook em: {full_url}")
        await telegram_app.bot.set_webhook(url=full_url)
        await telegram_app.initialize()
    else:
        logger.warning("Webhook não configurado. Verifique TELEGRAM_TOKEN e WEBHOOK_URL.")
    
    yield
    
    # Finalizar ao encerrar
    await telegram_app.shutdown()

# Criar app FastAPI
app = FastAPI(lifespan=lifespan, title="EducaBot 4.0 API")

@app.get("/")
async def index():
    return {"status": "EducaBot 4.0 está online", "version": "4.0.0"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post(f"/webhook/{TOKEN}")
async def telegram_webhook(request: Request):
    """Endpoint que recebe as atualizações do Telegram."""
    try:
        data = await request.json()
        update = Update.de_json(data, telegram_app.bot)
        await telegram_app.process_update(update)
        return Response(status_code=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Erro ao processar webhook: {e}")
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

if __name__ == "__main__":
    # Iniciar servidor
    uvicorn.run("app:app", host="0.0.0.0", port=PORT, reload=False)
