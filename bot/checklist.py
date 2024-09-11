# # # # bot/checklist.py
# # #
# # # import logging
# # # import json
# # # import os
# # #
# # # checklist = {}
# # # next_id = 1  # Inicializar el identificador único
# # # CHECKLIST_FILE = "data/checklist.json"  # Ruta al archivo JSON
# # #
# # # # Configuración del logger
# # # logger = logging.getLogger(__name__)
# # #
# # #
# # # # Función para cargar el checklist desde el archivo JSON
# # # def load_checklist():
# # #     global checklist, next_id
# # #     if os.path.exists(CHECKLIST_FILE):
# # #         with open(CHECKLIST_FILE, 'r') as file:
# # #             data = json.load(file)
# # #             checklist = {int(k): v for k, v in data.get("tasks", {}).items()}
# # #             next_id = data.get("next_id", 1)
# # #             logger.info("Checklist cargado desde el archivo JSON")
# # #     else:
# # #         logger.info("Archivo JSON no encontrado. Creando uno nuevo.")
# # #
# # #
# # # # Función para guardar el checklist en el archivo JSON
# # # def save_checklist():
# # #     # Crear el directorio 'data/' si no existe
# # #     os.makedirs(os.path.dirname(CHECKLIST_FILE), exist_ok=True)
# # #
# # #     with open(CHECKLIST_FILE, 'w') as file:
# # #         data = {
# # #             "tasks": checklist,
# # #             "next_id": next_id
# # #         }
# # #         json.dump(data, file, indent=4)
# # #         logger.info("Checklist guardado en el archivo JSON")
# # #
# # #
# # # async def start(update, context):
# # #     logger.info("Comando /start ejecutado")
# # #     await update.message.reply_text('Hola! Soy tu bot de checklist. Usa los comandos /add, /mark, /unmark, /checklist.')
# # #
# # #
# # # async def add_task(update, context):
# # #     global next_id
# # #     task = ' '.join(context.args)
# # #     if not task:
# # #         await update.message.reply_text('Por favor, especifica una tarea para agregar.')
# # #         logger.warning("Comando /add ejecutado sin especificar una tarea")
# # #     else:
# # #         checklist[next_id] = {"task": task, "completed": False}
# # #         await update.message.reply_text(f"Tarea '{task}' agregada con identificador {next_id}.")
# # #         logger.info(f"Tarea '{task}' agregada con identificador {next_id}")
# # #         next_id += 1
# # #         save_checklist()
# # #
# # #
# # # async def mark_task(update, context):
# # #     try:
# # #         task_id = int(context.args[0])
# # #         if task_id in checklist:
# # #             checklist[task_id]["completed"] = True
# # #             await update.message.reply_text(f"Tarea '{checklist[task_id]['task']}' marcada como completada.")
# # #             logger.info(f"Tarea '{checklist[task_id]['task']}' marcada como completada con identificador {task_id}")
# # #             save_checklist()
# # #         else:
# # #             await update.message.reply_text(f"No se encontró ninguna tarea con el identificador {task_id}.")
# # #             logger.warning(f"No se encontró ninguna tarea con el identificador {task_id}")
# # #     except (IndexError, ValueError):
# # #         await update.message.reply_text('Por favor, proporciona un identificador de tarea válido.')
# # #         logger.error("Identificador inválido proporcionado en comando /mark")
# # #
# # #
# # # async def unmark_task(update, context):
# # #     try:
# # #         task_id = int(context.args[0])
# # #         if task_id in checklist:
# # #             checklist[task_id]["completed"] = False
# # #             await update.message.reply_text(f"Tarea '{checklist[task_id]['task']}' desmarcada.")
# # #             logger.info(f"Tarea '{checklist[task_id]['task']}' desmarcada con identificador {task_id}")
# # #             save_checklist()
# # #         else:
# # #             await update.message.reply_text(f"No se encontró ninguna tarea con el identificador {task_id}.")
# # #             logger.warning(f"No se encontró ninguna tarea con el identificador {task_id}")
# # #     except (IndexError, ValueError):
# # #         await update.message.reply_text('Por favor, proporciona un identificador de tarea válido.')
# # #         logger.error("Identificador inválido proporcionado en comando /unmark")
# # #
# # #
# # # async def get_checklist(update, context):
# # #     if not checklist:
# # #         await update.message.reply_text("El checklist está vacío.")
# # #         logger.info("Comando /checklist ejecutado: El checklist está vacío")
# # #     else:
# # #         response = "Checklist:\n"
# # #         for task_id, info in checklist.items():
# # #             status = "✅" if info["completed"] else "❌"
# # #             response += f"{task_id}: {status} {info['task']}\n"
# # #         await update.message.reply_text(response)
# # #         logger.info("Comando /checklist ejecutado. Estado actual:\n" + response)
# # #
# # #
# # # # Cargar el checklist cuando se inicia el módulo
# # # load_checklist()
# #
# # import logging
# # import json
# # import os
# # from web.generate_html import generate_html, save_html_file
# #
# # checklist = {}
# # next_id = 1
# # CHECKLIST_FILE = "data/checklist.json"
# #
# # # Configuración del logger
# # logger = logging.getLogger(__name__)
# #
# #
# # # Función para cargar el checklist desde el archivo JSON
# # def load_checklist():
# #     global checklist, next_id
# #     if os.path.exists(CHECKLIST_FILE):
# #         with open(CHECKLIST_FILE, 'r') as file:
# #             data = json.load(file)
# #             checklist = {int(k): v for k, v in data.get("tasks", {}).items()}
# #             next_id = data.get("next_id", 1)
# #             logger.info("Checklist cargado desde el archivo JSON")
# #     else:
# #         logger.info("Archivo JSON no encontrado. Creando uno nuevo.")
# #
# #
# # # Función para guardar el checklist en el archivo JSON
# # def save_checklist():
# #     os.makedirs(os.path.dirname(CHECKLIST_FILE), exist_ok=True)
# #     with open(CHECKLIST_FILE, 'w') as file:
# #         data = {
# #             "tasks": checklist,
# #             "next_id": next_id
# #         }
# #         json.dump(data, file, indent=4)
# #         logger.info("Checklist guardado en el archivo JSON")
# #
# #
# # # Función para clasificar tareas en la matriz de Eisenhower
# # def categorize_tasks():
# #     eisenhower_matrix = {
# #         "Urgente e Importante": [],
# #         "No Urgente pero Importante": [],
# #         "Urgente pero No Importante": [],
# #         "No Urgente y No Importante": []
# #     }
# #
# #     for task_id, info in checklist.items():
# #         task = info["task"]
# #         completed = info.get("completed", False)
# #         urgent = info.get("urgent", False)
# #         important = info.get("important", False)
# #
# #         if urgent and important:
# #             eisenhower_matrix["Urgente e Importante"].append((task_id, task, completed))
# #         elif not urgent and important:
# #             eisenhower_matrix["No Urgente pero Importante"].append((task_id, task, completed))
# #         elif urgent and not important:
# #             eisenhower_matrix["Urgente pero No Importante"].append((task_id, task, completed))
# #         else:
# #             eisenhower_matrix["No Urgente y No Importante"].append((task_id, task, completed))
# #
# #     # Generar y guardar HTML
# #     html_content = generate_html(eisenhower_matrix)
# #     save_html_file(html_content, "data/eisenhower_matrix.html")
# #
# #     return eisenhower_matrix
# #
# #
# # # Funciones asincrónicas para comandos del bot
# # async def start(update, context):
# #     logger.info("Comando /start ejecutado")
# #     await update.message.reply_text(
# #         'Hola! Soy tu bot de checklist. Usa los comandos /add, /mark, /unmark, /checklist, /set_priority y /eisenhower.')
# #
# #
# # async def add_task(update, context):
# #     global next_id
# #     task = ' '.join(context.args)
# #     if not task:
# #         await update.message.reply_text('Por favor, especifica una tarea para agregar.')
# #         logger.warning("Comando /add ejecutado sin especificar una tarea")
# #     else:
# #         checklist[next_id] = {"task": task, "completed": False, "urgent": False, "important": False}
# #         await update.message.reply_text(f"Tarea '{task}' agregada con identificador {next_id}.")
# #         logger.info(f"Tarea '{task}' agregada con identificador {next_id}")
# #         next_id += 1
# #         save_checklist()
# #
# #
# # async def mark_task(update, context):
# #     try:
# #         task_id = int(context.args[0])
# #         if task_id in checklist:
# #             checklist[task_id]["completed"] = True
# #             await update.message.reply_text(f"Tarea '{checklist[task_id]['task']}' marcada como completada.")
# #             logger.info(f"Tarea '{checklist[task_id]['task']}' marcada como completada con identificador {task_id}")
# #             save_checklist()
# #         else:
# #             await update.message.reply_text(f"No se encontró ninguna tarea con el identificador {task_id}.")
# #             logger.warning(f"No se encontró ninguna tarea con el identificador {task_id}")
# #     except (IndexError, ValueError):
# #         await update.message.reply_text('Por favor, proporciona un identificador de tarea válido.')
# #         logger.error("Identificador inválido proporcionado en comando /mark")
# #
# #
# # async def unmark_task(update, context):
# #     try:
# #         task_id = int(context.args[0])
# #         if task_id in checklist:
# #             checklist[task_id]["completed"] = False
# #             await update.message.reply_text(f"Tarea '{checklist[task_id]['task']}' desmarcada.")
# #             logger.info(f"Tarea '{checklist[task_id]['task']}' desmarcada con identificador {task_id}")
# #             save_checklist()
# #         else:
# #             await update.message.reply_text(f"No se encontró ninguna tarea con el identificador {task_id}.")
# #             logger.warning(f"No se encontró ninguna tarea con el identificador {task_id}")
# #     except (IndexError, ValueError):
# #         await update.message.reply_text('Por favor, proporciona un identificador de tarea válido.')
# #         logger.error("Identificador inválido proporcionado en comando /unmark")
# #
# #
# # async def get_checklist(update, context):
# #     if not checklist:
# #         await update.message.reply_text("El checklist está vacío.")
# #         logger.info("Comando /checklist ejecutado: El checklist está vacío")
# #     else:
# #         response = "Checklist:\n"
# #         for task_id, info in checklist.items():
# #             status = "✅" if info["completed"] else "❌"
# #             response += f"{task_id}: {status} {info['task']}\n"
# #         await update.message.reply_text(response)
# #         logger.info("Comando /checklist ejecutado. Estado actual:\n" + response)
# #
# #
# # async def set_priority(update, context):
# #     try:
# #         task_id = int(context.args[0])
# #         urgent = context.args[1].lower() == 'urgent'
# #         important = context.args[2].lower() == 'important'
# #
# #         if task_id in checklist:
# #             checklist[task_id]["urgent"] = urgent
# #             checklist[task_id]["important"] = important
# #             await update.message.reply_text(f"Prioridad de la tarea '{checklist[task_id]['task']}' actualizada.")
# #             save_checklist()
# #         else:
# #             await update.message.reply_text("No se encontró ninguna tarea con el identificador dado.")
# #     except (IndexError, ValueError):
# #         await update.message.reply_text('Por favor, proporciona un identificador de tarea válido y las prioridades.')
# #
# #
# # async def show_eisenhower(update, context):
# #     matrix = categorize_tasks()
# #     response = ""
# #     for category, tasks in matrix.items():
# #         response += f"\n{category}:\n"
# #         if tasks:
# #             for task_id, task, completed in tasks:
# #                 status = "✅" if completed else "❌"
# #                 response += f"  {task_id}: {status} {task}\n"
# #         else:
# #             response += "  No hay tareas en esta categoría.\n"
# #     await update.message.reply_text(response)
# #
# #
# # # Cargar el checklist cuando se inicia el módulo
# # load_checklist()
#
#
# # bot/checklist.py
#
# import logging
# import json
# import os
# from telegram import Update
# from telegram.ext import ContextTypes
# from web.generate_html import generate_html, save_html_file
#
# checklist = {}
# next_id = 1  # Inicializar el identificador único
# CHECKLIST_FILE = "data/checklist.json"  # Ruta al archivo JSON
#
# # Configuración del logger
# logger = logging.getLogger(__name__)
#
#
# # Función para cargar el checklist desde el archivo JSON
# def load_checklist():
#     global checklist, next_id
#     if os.path.exists(CHECKLIST_FILE):
#         with open(CHECKLIST_FILE, 'r') as file:
#             data = json.load(file)
#             checklist = {int(k): v for k, v in data.get("tasks", {}).items()}
#             next_id = data.get("next_id", 1)
#             logger.info("Checklist cargado desde el archivo JSON")
#     else:
#         logger.info("Archivo JSON no encontrado. Creando uno nuevo.")
#
#
# # Función para guardar el checklist en el archivo JSON
# def save_checklist():
#     # Crear el directorio 'data/' si no existe
#     os.makedirs(os.path.dirname(CHECKLIST_FILE), exist_ok=True)
#
#     with open(CHECKLIST_FILE, 'w') as file:
#         data = {
#             "tasks": checklist,
#             "next_id": next_id
#         }
#         json.dump(data, file, indent=4)
#         logger.info("Checklist guardado en el archivo JSON")
#
#
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     logger.info("Comando /start ejecutado")
#     await update.message.reply_text(
#         'Hola! Soy tu bot de checklist. Usa los comandos /add, /mark, /unmark, /checklist, /set_priority, /eisenhower.')
#
#
# async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     global next_id
#     task = ' '.join(context.args)
#     if not task:
#         await update.message.reply_text('Por favor, especifica una tarea para agregar.')
#         logger.warning("Comando /add ejecutado sin especificar una tarea")
#     else:
#         checklist[next_id] = {"task": task, "completed": False, "urgent": False, "important": False}
#         await update.message.reply_text(f"Tarea '{task}' agregada con identificador {next_id}.")
#         logger.info(f"Tarea '{task}' agregada con identificador {next_id}")
#         next_id += 1
#         save_checklist()
#
#
# async def mark_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     try:
#         task_id = int(context.args[0])
#         if task_id in checklist:
#             checklist[task_id]["completed"] = True
#             await update.message.reply_text(f"Tarea '{checklist[task_id]['task']}' marcada como completada.")
#             logger.info(f"Tarea '{checklist[task_id]['task']}' marcada como completada con identificador {task_id}")
#             save_checklist()
#         else:
#             await update.message.reply_text(f"No se encontró ninguna tarea con el identificador {task_id}.")
#             logger.warning(f"No se encontró ninguna tarea con el identificador {task_id}")
#     except (IndexError, ValueError):
#         await update.message.reply_text('Por favor, proporciona un identificador de tarea válido.')
#         logger.error("Identificador inválido proporcionado en comando /mark")
#
#
# async def unmark_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     try:
#         task_id = int(context.args[0])
#         if task_id in checklist:
#             checklist[task_id]["completed"] = False
#             await update.message.reply_text(f"Tarea '{checklist[task_id]['task']}' desmarcada.")
#             logger.info(f"Tarea '{checklist[task_id]['task']}' desmarcada con identificador {task_id}")
#             save_checklist()
#         else:
#             await update.message.reply_text(f"No se encontró ninguna tarea con el identificador {task_id}.")
#             logger.warning(f"No se encontró ninguna tarea con el identificador {task_id}")
#     except (IndexError, ValueError):
#         await update.message.reply_text('Por favor, proporciona un identificador de tarea válido.')
#         logger.error("Identificador inválido proporcionado en comando /unmark")
#
#
# async def get_checklist(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if not checklist:
#         await update.message.reply_text("El checklist está vacío.")
#         logger.info("Comando /checklist ejecutado: El checklist está vacío")
#     else:
#         response = "Checklist:\n"
#         for task_id, info in checklist.items():
#             status = "✅" if info["completed"] else "❌"
#             response += f"{task_id}: {status} {info['task']}\n"
#         await update.message.reply_text(response)
#         logger.info("Comando /checklist ejecutado. Estado actual:\n" + response)
#
#
# async def set_priority(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     try:
#         task_id = int(context.args[0])
#         urgent = context.args[1].lower() == 'urgent'
#         important = context.args[2].lower() == 'important'
#
#         if task_id in checklist:
#             checklist[task_id]["urgent"] = urgent
#             checklist[task_id]["important"] = important
#             await update.message.reply_text(f"Prioridad de la tarea '{checklist[task_id]['task']}' actualizada.")
#             logger.info(f"Prioridad de la tarea '{checklist[task_id]['task']}' actualizada.")
#             save_checklist()
#         else:
#             await update.message.reply_text("No se encontró ninguna tarea con el identificador dado.")
#     except (IndexError, ValueError):
#         await update.message.reply_text('Por favor, proporciona un identificador de tarea válido y las prioridades.')
#         logger.error("Comando /set_priority ejecutado con argumentos inválidos")
#
#
# def categorize_tasks():
#     eisenhower_matrix = {
#         "Urgente e Importante": [],
#         "No Urgente pero Importante": [],
#         "Urgente pero No Importante": [],
#         "No Urgente y No Importante": []
#     }
#     for task_id, info in checklist.items():
#         if info["urgent"] and info["important"]:
#             eisenhower_matrix["Urgente e Importante"].append((task_id, info["task"], info["completed"]))
#         elif not info["urgent"] and info["important"]:
#             eisenhower_matrix["No Urgente pero Importante"].append((task_id, info["task"], info["completed"]))
#         elif info["urgent"] and not info["important"]:
#             eisenhower_matrix["Urgente pero No Importante"].append((task_id, info["task"], info["completed"]))
#         else:
#             eisenhower_matrix["No Urgente y No Importante"].append((task_id, info["task"], info["completed"]))
#     return eisenhower_matrix
#
#
# async def show_eisenhower(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     matrix = categorize_tasks()
#     response = ""
#     for category, tasks in matrix.items():
#         response += f"\n{category}:\n"
#         if tasks:
#             for task_id, task, completed in tasks:
#                 status = "✅" if completed else "❌"
#                 response += f"  {task_id}: {status} {task}\n"
#         else:
#             response += "  No hay tareas en esta categoría.\n"
#
#     # Generar y guardar el archivo HTML
#     html_content = generate_html(matrix)
#     save_html_file(html_content, "data/eisenhower_matrix.html")
#
#     await update.message.reply_text(response)
#     logger.info("Comando /eisenhower ejecutado. Matriz de Eisenhower generada.")
#
#
# # Cargar el checklist cuando se inicia el módulo
# load_checklist()


