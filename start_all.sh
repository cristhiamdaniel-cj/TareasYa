##########!/bin/bash
#########
########## Activar entorno virtual
#########source .venv/bin/activate
#########
########## Iniciar el bot en segundo plano
#########echo "Iniciando el bot..."
#########nohup python3 -m bot.main > bot_output.log 2>&1 &
#########
########## Cambiar al directorio de datos
#########cd data
#########
########## Iniciar servidor HTTP en segundo plano
#########echo "Iniciando servidor HTTP..."
#########nohup python3 -m http.server 8000 > server_output.log 2>&1 &
#########
########## Volver al directorio raíz
#########cd ..
#########
########## Iniciar ngrok para exponer el servidor HTTP
#########echo "Iniciando ngrok..."
#########nohup ngrok http 8000 > ngrok_output.log 2>&1 &
#########
#########echo "Todos los servicios han sido iniciados."
#########
#########
#########!/bin/bash
########
######### Activar entorno virtual
########. .venv/bin/activate
########
######### Iniciar el bot en segundo plano
########echo "Iniciando el bot..."
########nohup python3 -m bot.main > bot_output.log 2>&1 &
########
######### Cambiar al directorio de datos
########cd data
########
######### Iniciar servidor HTTP en segundo plano
########echo "Iniciando servidor HTTP..."
########nohup python3 -m http.server 8000 > server_output.log 2>&1 &
########
######### Volver al directorio raíz
########cd ..
########
######### Iniciar ngrok para exponer el servidor HTTP
########echo "Iniciando ngrok..."
########nohup ngrok http 8000 > ngrok_output.log 2>&1 &
########
########echo "Todos los servicios han sido iniciados."
########
######### Esperar un poco para permitir que ngrok se inicie y capture la salida
########sleep 5
########
######### Mostrar la URL pública generada por ngrok
########echo "URL pública de ngrok:"
########grep -o "https://[0-9a-z]*\.ngrok-free.app" ngrok_output.log
########
########!/bin/bash
#######
######## Activar entorno virtual
#######. .venv/bin/activate
#######
######## Iniciar el bot en segundo plano
#######echo "Iniciando el bot..."
#######nohup python3 -m bot.main > bot_output.log 2>&1 &
#######
######## Cambiar al directorio de datos
#######cd data
#######
######## Iniciar servidor HTTP en segundo plano
#######echo "Iniciando servidor HTTP..."
#######nohup python3 -m http.server 8000 > server_output.log 2>&1 &
#######
######## Volver al directorio raíz
#######cd ..
#######
######## Iniciar ngrok para exponer el servidor HTTP
#######echo "Iniciando ngrok..."
#######nohup ngrok http 8000 > ngrok_output.log 2>&1 &
#######
#######echo "Todos los servicios han sido iniciados."
#######
######## Esperar un poco para permitir que ngrok se inicie y capture la salida
#######sleep 10
#######
######## Mostrar la URL pública generada por ngrok
#######echo "URL pública de ngrok:"
#######grep -o "https://[0-9a-z]*\.ngrok-free.app" ngrok_output.log
#######
######## Verificar si se encontró la URL de ngrok
#######if [ $? -ne 0 ]; then
#######  echo "No se pudo obtener la URL de ngrok. Verifique el archivo ngrok_output.log para más detalles."
#######fi
#######
#######!/bin/bash
######
####### Activar entorno virtual
######. .venv/bin/activate
######
####### Iniciar el bot en segundo plano
######echo "Iniciando el bot..."
######nohup python3 -m bot.main > bot_output.log 2>&1 &
######
####### Cambiar al directorio de datos
######cd data
######
####### Iniciar servidor HTTP en segundo plano
######echo "Iniciando servidor HTTP..."
######nohup python3 -m http.server 8000 > server_output.log 2>&1 &
######
####### Volver al directorio raíz
######cd ..
######
####### Iniciar ngrok para exponer el servidor HTTP
######echo "Iniciando ngrok..."
######nohup ngrok start --all > ngrok_output.log 2>&1 &
######
######echo "Todos los servicios han sido iniciados."
######
####### Esperar un poco para permitir que ngrok se inicie y capture la salida
######sleep 10
######
####### Mostrar la URL pública generada por ngrok
######echo "URL pública de ngrok:"
######grep -o "https://[0-9a-z]*\.ngrok-free.app" ngrok_output.log
######
####### Verificar si se encontró la URL de ngrok
######if [ $? -ne 0 ]; then
######  echo "No se pudo obtener la URL de ngrok. Verifique el archivo ngrok_output.log para más detalles."
######fi
######
#####
######!/bin/bash
#####
#####echo "Iniciando el bot..."
#####. .venv/bin/activate  # Activar el entorno virtual
#####nohup python3 -m bot.main > bot_output.log 2>&1 &  # Ejecuta el bot en segundo plano
#####
#####echo "Iniciando servidor HTTP..."
#####cd data
#####nohup python3 -m http.server 8000 > ../server_output.log 2>&1 &  # Ejecuta el servidor HTTP en segundo plano
#####cd ..
#####
#####echo "Iniciando ngrok..."
#####nohup ngrok http 8000 > ngrok_output.log 2>&1 &  # Ejecuta ngrok en segundo plano
#####
#####sleep 5  # Espera unos segundos para que ngrok se inicie
#####
#####NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok-free.app")
#####
#####if [[ -z "$NGROK_URL" ]]; then
#####  echo "No se pudo obtener la URL de ngrok. Verifique el archivo ngrok_output.log para más detalles."
#####else
#####  echo "URL pública de ngrok: $NGROK_URL"
#####fi
#####
#####echo "Todos los servicios han sido iniciados."
#####
#####
#####!/bin/bash
####
####echo "Iniciando el bot..."
####. .venv/bin/activate  # Activar el entorno virtual
####nohup python3 -m bot.main > bot_output.log 2>&1 &  # Ejecuta el bot en segundo plano
####
####echo "Iniciando servidor HTTP..."
####cd data
####nohup python3 -m http.server 8000 > ../server_output.log 2>&1 &  # Ejecuta el servidor HTTP en segundo plano
####cd ..
####
####echo "Iniciando ngrok..."
####nohup ngrok http 8000 > ngrok_output.log 2>&1 &  # Ejecuta ngrok en segundo plano
####
####sleep 5  # Espera unos segundos para que ngrok se inicie
####
####NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok-free.app")
####
####if [ -z "$NGROK_URL" ]; then
####  echo "No se pudo obtener la URL de ngrok. Verifique el archivo ngrok_output.log para más detalles."
####else
####  echo "URL pública de ngrok: $NGROK_URL"
####fi
####
####echo "Todos los servicios han sido iniciados."
####
####!/bin/bash
###
###echo "Iniciando el bot..."
###. .venv/bin/activate  # Activar el entorno virtual
###nohup python3 -m bot.main > bot_output.log 2>&1 &  # Ejecuta el bot en segundo plano
###
###echo "Iniciando servidor HTTP..."
###cd data
###nohup python3 -m http.server 8000 > ../server_output.log 2>&1 &  # Ejecuta el servidor HTTP en segundo plano
###cd ..
###
###echo "Cerrando cualquier sesión existente de ngrok..."
###pkill -f ngrok  # Mata cualquier proceso de ngrok que ya esté ejecutándose
###
###echo "Iniciando ngrok..."
###nohup ngrok http 8000 > ngrok_output.log 2>&1 &  # Ejecuta ngrok en segundo plano
###
###sleep 5  # Espera unos segundos para que ngrok se inicie
###
###NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok-free.app")
###
###if [ -z "$NGROK_URL" ]; then
###  echo "No se pudo obtener la URL de ngrok. Verifique el archivo ngrok_output.log para más detalles."
###else
###  echo "URL pública de ngrok: $NGROK_URL"
###fi
###
###echo "Todos los servicios han sido iniciados."
###
###!/bin/bash
##
##echo "Iniciando el bot..."
##. .venv/bin/activate  # Activar el entorno virtual
##nohup python3 -m bot.main > bot_output.log 2>&1 &  # Ejecuta el bot en segundo plano
##
##echo "Iniciando servidor HTTP..."
##cd data
##nohup python3 -m http.server 8000 > ../server_output.log 2>&1 &  # Ejecuta el servidor HTTP en segundo plano
##cd ..
##
##echo "Cerrando cualquier sesión existente de ngrok..."
##pkill -f ngrok  # Mata cualquier proceso de ngrok que ya esté ejecutándose
##
##echo "Iniciando ngrok..."
### Ejecuta ngrok con autenticación
##nohup ngrok http 8000 --config ~/.ngrok2/ngrok.yml > ngrok_output.log 2>&1 &  # Ejecuta ngrok en segundo plano
##
##sleep 5  # Espera unos segundos para que ngrok se inicie
##
##NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok-free.app")
##
##if [ -z "$NGROK_URL" ]; then
##  echo "No se pudo obtener la URL de ngrok. Verifique el archivo ngrok_output.log para más detalles."
##else
##  echo "URL pública de ngrok: $NGROK_URL"
##fi
##
##echo "Todos los servicios han sido iniciados."
##
##!/bin/bash
#
#echo "Iniciando el bot..."
#. .venv/bin/activate  # Activar el entorno virtual
#nohup python3 -m bot.main > bot_output.log 2>&1 &  # Ejecuta el bot en segundo plano
#
#echo "Iniciando servidor HTTP..."
#cd data
#nohup python3 -m http.server 8000 > ../server_output.log 2>&1 &  # Ejecuta el servidor HTTP en segundo plano
#cd ..
#
#echo "Cerrando cualquier sesión existente de ngrok..."
#pkill -f ngrok  # Mata cualquier proceso de ngrok que ya esté ejecutándose
#
#echo "Iniciando ngrok..."
#nohup ngrok start --all --config ~/.ngrok2/ngrok.yml > ngrok_output.log 2>&1 &  # Ejecuta ngrok en segundo plano con configuración
#
#sleep 5  # Espera unos segundos para que ngrok se inicie
#
#NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok-free.app")
#
#if [ -z "$NGROK_URL" ]; then
#  echo "No se pudo obtener la URL de ngrok. Verifique el archivo ngrok_output.log para más detalles."
#else
#  echo "URL pública de ngrok: $NGROK_URL"
#fi
#
#echo "Todos los servicios han sido iniciados."
#
#!/bin/bash

echo "Iniciando el bot..."
. .venv/bin/activate  # Activar el entorno virtual
nohup python3 -m bot.main > bot_output.log 2>&1 &  # Ejecuta el bot en segundo plano

echo "Iniciando servidor HTTP..."
cd data
nohup python3 -m http.server 8000 > ../server_output.log 2>&1 &  # Ejecuta el servidor HTTP en segundo plano
cd ..

echo "Cerrando cualquier sesión existente de ngrok..."
pkill -f ngrok  # Mata cualquier proceso de ngrok que ya esté ejecutándose

echo "Iniciando ngrok..."
nohup ngrok start --all --config ~/.ngrok2/ngrok.yml > ngrok_output.log 2>&1 &  # Ejecuta ngrok en segundo plano

sleep 5  # Espera unos segundos para que ngrok se inicie

NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok-free.app")

if [ -z "$NGROK_URL" ]; then
  echo "No se pudo obtener la URL de ngrok. Verifique el archivo ngrok_output.log para más detalles."
else
  echo "URL pública de ngrok: $NGROK_URL"
fi

echo "Todos los servicios han sido iniciados."

