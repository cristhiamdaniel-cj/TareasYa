from telegram.ext import CommandHandler
from bot.checklist import start, add_task, mark_task, unmark_task, get_checklist, set_priority, show_eisenhower, \
    delete_tasks
from bot.reminders import set_reminders

# Funcion para configurar los manejadores de comandos
def setup_handlers(application):
    application.add_handler(CommandHandler("init", start))
    application.add_handler(CommandHandler("add", add_task))
    application.add_handler(CommandHandler("done", mark_task))
    application.add_handler(CommandHandler("undo", unmark_task))
    application.add_handler(CommandHandler("list", get_checklist))
    application.add_handler(CommandHandler("prio", set_priority))
    application.add_handler(CommandHandler("eisn", show_eisenhower))
    application.add_handler(CommandHandler("delete", delete_tasks))

    # Añadir recordatorio
    set_reminders(application)
