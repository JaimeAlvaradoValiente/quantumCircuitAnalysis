import json
import os
import requests


def predict(json_data, backend):
    # Hacer la llamada a predict_error desplegado en AWS
    url = 'http://54.217.38.166:5000/predict_error'

    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        'backend': backend,
        'circuit': json_data
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    print(response.text)

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

     # Obtener la línea que define el backend y extraer el nombre del backend
    backend_line = None
    for line in code.split("\n"):
        if "Aer.get_backend" in line:
            backend_line = line.strip()
            break
    if backend_line:
        backend = backend_line.split("(")[1].split(")")[0].strip("\"'")
    else:
        backend = "ibmq_lima"

    predict(json_obj, backend)
    return json.dumps(json_obj), backend


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
            if file_path.endswith(".py") and file_path != os.path.abspath(__file__):
                json_data, backend = convert_to_json(file_path)
                if json_data:
                    json_file_path = os.path.join(json_dir, file.replace(".py", ".json"))
                    with open(json_file_path, "w") as f:
                        f.write(json_data)
                    with open(json_file_path) as f:
                        print(f.read())
                    print(f"The backend for {json_file_path} is {backend}")
                    


