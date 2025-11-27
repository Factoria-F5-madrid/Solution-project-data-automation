# config.py
# Configuración del proyecto - Lee variables desde .env
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# === CONFIGURACIÓN DE BASE DE DATOS ===
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '3306')
DB_NAME = os.getenv('DB_NAME', 'sakila')

# === CONFIGURACIÓN DE ARCHIVOS ===
EXCEL_FILE = os.getenv('EXCEL_FILE', 'Sakila_Dashboard.xlsx')
OUTPUT_FOLDER = os.getenv('OUTPUT_FOLDER', 'output')

# === CONFIGURACIÓN DE AUTOMATIZACIÓN ===
AUTO_OPEN_EXCEL = os.getenv('AUTO_OPEN_EXCEL', 'true').lower() == 'true'
