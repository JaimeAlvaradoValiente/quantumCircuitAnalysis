import json
import os


def convert_to_json(file_path):
    """Convierte el archivo Python en un objeto JSON."""
    with open(file_path) as f:
        code = f.read()

    # Analizar el código Python y crear un objeto JSON
    # con el contenido del archivo
    json_obj = {
        "filename": os.path.basename(file_path),
        "code": code
    }

    return json.dumps(json_obj)


if __name__ == "__main__":
    # Obtener la ruta del directorio raíz del repositorio
    repo_path = os.environ["GITHUB_WORKSPACE"]
    print(repo_path)

    # Crear el directorio `json` si no existe
    json_dir = os.path.join(repo_path, "json")
    if not os.path.exists(json_dir):
        os.mkdir(json_dir)

    # Recorrer todos los archivos `.py` en el repositorio y crear archivos `.json`
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(".py"):
                json_data = convert_to_json(file_path)
                if json_data:
                    json_file_path = os.path.join(json_dir, file.replace(".py", ".json"))
                    with open(json_file_path, "w") as f:
                        f.write(json_data)
                    with open(json_file_path) as f:
                        print(f.read())
