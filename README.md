# EducaBot 4.0 🤖

O **EducaBot 4.0** é um assistente virtual profissional desenvolvido para auxiliar no processo do **Educacenso** da Secretaria de Estado de Educação do Distrito Federal (SEEDF). Ele utiliza busca semântica leve baseada em **TF-IDF** para responder dúvidas frequentes de forma rápida e eficiente.

## 🚀 Tecnologias Utilizadas

- **Python 3.12+**
- **FastAPI**: Servidor web de alta performance.
- **python-telegram-bot**: Integração com a API do Telegram via Webhook.
- **Scikit-learn**: Motor de busca semântica utilizando TF-IDF e Similaridade de Cosseno.
- **Render**: Plataforma de hospedagem (compatível com plano Free).

## 📁 Estrutura do Projeto

```text
EducaBot/
├── dados/           # Base de conhecimento (FAQ em JSON)
├── logs/            # Registros de execução
├── tests/           # Testes automatizados
├── app.py           # Ponto de entrada FastAPI e Webhook
├── bot.py           # Lógica e handlers do Telegram
├── config.py        # Configurações centralizadas
├── faq.py           # Gerenciador de dados do FAQ
├── ia.py            # Motor de busca semântica
├── requirements.txt # Dependências do projeto
├── render.yaml      # Configuração de Infraestrutura como Código (IaC)
├── Procfile         # Comando de inicialização para o Render
└── README.md        # Documentação do projeto
```

## 🛠️ Como Instalar e Executar Localmente

1. **Clonar o repositório:**
   ```bash
   git clone <url-do-seu-repositorio>
   cd EducaBot
   ```

2. **Criar um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variáveis de ambiente:**
   Crie um arquivo `.env` ou exporte no terminal:
   ```bash
   export TELEGRAM_TOKEN="seu_token_aqui"
   export WEBHOOK_URL="https://sua-url-temporaria.ngrok-free.app"
   export PORT=8000
   ```

5. **Executar a aplicação:**
   ```bash
   python app.py
   ```

## 🌐 Publicação no GitHub

1. Crie um novo repositório no GitHub.
2. Inicialize o git localmente:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: EducaBot 4.0"
   git branch -M main
   git remote add origin <sua-url-github>
   git push -u origin main
   ```

## ☁️ Publicação no Render

1. Acesse o [Render Dashboard](https://dashboard.render.com/).
2. Clique em **New +** > **Blueprint**.
3. Conecte seu repositório do GitHub.
4. O Render detectará automaticamente o arquivo `render.yaml`.
5. Configure as **Environment Variables** no painel do Render:
   - `TELEGRAM_TOKEN`: Token obtido com o @BotFather.
   - `WEBHOOK_URL`: A URL gerada pelo Render (ex: `https://educabot-xyz.onrender.com`).
6. O deploy será iniciado automaticamente.

## 🔄 Como Atualizar o FAQ

1. Edite o arquivo `dados/faq.json`.
2. Adicione novas perguntas e respostas seguindo o formato:
   ```json
   {
     "pergunta": "Sua pergunta aqui?",
     "resposta": "Sua resposta detalhada aqui."
   }
   ```
3. Envie as alterações para o GitHub.
4. No Telegram, envie o comando `/reload` para que o bot recarregue a base sem a necessidade de reiniciar o servidor.

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais e institucionais da SEEDF.