# bot/checklist.py

import logging
import json
import os
from telegram import Update
from telegram.ext import ContextTypes
from web.generate_html import generate_html, save_html_file

checklist = {}
next_id = 1  # Inicializar el identificador único
CHECKLIST_FILE = "data/checklist.json"  # Ruta al archivo JSON

# Configuración del logger
logger = logging.getLogger(__name__)


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


def save_checklist():
    os.makedirs(os.path.dirname(CHECKLIST_FILE), exist_ok=True)
    with open(CHECKLIST_FILE, 'w') as file:
        data = {
            "tasks": checklist,
            "next_id": next_id
        }
        json.dump(data, file, indent=4)
        logger.info("Checklist guardado en el archivo JSON")


# Nueva función para eliminar tareas completadas
def delete_completed_tasks():
    global checklist
    checklist = {task_id: info for task_id, info in checklist.items() if not info["completed"]}
    save_checklist()
    logger.info("Tareas completadas eliminadas del checklist")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Comando /init ejecutado")
    await update.message.reply_text(
        'Hola! Soy tu bot de checklist. Usa los comandos:\n'
        '/add [tarea] - Agrega una tarea\n'
        '/done [id] - Marca una tarea como completada\n'
        '/undo [id] - Desmarca una tarea\n'
        '/list - Muestra el checklist\n'
        '/prio [id] [urgente] [importante] - Establece prioridad\n'
        '/eisn - Muestra la matriz de Eisenhower\n'
        '/delete - Elimina todas las tareas completadas'
    )


