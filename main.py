import requests # type: ignore

# URL base de la API para generar QR
base_url = "https://api.qrserver.com/v1/create-qr-code/"

# Parámetros para la solicitud (datos a codificar y tamaño del QR)
params = {
    'data': 'https://www.example.com',  # Cambia esta URL por el contenido que quieras codificar
    'size': '300x300'  # Tamaño del QR (en píxeles)
}

password = "e55532a9-0e22-45c1-b704-246c02daf3dd"

# Hacer la solicitud GET a la API
response = requests.get(base_url, params=params)

# Guardar la imagen del QR en un archivo
if response.status_code == 200:
    with open("qr_code.png", "wb") as f:
        f.write(response.content)
        print("Código QR guardado como qr_code.png")
else:
    print(f"Error al generar el QR: {response.status_code}")