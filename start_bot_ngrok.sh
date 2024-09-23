#!/bin/bash

# Ruta al entorno virtual
VENV_DIR=".venv"

# Archivos para logs temporales
BOT_LOG="bot_temp.log"
SERVER_LOG="server_temp.log"

# Función para cerrar los procesos correctamente
function cleanup {
    echo "Cerrando los servicios..."

    # Obtener el PID del bot de Telegram
    BOT_PIDS=$(pgrep -f "python3 -m bot.main")
    if [ -n "$BOT_PIDS" ]; then
        for PID in $BOT_PIDS; do
            echo "Cerrando el bot de Telegram con PID $PID..."
            kill -9 "$PID"
        done
    else
        echo "No se encontró el bot de Telegram ejecutándose."
    fi

    # Obtener el PID del servidor HTTP (puerto 8000)
    SERVER_PIDS=$(lsof -ti:8000)
    if [ -n "$SERVER_PIDS" ]; then
        for PID in $SERVER_PIDS; do
            echo "Cerrando el servidor HTTP con PID $PID..."
            kill -9 "$PID"
        done
    else
        echo "No se encontró el servidor HTTP ejecutándose en el puerto 8000."
    fi

    # Cerrar cualquier proceso de ngrok
    NGROK_PIDS=$(pgrep -f "ngrok http 8000")
    if [ -n "$NGROK_PIDS" ]; then
        for PID in $NGROK_PIDS; do
            echo "Cerrando ngrok con PID $PID..."
            kill -9 "$PID"
        done
    else
        echo "No se encontró ngrok ejecutándose."
    fi

    echo "Todos los servicios han sido cerrados."
}

# Configurar para que los servicios se cierren al finalizar el script
trap cleanup EXIT

# Matar cualquier instancia anterior del bot de Telegram, servidor HTTP y ngrok
cleanup

# Activar el entorno virtual
echo "Activando el entorno virtual..."
source "$VENV_DIR/bin/activate"

# Iniciar el bot en segundo plano y almacenar logs
echo "Iniciando el bot de Telegram..."
nohup python3 -m bot.main > "$BOT_LOG" 2>&1 &
echo "Bot de Telegram iniciado con PID $!"

# Cambiar al directorio data y ejecutar el servidor HTTP en segundo plano, almacenando logs
echo "Iniciando servidor HTTP en el puerto 8000..."
cd data
nohup python3 -m http.server 8000 > "../$SERVER_LOG" 2>&1 &
echo "Servidor HTTP iniciado con PID $!"
cd ..

# Iniciar ngrok para exponer el puerto 8000 (sin logs, ya que lo revisas manualmente)
echo "Iniciando ngrok..."
nohup ngrok http 8000 > /dev/null 2>&1 &
echo "ngrok iniciado con PID $!"

# Mostrar mensajes finales
echo "Todos los servicios han sido iniciados."
echo "Logs temporales almacenados en: $BOT_LOG (bot) y $SERVER_LOG (servidor web)"

# Esperar a que el usuario termine para cerrar los procesos
echo "Presiona Ctrl+C para cerrar los servicios..."
wait