# async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     global next_id
#     task = ' '.join(context.args)
#     if not task:
#         await update.message.reply_text('Por favor, especifica una tarea para agregar.')
#         logger.warning("Comando /add ejecutado sin especificar una tarea")
#     else:
#         checklist[next_id] = {"task": task, "completed": False, "urgent": False, "important": False}
#         await update.message.reply_text(f"Tarea '{task}' agregada con identificador {next_id}.")
#         logger.info(f"Tarea '{task}' agregada con identificador {next_id}")
#         next_id += 1
#         save_checklist()

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


# async def mark_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     try:
#         task_id = int(context.args[0])
#         if task_id in checklist:
#             checklist[task_id]["completed"] = True
#             await update.message.reply_text(f"Tarea '{checklist[task_id]['task']}' marcada como completada.")
#             logger.info(f"Tarea '{checklist[task_id]['task']}' marcada como completada con identificador {task_id}")
#             save_checklist()
#         else:
#             await update.message.reply_text(f"No se encontró ninguna tarea con el identificador {task_id}.")
#             logger.warning(f"No se encontró ninguna tarea con el identificador {task_id}")
#     except (IndexError, ValueError):
#         await update.message.reply_text('Por favor, proporciona un identificador de tarea válido.')
#         logger.error("Identificador inválido proporcionado en comando /done")


