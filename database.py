import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Entrada no confiable del usuario
user_input = input("Ingrese el nombre de usuario: ")

# Consulta vulnerable a inyección SQL
query = f"SELECT * FROM users WHERE username = '{user_input}'"

# Ejecutar la consulta
cursor.execute(query)

# Obtener los resultados
rows = cursor.fetchall()

for row in rows:
    print(row)

# Cerrar la conexión
conn.close()
