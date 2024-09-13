import logging
from telegram.ext import Application
from bot.handlers import setup_handlers
from bot.config import TOKEN
from bot.reminders import scheduler
from bot.reminders import set_reminders


# Función para manejar los errores del bot
async def error_handler(update, context):
    """Loga los errores causados por las actualizaciones del bot."""
    logging.error(msg="Exception while handling an update:", exc_info=context.error)

# Función principal
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

    # Configurar los recordatorios
    set_reminders(application)

    # Añadir manejador de errores
    application.add_error_handler(error_handler)

    # Solo iniciar el scheduler si no está corriendo
    if not scheduler.running:
        scheduler.start()
        logger.info("Scheduler iniciado")
    else:
        logger.info("Scheduler ya está corriendo")

    logger.info("Bot iniciado")

    # Iniciar el bot
    application.run_polling()


if __name__ == '__main__':
    main()
