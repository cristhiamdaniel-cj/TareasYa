#!/bin/bash

echo "Cerrando instancias anteriores..."

# Eliminar instancias anteriores del bot, servidor HTTP y ngrok
pkill -f "python3 -m bot.main"
pkill -f "python3 -m http.server 8000"
pkill -f ngrok

echo "Instancias anteriores cerradas."

echo "Iniciando el bot..."
. .venv/bin/activate  # Activar el entorno virtual
nohup python3 -m bot.main > bot_output.log 2>&1 &  # Ejecuta el bot en segundo plano
echo "Bot iniciado."

echo "Iniciando servidor HTTP..."
cd data
nohup python3 -m http.server 8000 > ../server_output.log 2>&1 &  # Ejecuta el servidor HTTP en segundo plano
echo "Servidor HTTP iniciado."
cd ..

echo "Iniciando ngrok..."
# Iniciar ngrok y redirigir tanto la salida estándar como los errores a la consola y al archivo de log
nohup ngrok http 8000 --config ~/.ngrok2/ngrok.yml > ngrok_output.log 2>&1 &
sleep 10  # Espera unos segundos para que ngrok se inicie

# Verificar si ngrok se inició correctamente
if ! pgrep -f ngrok > /dev/null; then
  echo "ngrok no se pudo iniciar. Verifica los registros en ngrok_output.log."
  exit 1
fi

# Intentar obtener la URL de ngrok directamente desde su API local
NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | grep -Po '"public_url":"\Khttps://[0-9a-z.-]*')

if [ -z "$NGROK_URL" ]; then
  echo "No se pudo obtener la URL de ngrok. Verifique el archivo ngrok_output.log para más detalles."
else
  echo "URL pública de ngrok: $NGROK_URL"
fi

echo "Todos los servicios han sido iniciados."

# Monitorear logs del bot y de ngrok en tiempo real
echo "Mostrando logs del bot y de ngrok..."
tail -f bot_output.log ngrok_output.log

