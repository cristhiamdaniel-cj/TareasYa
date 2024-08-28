# TareasYa

Este es un bot de Telegram para gestionar un checklist de tareas. Puedes agregar, marcar, desmarcar y ver tareas usando comandos de Telegram.

## Instalación

1. Clona este repositorio.
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Configura tu token de Telegram en `bot/config.py`.

4. Ejecuta el bot:

```bash
python bot/main.py
```

## Comandos del Bot

- `/start`: Inicia el bot y muestra un mensaje de bienvenida.
- `/add <tarea>`: Agrega una nueva tarea al checklist.
- `/mark <tarea>`: Marca una tarea como completada.
- `/unmark <tarea>`: Desmarca una tarea (la pone como no completada).
- `/checklist`: Muestra todas las tareas y su estado.
```

### 9. `requirements.txt`

Este archivo lista las dependencias del proyecto. Asegúrate de incluir `python-telegram-bot` para que otros desarrolladores puedan instalarlo fácilmente.

```plaintext
python-telegram-bot
```

### Instrucciones Finales

1. **Instalar Dependencias**:
   - Asegúrate de instalar las dependencias listadas en `requirements.txt` ejecutando el siguiente comando en tu terminal:

   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecutar el Bot**:
   - Para iniciar el bot, simplemente ejecuta el archivo `main.py` desde PyCharm o desde la terminal:

   ```bash
   python bot/main.py
   ```
