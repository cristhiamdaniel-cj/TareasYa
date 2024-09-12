import logging
import json
import os
from telegram import Update
from telegram.ext import ContextTypes
from web.generate_html import generate_html, save_html_file

checklist = {}
next_id = 1  # Inicializar el identificador único
CHECKLIST_FILE = "data/checklist.json"  # Ruta al archivo JSON
USER_FILE = "data/users.json"  # Ruta al archivo JSON de usuarios

# Configuración del logger
logger = logging.getLogger(__name__)

# Cargar el checklist
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

# Guardar el checklist
def save_checklist():
    os.makedirs(os.path.dirname(CHECKLIST_FILE), exist_ok=True)
    with open(CHECKLIST_FILE, 'w') as file:
        data = {
            "tasks": checklist,
            "next_id": next_id
        }
        json.dump(data, file, indent=4)
        logger.info("Checklist guardado en el archivo JSON")

# Función para cargar usuarios desde el archivo JSON
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as file:
            try:
                users = json.load(file)
                logger.info("Usuarios cargados desde el archivo JSON")
                return users
            except json.JSONDecodeError:
                logger.error("Error al cargar el archivo de usuarios. El archivo está vacío o corrupto.")
                return []
    else:
        logger.info("Archivo de usuarios no encontrado. Creando uno nuevo.")
        return []

# Función para guardar los usuarios en el archivo JSON
def save_users(users):
    os.makedirs(os.path.dirname(USER_FILE), exist_ok=True)
    with open(USER_FILE, 'w') as file:
        json.dump(users, file, indent=4)
    logger.info("Usuarios guardados en el archivo JSON")

# Función para añadir un usuario
def add_user(chat_id):
    users = load_users()
    if chat_id not in users:
        users.append(chat_id)
        save_users(users)
        logger.info(f"Usuario {chat_id} añadido.")
    else:
        logger.info(f"Usuario {chat_id} ya estaba registrado.")

# Obtener las tareas pendientes
def get_pending_tasks():
    if not checklist:
        return ""

    response = "Checklist de tareas pendientes:\n"
    for task_id, info in checklist.items():
        if not info["completed"]:
            response += f"{task_id}: ❌ {info['task']}\n"
    return response if response != "Checklist de tareas pendientes:\n" else "No hay tareas pendientes."

# Nueva función para eliminar tareas completadas
def delete_completed_tasks():
    global checklist
    checklist = {task_id: info for task_id, info in checklist.items() if not info["completed"]}
    save_checklist()
    logger.info("Tareas completadas eliminadas del checklist")

# Si no planeas usar el contexto, puedes eliminarlo de la firma de la función
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Comando /init ejecutado")
    chat_id = update.message.chat_id
    add_user(chat_id)  # Añadir el usuario a la lista si no está registrado
    await update.message.reply_text(
        '¡Hola! Has sido registrado para recibir recordatorios diarios.\n'
        'Usa los comandos:\n'
        '/add [tarea] - Agrega una tarea\n'
        '/done [id] - Marca una tarea como completada\n'
        '/undo [id] - Desmarca una tarea\n'
        '/list - Muestra el checklist\n'
        '/prio [id] [urgente] [importante] - Establece prioridad\n'
        '/eisn - Muestra la matriz de Eisenhower\n'
        '/delete - Elimina todas las tareas completadas'
    )

# Función para agregar una tarea al checklist
async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global next_id
    task = ' '.join(context.args)  # Juntamos todos los argumentos en una cadena

    if not task:
        await update.message.reply_text(
            'Por favor, especifica una tarea para agregar.\n'
            'Uso correcto: /add [tarea]\n'
            'Ejemplo: /add Comprar leche'
        )
        logger.warning("Comando /add ejecutado sin especificar una tarea")
    else:
        checklist[next_id] = {"task": task, "completed": False, "urgent": False, "important": False}
        await update.message.reply_text(f"Tarea '{task}' agregada con el ID {next_id}.")
        logger.info(f"Tarea '{task}' agregada con identificador {next_id}")
        next_id += 1
        save_checklist()

# Función para marcar una tarea como completada
async def mark_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        task_id = int(context.args[0])
        if task_id in checklist:
            checklist[task_id]["completed"] = True
            await update.message.reply_text(f"Tarea '{checklist[task_id]['task']}' marcada como completada.")
            logger.info(f"Tarea '{checklist[task_id]['task']}' marcada como completada con identificador {task_id}")
            save_checklist()
        else:
            await update.message.reply_text(f"No se encontró ninguna tarea con el ID {task_id}.")
            logger.warning(f"No se encontró ninguna tarea con el ID {task_id}")
    except (IndexError, ValueError):
        await update.message.reply_text(
            'Uso incorrecto del comando /done. Ejemplo de uso:\n'
            '/done [id]\n'
            'Donde [id] es el número identificador de la tarea.\n'
            'Ejemplo: /done 1'
        )
        logger.error("Identificador inválido proporcionado en comando /done")

