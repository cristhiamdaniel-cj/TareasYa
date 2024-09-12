from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone
import logging
from bot.checklist import load_users, get_pending_tasks

# Inicializa el scheduler
scheduler = AsyncIOScheduler()

# Define la zona horaria de Colombia
colombia_tz = timezone('America/Bogota')

# Función para enviar recordatorios a los usuarios
async def send_reminders(context):
    users = load_users()  # Cargar los usuarios registrados
    for user_id in users:
        tasks = get_pending_tasks()  # Obtener las tareas pendientes
        if tasks:
            message = "Aquí tienes tu lista de tareas pendientes:\n" + tasks
            # Enviar el mensaje a cada usuario registrado
            await context.bot.send_message(chat_id=user_id, text=message)
        else:
            # Si no hay tareas pendientes, enviar un mensaje indicando esto
            await context.bot.send_message(chat_id=user_id, text="¡No tienes tareas pendientes! 😃")
        logging.info(f"Recordatorio enviado al usuario {user_id}")

# Función para programar el recordatorio diario
def set_reminder(application):
    scheduler.add_job(
        send_reminders,
        'cron',
        hour=17,  # Hora a la que deseas enviar el recordatorio
        minute=21,  # Minuto a la que deseas enviar el recordatorio
        timezone=colombia_tz,
        args=[application]  # Pasar el contexto de la aplicación como argumento
    )
    scheduler.start()  # Iniciar el scheduler
    logging.info("Recordatorio diario programado a las 17:00 hora de Colombia")

# Función para programar el recordatorio diario a las 9:00 AM
def schedule_daily_reminder(application):
    scheduler.add_job(
        send_reminders,
        'cron',
        hour=9,
        minute=0,  # Programado para las 9:00 AM
        timezone=colombia_tz,
        args=[application]  # Pasar la aplicación completa como argumento
    )
    scheduler.start()  # Iniciar el scheduler
    logging.info("Recordatorio diario programado a las 9:00 AM hora de Colombia")


