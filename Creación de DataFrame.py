import pandas as pd

# Crear un diccionario con datos
datos = {
    "nombre": ["María", "Luis", "Carmen", "Antonio"],
    "edad": [18, 22, 20, 21],
    "grado": ["Economía", "Medicina", "Arquitectura", "Economía"],
    "correo": [
        "maria@gmail.com",
        "luis@yahoo.es",
        "carmen@gmail.com",
        "antonio@gmail.com",
    ],
}

# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(datos)

# Mostrar el DataFrame
print("DataFrame creado desde un diccionario de listas:")
print(df)