# Función para desmarcar una tarea
async def unmark_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        logger.error("Identificador inválido proporcionado en comando /undo")

# Función para mostrar el checklist
async def get_checklist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not checklist:
        await update.message.reply_text("El checklist está vacío.")
        logger.info("Comando /list ejecutado: El checklist está vacío")
    else:
        response = "Checklist:\n"
        for task_id, info in checklist.items():
            status = "✅" if info["completed"] else "❌"
            response += f"{task_id}: {status} {info['task']}\n"
        await update.message.reply_text(response)
        logger.info("Comando /list ejecutado. Estado actual:\n" + response)

# Función para establecer la prioridad de una tarea
async def set_priority(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if len(context.args) < 3:
            raise ValueError("Faltan argumentos.")

        task_id = int(context.args[0])
        urgent = context.args[1].lower() == 'urgent'
        important = context.args[2].lower() == 'important'

        if task_id in checklist:
            checklist[task_id]["urgent"] = urgent
            checklist[task_id]["important"] = important
            await update.message.reply_text(f"Prioridad de la tarea '{checklist[task_id]['task']}' actualizada.")
            logger.info(f"Prioridad de la tarea '{checklist[task_id]['task']}' actualizada.")
            save_checklist()
        else:
            await update.message.reply_text(f"No se encontró ninguna tarea con el ID {task_id}.")
    except (IndexError, ValueError):
        await update.message.reply_text(
            'Uso incorrecto del comando /prio. Ejemplo de uso:\n'
            '/prio [id] urgent important\n'
            'Donde:\n'
            '- [id] es el ID de la tarea (un número entero).\n'
            '- "urgent" indica si la tarea es urgente.\n'
            '- "important" indica si la tarea es importante.\n'
            'Ejemplo: /prio 1 urgent important'
        )
        logger.error("Comando /prio ejecutado con argumentos inválidos")

# Función para categorizar las tareas en la matriz de Eisenhower
def categorize_tasks():
    eisenhower_matrix = {
        "Urgente e Importante": [],
        "No Urgente pero Importante": [],
        "Urgente pero No Importante": [],
        "No Urgente y No Importante": []
    }
    for task_id, info in checklist.items():
        if info["urgent"] and info["important"]:
            eisenhower_matrix["Urgente e Importante"].append((task_id, info["task"], info["completed"]))
        elif not info["urgent"] and info["important"]:
            eisenhower_matrix["No Urgente pero Importante"].append((task_id, info["task"], info["completed"]))
        elif info["urgent"] and not info["important"]:
            eisenhower_matrix["Urgente pero No Importante"].append((task_id, info["task"], info["completed"]))
        else:
            eisenhower_matrix["No Urgente y No Importante"].append((task_id, info["task"], info["completed"]))
    return eisenhower_matrix

# Función para guardar la matriz de Eisenhower en un archivo HTML
async def show_eisenhower(update: Update, context: ContextTypes.DEFAULT_TYPE):
    matrix = categorize_tasks()
    response = ""
    for category, tasks in matrix.items():
        response += f"{category}:\n"
        if tasks:
            for task_id, task, completed in tasks:
                status = "✅" if completed else "❌"
                response += f"  {task_id}: {status} {task}\n"
        else:
            response += "  No hay tareas en esta categoría.\n"

    html_content = generate_html(matrix)
    save_html_file(html_content, "data/eisenhower_matrix.html")

    await update.message.reply_text(response)
    logger.info("Comando /eisn ejecutado. Matriz de Eisenhower generada.")

# Función para eliminar tareas completadas
async def delete_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    confirmation = ' '.join(context.args).lower()

    if confirmation == 'confirm':
        delete_completed_tasks()
        await update.message.reply_text("Todas las tareas completadas han sido eliminadas.")
        logger.info("Comando /delete ejecutado. Tareas completadas eliminadas.")
    else:
        await update.message.reply_text(
            '¿Estás seguro de que quieres eliminar todas las tareas completadas?\n'
            'Si es así, usa: /delete confirm'
        )
        logger.warning("Eliminación de tareas completadas no confirmada.")

# Cargar el checklist cuando se inicia el módulo
load_checklist()
