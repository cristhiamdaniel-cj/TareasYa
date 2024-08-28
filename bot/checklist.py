# bot/checklist.py

import logging
import json
import os

checklist = {}
next_id = 1  # Inicializar el identificador único
CHECKLIST_FILE = "data/checklist.json"  # Ruta al archivo JSON

# Configuración del logger
logger = logging.getLogger(__name__)


# Función para cargar el checklist desde el archivo JSON
def load_checklist():
    global checklist, next_id
    if os.path.exists(CHECKLIST_FILE):
        with open(CHECKLIST_FILE, 'r') as file:
            data = json.load(file)
            checklist = {int(k): v for k, v in data.get("tasks", {}).items()}
            next_id = data.get("next_id", 1)
            logger.info("Checklist cargado desde el archivo JSON")
    else:
        logger.info("Archivo JSON no encontrado. Creando uno nuevo.")


# Función para guardar el checklist en el archivo JSON
def save_checklist():
    # Crear el directorio 'data/' si no existe
    os.makedirs(os.path.dirname(CHECKLIST_FILE), exist_ok=True)

    with open(CHECKLIST_FILE, 'w') as file:
        data = {
            "tasks": checklist,
            "next_id": next_id
        }
        json.dump(data, file, indent=4)
        logger.info("Checklist guardado en el archivo JSON")


async def start(update, context):
    logger.info("Comando /start ejecutado")
    await update.message.reply_text('Hola! Soy tu bot de checklist. Usa los comandos /add, /mark, /unmark, /checklist.')


async def add_task(update, context):
    global next_id
    task = ' '.join(context.args)
    if not task:
        await update.message.reply_text('Por favor, especifica una tarea para agregar.')
        logger.warning("Comando /add ejecutado sin especificar una tarea")
    else:
        checklist[next_id] = {"task": task, "completed": False}
        await update.message.reply_text(f"Tarea '{task}' agregada con identificador {next_id}.")
        logger.info(f"Tarea '{task}' agregada con identificador {next_id}")
        next_id += 1
        save_checklist()


async def mark_task(update, context):
    try:
        task_id = int(context.args[0])
        if task_id in checklist:
            checklist[task_id]["completed"] = True
            await update.message.reply_text(f"Tarea '{checklist[task_id]['task']}' marcada como completada.")
            logger.info(f"Tarea '{checklist[task_id]['task']}' marcada como completada con identificador {task_id}")
            save_checklist()
        else:
            await update.message.reply_text(f"No se encontró ninguna tarea con el identificador {task_id}.")
            logger.warning(f"No se encontró ninguna tarea con el identificador {task_id}")
    except (IndexError, ValueError):
        await update.message.reply_text('Por favor, proporciona un identificador de tarea válido.')
        logger.error("Identificador inválido proporcionado en comando /mark")


async def unmark_task(update, context):
    try:
        task_id = int(context.args[0])
        if task_id in checklist:
            checklist[task_id]["completed"] = False
            await update.message.reply_text(f"Tarea '{checklist[task_id]['task']}' desmarcada.")
            logger.info(f"Tarea '{checklist[task_id]['task']}' desmarcada con identificador {task_id}")
            save_checklist()
        else:
            await update.message.reply_text(f"No se encontró ninguna tarea con el identificador {task_id}.")
            logger.warning(f"No se encontró ninguna tarea con el identificador {task_id}")
    except (IndexError, ValueError):
        await update.message.reply_text('Por favor, proporciona un identificador de tarea válido.')
        logger.error("Identificador inválido proporcionado en comando /unmark")


async def get_checklist(update, context):
    if not checklist:
        await update.message.reply_text("El checklist está vacío.")
        logger.info("Comando /checklist ejecutado: El checklist está vacío")
    else:
        response = "Checklist:\n"
        for task_id, info in checklist.items():
            status = "✅" if info["completed"] else "❌"
            response += f"{task_id}: {status} {info['task']}\n"
        await update.message.reply_text(response)
        logger.info("Comando /checklist ejecutado. Estado actual:\n" + response)


# Cargar el checklist cuando se inicia el módulo
load_checklist()
