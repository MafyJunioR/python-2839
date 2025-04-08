import zipfile

# Lista de archivos a comprimir
archivos = ["argumentos.py", "argumentos2.py"]

# Nombre del archivo ZIP a crear
nombre_zip = "ejemplo.zip"

# Crear el archivo ZIP
with zipfile.ZipFile(nombre_zip, "w") as zipf:
    for archivo in archivos:
        zipf.write(archivo)

print(f"Archivo ZIP '{nombre_zip}' creado exitosamente.")