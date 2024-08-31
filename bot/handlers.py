# # bot/handlers.py
#
# from telegram.ext import CommandHandler
# from bot.checklist import start, add_task, mark_task, unmark_task, get_checklist, set_priority, show_eisenhower
#
# def setup_handlers(application):
#     application.add_handler(CommandHandler("init", start))  # Cambiado de /start a /init
#     application.add_handler(CommandHandler("add", add_task))  # Sin cambios
#     application.add_handler(CommandHandler("done", mark_task))  # Cambiado de /mark a /done
#     application.add_handler(CommandHandler("undo", unmark_task))  # Cambiado de /unmark a /undo
#     application.add_handler(CommandHandler("list", get_checklist))  # Cambiado de /checklist a /list
#     application.add_handler(CommandHandler("prio", set_priority))  # Cambiado de /set_priority a /prio
#     application.add_handler(CommandHandler("eisn", show_eisenhower))  # Cambiado de /eisenhower a /eisn


# bot/handlers.py

from telegram.ext import CommandHandler
from bot.checklist import start, add_task, mark_task, unmark_task, get_checklist, set_priority, show_eisenhower, delete_tasks


def setup_handlers(application):
    application.add_handler(CommandHandler("init", start))  # Cambiado de /start a /init
    application.add_handler(CommandHandler("add", add_task))  # Sin cambios
    application.add_handler(CommandHandler("done", mark_task))  # Cambiado de /mark a /done
    application.add_handler(CommandHandler("undo", unmark_task))  # Cambiado de /unmark a /undo
    application.add_handler(CommandHandler("list", get_checklist))  # Cambiado de /checklist a /list
    application.add_handler(CommandHandler("prio", set_priority))  # Cambiado de /set_priority a /prio
    application.add_handler(CommandHandler("eisn", show_eisenhower))  # Cambiado de /eisenhower a /eisn
    application.add_handler(CommandHandler("delete", delete_tasks))  # Nuevo comando para eliminar tareas completadas

