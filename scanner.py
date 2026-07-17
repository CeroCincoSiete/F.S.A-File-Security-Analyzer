import hashlib
import os
from signatures import SIGNATURES

def get_file_hash(file_path):
    """Genera un hash SHA-256 para verificar si el archivo es conocido."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def analyze_file(file_path):
    """Compara la extensión real vs la firma detectada."""
    ext_detectada = os.path.splitext(file_path)[1].lower().replace('.', '')
    
    with open(file_path, "rb") as f:
        header = f.read(4).hex().upper()
    
    # Buscar firma (probando diferentes longitudes)
    file_type = "Desconocido"
    for sig, name in SIGNATURES.items():
        if header.startswith(sig):
            file_type = name
            break
            
    return file_type, ext_detectada
