# # # # bot/main.py
# # #
# # # import logging
# # # from telegram.ext import Application
# # # from bot.handlers import setup_handlers
# # # from bot.config import TOKEN
# # #
# # #
# # # def main():
# # #     # Configuración del logger
# # #     logging.basicConfig(
# # #         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
# # #         level=logging.INFO
# # #     )
# # #
# # #     logger = logging.getLogger(__name__)
# # #
# # #     # Crear la aplicación con el token
# # #     application = Application.builder().token(TOKEN).build()
# # #
# # #     # Configurar los manejadores de comandos
# # #     setup_handlers(application)
# # #
# # #     logger.info("Bot iniciado")
# # #
# # #     # Iniciar el bot
# # #     application.run_polling()
# # #
# # #
# # # if __name__ == '__main__':
# # #     main()
# #
# # import logging
# # from telegram.ext import Application
# # from bot.handlers import setup_handlers
# # from bot.config import TOKEN
# #
# # def main():
# #     # Configuración del logger
# #     logging.basicConfig(
# #         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
# #         level=logging.INFO
# #     )
# #
# #     logger = logging.getLogger(__name__)
# #
# #     # Crear la aplicación con el token
# #     application = Application.builder().token(TOKEN).build()
# #
# #     # Configurar los manejadores de comandos
# #     setup_handlers(application)
# #
# #     logger.info("Bot iniciado")
# #
# #     # Iniciar el bot
# #     application.run_polling()
# #
# # if __name__ == '__main__':
# #     main()
#
#
# # bot/main.py
#
# import logging
# from telegram.ext import Application
# from bot.handlers import setup_handlers
# from bot.config import TOKEN
#
# async def error_handler(update, context):
#     """Loga los errores causados por las actualizaciones del bot."""
#     logging.error(msg="Exception while handling an update:", exc_info=context.error)
#     # Puedes agregar lógica adicional para responder a los usuarios en caso de error, si lo deseas
#
# def main():
#     # Configuración del logger
#     logging.basicConfig(
#         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#         level=logging.INFO
#     )
#
#     logger = logging.getLogger(__name__)
#
#     # Crear la aplicación con el token
#     application = Application.builder().token(TOKEN).build()
#
#     # Configurar los manejadores de comandos
#     setup_handlers(application)
#
#     # Añadir manejador de errores
#     application.add_error_handler(error_handler)
#
#     logger.info("Bot iniciado")
#
#     # Iniciar el bot
#     application.run_polling()
#
#
# if __name__ == '__main__':
#     main()

# bot/main.py

import logging
from telegram.ext import Application
from bot.handlers import setup_handlers
from bot.config import TOKEN

async def error_handler(update, context):
    """Loga los errores causados por las actualizaciones del bot."""
    logging.error(msg="Exception while handling an update:", exc_info=context.error)

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

    # Añadir manejador de errores
    application.add_error_handler(error_handler)

    logger.info("Bot iniciado")

    # Iniciar el bot
    application.run_polling()


if __name__ == '__main__':
    main()
