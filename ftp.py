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
base_directory = "docs/"

# Ejecutar la función para renombrar archivos y directorios recursivamente
ftp_rename_files(ftp, base_directory)

# Cerrar la conexión FTP
ftp.quit()
