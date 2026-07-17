# 🛡️ File Security Analyzer

Herramienta de análisis forense ligero para la identificación de archivos mediante verificación de firmas (Magic Bytes) y hashing.

## ⚠️ Aviso de Seguridad (Disclaimer)
Este proyecto es una herramienta de **análisis estático**. 
* **No realiza análisis dinámico:** No ejecuta el código ni detecta virus polimórficos de forma conductual.
* **Uso responsable:** Utilízalo para identificar discrepancias entre la extensión de un archivo y su contenido real.
* **No garantizamos inmunidad:** Ninguna herramienta local de este tipo sustituye a un antivirus con base de datos de firmas actualizada.

## 🚀 Características
* **Detección por firma:** Ignora la extensión y lee los bytes reales del archivo.
* **Detección de "Discrepancias de Extensión":** Alerta si un ejecutable `.exe` se disfraza de otra extensión.
* **Integridad:** Genera un hash SHA-256 para verificar la unicidad del archivo.
