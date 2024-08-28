# bot/handlers.py

from telegram.ext import CommandHandler
from bot.checklist import start, add_task, mark_task, unmark_task, get_checklist

def setup_handlers(application):
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add_task))
    application.add_handler(CommandHandler("mark", mark_task))
    application.add_handler(CommandHandler("unmark", unmark_task))
    application.add_handler(CommandHandler("checklist", get_checklist))
