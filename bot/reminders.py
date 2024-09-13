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

# Función para programar los recordatorios a las 10:00 AM, 3:00 PM y 8:00 PM
def set_reminders(application):
    scheduler.add_job(
        send_reminders,
        'cron',
        hour=10,  # Programado para las 10:00 AM
        minute=0,
        timezone=colombia_tz,
        args=[application]  # Pasar el contexto de la aplicación como argumento
    )
    
    scheduler.add_job(
        send_reminders,
        'cron',
        hour=15,  # Programado para las 3:00 PM
        minute=0,
        timezone=colombia_tz,
        args=[application]  # Pasar el contexto de la aplicación como argumento
    )
    
    scheduler.add_job(
        send_reminders,
        'cron',
        hour=20,  # Programado para las 8:00 PM
        minute=0,
        timezone=colombia_tz,
        args=[application]  # Pasar el contexto de la aplicación como argumento
    )
    
    # scheduler.start()  # Iniciar el scheduler
    logging.info("Recordatorios programados a las 10:00 AM, 3:00 PM y 8:00 PM hora de Colombia")


