import json

# Cargar el archivo JSON existente
with open('data/checklist.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Iterar sobre las tareas y agregar las claves "urgent" e "important" si no existen
for task_id, task_info in data["tasks"].items():
    if "urgent" not in task_info:
        task_info["urgent"] = False
    if "important" not in task_info:
        task_info["important"] = False

# Guardar los cambios en el archivo JSON
with open('data/checklist.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Archivo JSON actualizado con éxito.")
