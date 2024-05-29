# FTP Rename Files Script

Este script se conecta a un servidor FTP, navega a un directorio específico y renombra recursivamente todos los archivos y directorios dentro de ese directorio, reemplazando los espacios en blanco en los nombres con guiones bajos.

## Requisitos

- Python 3.x
- Biblioteca `ftplib` (incluida en la biblioteca estándar de Python)

## Uso

1. Clona este repositorio o descarga el archivo del script.
2. Asegúrate de tener Python instalado en tu sistema.
3. Modifica las credenciales FTP y el directorio base según sea necesario.
4. Ejecuta el script.

## Código

```python
from ftplib import FTP
import os

def ftp_rename_files(ftp, directory):
    try:
        # Cambiar al directorio especificado
        ftp.cwd(directory)
    except Exception as e:
        print(f"Error al cambiar al directorio {directory}: {e}")
        return
    
    # Obtener la lista de archivos y directorios en el directorio actual
    files = ftp.nlst()

    # Iterar sobre cada archivo o directorio
    for file in files:
        # Reemplazar espacios en blanco con guiones bajos en el nombre del archivo o directorio
        new_name = file.replace(" ", "_")
        
        # Renombrar el archivo o directorio
        try:
            ftp.rename(file, new_name)
            print(f"Renombrado {file} a {new_name}")
        except Exception as e:
            print(f"No se pudo renombrar {file} a {new_name}: {e}")
        
        # Verificar si es un directorio
        if "." not in file:
            # Si es un directorio, recorrer recursivamente
            ftp_rename_files(ftp, new_name)
```
# Credenciales FTP
FTP_USERNAME = ""
FTP_PASSWORD = ""
FTP_SERVER = ""
FTP_PORT = 21

# Conexión al servidor FTP
ftp = FTP()
ftp.connect(FTP_SERVER, FTP_PORT)
ftp.login(user=FTP_USERNAME, passwd=FTP_PASSWORD)

# Directorio base
base_directory = "docs/directorio"

# Ejecutar la función para renombrar archivos y directorios recursivamente
ftp_rename_files(ftp, base_directory)

# Cerrar la conexión FTP
ftp.quit()

## Explicación del Código

### Importaciones
El script importa la biblioteca `ftplib` y `os`.

### Función `ftp_rename_files`
- Cambia al directorio especificado en el servidor FTP.
- Obtiene la lista de archivos y directorios en el directorio actual.
- Itera sobre cada archivo o directorio:
  - Reemplaza espacios en blanco con guiones bajos en el nombre.
  - Renombra el archivo o directorio en el servidor FTP.
  - Si es un directorio, llama a la función recursivamente para procesar su contenido.

### Credenciales FTP
Se especifican las credenciales para conectar al servidor FTP.

### Conexión al Servidor FTP
El script se conecta al servidor FTP y realiza el login.

### Ejecución de la Función
Se llama a la función `ftp_rename_files` para renombrar archivos y directorios en el directorio base especificado.

### Cierre de la Conexión
Se cierra la conexión al servidor FTP.

### Notas
- Asegúrate de reemplazar las credenciales y el directorio base por los correctos antes de ejecutar el script.
- El script maneja errores básicos, pero puede ser mejorado para manejar casos específicos más robustamente.