async def mark_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Comprobamos que el ID se haya proporcionado y sea un número entero
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


# async def set_priority(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     try:
#         task_id = int(context.args[0])
#         urgent = context.args[1].lower() == 'urgent'
#         important = context.args[2].lower() == 'important'
#
#         if task_id in checklist:
#             checklist[task_id]["urgent"] = urgent
#             checklist[task_id]["important"] = important
#             await update.message.reply_text(f"Prioridad de la tarea '{checklist[task_id]['task']}' actualizada.")
#             logger.info(f"Prioridad de la tarea '{checklist[task_id]['task']}' actualizada.")
#             save_checklist()
#         else:
#             await update.message.reply_text("No se encontró ninguna tarea con el identificador dado.")
#     except (IndexError, ValueError):
#         await update.message.reply_text('Por favor, proporciona un identificador de tarea válido y las prioridades.')
#         logger.error("Comando /prio ejecutado con argumentos inválidos")

async def set_priority(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Verificamos que al menos haya tres argumentos: ID, urgent y important
        if len(context.args) < 3:
            raise ValueError("Faltan argumentos.")

        task_id = int(context.args[0])  # Intentamos convertir el primer argumento en un entero (ID de la tarea)
        urgent = context.args[1].lower() == 'urgent'  # El segundo argumento debe ser 'urgent'
        important = context.args[2].lower() == 'important'  # El tercer argumento debe ser 'important'

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


# Nueva función asincrónica para el comando /delete
async def delete_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    delete_completed_tasks()
    await update.message.reply_text("Todas las tareas completadas han sido eliminadas.")
    logger.info("Comando /delete ejecutado. Tareas completadas eliminadas.")


# Cargar el checklist cuando se inicia el módulo
load_checklist()
