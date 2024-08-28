# bot/main.py

import logging
from telegram.ext import Application
from bot.handlers import setup_handlers
from bot.config import TOKEN


def main():
    # Configuración del logger
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    logger = logging.getLogger(__name__)

    # Crear la aplicación con el token
    application = Application.builder().token(TOKEN).build()

    # Configurar los manejadores de comandos
    setup_handlers(application)

    logger.info("Bot iniciado")

    # Iniciar el bot
    application.run_polling()


if __name__ == '__main__':
    main()
