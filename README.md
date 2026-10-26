# 🛡️ FSA · File Security Analyzer

Herramienta ligera de análisis estático que identifica el tipo **real** de un archivo leyendo sus *magic bytes* (ignora la extensión), detecta ejecutables disfrazados y calcula su hash SHA-256.

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-informational)

## 🚀 Características

- **Detección por firma:** lee la cabecera del archivo y la compara con una tabla de firmas conocidas (JPEG, PNG, PDF, ZIP/DOCX/JAR, EXE, ELF, Java CLASS).
- **Discrepancia de extensión:** alerta si un ejecutable de Windows (`MZ`) tiene una extensión distinta de `.exe`.
- **Integridad:** hash SHA-256 por bloques (válido para archivos grandes), útil para buscarlo en VirusTotal u otras bases de IOCs.

## 🛠️ Instalación

```bash
git clone https://github.com/CeroCincoSiete/F.S.A-File-Security-Analyzer.git
cd F.S.A-File-Security-Analyzer
pip install -r requirements.txt
```

## ▶️ Uso

```bash
python main.py
# Introduce la ruta del archivo a analizar: /ruta/a/factura.pdf
```

La herramienta muestra una tabla con la firma detectada, la extensión del archivo y el hash, y una alerta en rojo si hay un ejecutable oculto.

## 📁 Estructura

```
├── main.py         # Interfaz (Rich) y lógica de alerta
├── scanner.py      # Lectura de cabecera y cálculo de SHA-256
├── signatures.py   # Tabla de magic bytes
└── requirements.txt
```

## 🗺️ Próximos pasos

- [ ] Ampliar la tabla de firmas (RAR, 7z, GZIP, MSI, LNK, ISO…).
- [ ] Extender la alerta de discrepancia a ELF y otros ejecutables.
- [ ] Argumento por CLI (`python main.py <archivo>`) y análisis de carpetas.
- [ ] Consulta opcional del hash en la API de VirusTotal.

## ⚠️ Aviso

Es una herramienta de **análisis estático**: no ejecuta el archivo ni detecta malware por comportamiento. No sustituye a un antivirus actualizado.

## 📜 Licencia

MIT
