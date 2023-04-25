import os
import json

# Funcion para convertir los archivos .py en formato JSON
def convert_to_json(file_path):
    # Verifica si el archivo es .py
    if not file_path.endswith('.py'):
        return None
    
    # Lee el contenido del archivo .py
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Crea un diccionario para almacenar el contenido y la ruta del archivo
    data = {
        'path': file_path,
        'content': content
    }
    
    # Convierte el diccionario en formato JSON y devuelve el resultado
    return json.dumps(data)

# Obtiene la ruta del repositorio
repo_path = os.environ['GITHUB_WORKSPACE']

# Recorre todos los archivos en la ruta del repositorio
for root, dirs, files in os.walk(repo_path):
    for file in files:
        # Convierte cada archivo .py en formato JSON
        file_path = os.path.join(root, file)
        json_data = convert_to_json(file_path)
        
        # Escribe el archivo JSON en la misma ruta que el archivo .py
        if json_data:
            with open(file_path.replace('.py', '.json'), 'w') as f:
                f.write(json_data)
