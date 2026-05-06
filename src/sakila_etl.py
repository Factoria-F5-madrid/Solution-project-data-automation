# src/sakila_etl.py
# Proceso ETL para base de datos Sakila
# Arquitectura: cada consulta SQL vive en queries/*.sql
# Python solo orquesta: conecta, ejecuta, guarda CSV.
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
import os
from .config import *

# Carpeta de queries relativa a la raíz del proyecto
QUERIES_DIR = Path(__file__).parent.parent / 'queries'

# Mapeo: nombre_de_archivo_sql → nombre_de_archivo_csv
CONSULTAS = {
    'resumen_diario.sql': 'resumen_diario.csv',
    'top_peliculas.sql':  'top_peliculas.csv',
    'por_categoria.sql':  'por_categoria.csv',
    'por_tienda.sql':     'por_tienda.csv',
}

def conectar_bd():
    """Crear conexión a la base de datos"""
    url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    engine = create_engine(url)
    return engine

def extraer_datos(engine):
    """
    Ejecuta cada archivo .sql de CONSULTAS y devuelve un diccionario
    {nombre_csv: DataFrame}.
    SQL hace la agregación; Python solo recibe resultados listos.
    """
    print("📥 Extrayendo datos de MySQL...")

    resultados = {}
    for archivo_sql, archivo_csv in CONSULTAS.items():
        ruta_sql = QUERIES_DIR / archivo_sql
        query = ruta_sql.read_text(encoding='utf-8')
        df = pd.read_sql(query, engine)
        resultados[archivo_csv] = df
        print(f"  ✓ {archivo_sql} → {len(df)} filas")

    return resultados

def guardar_archivos(resultados):
    """Guarda cada DataFrame como CSV en la carpeta output/"""
    print("💾 Guardando archivos...")

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for archivo_csv, df in resultados.items():
        df.to_csv(f'{OUTPUT_FOLDER}/{archivo_csv}', index=False)
        print(f"  ✓ {archivo_csv}")

    print(f"✓ Archivos guardados en carpeta '{OUTPUT_FOLDER}/'")
    return True

def proceso_completo():
    """Ejecutar proceso ETL completo"""
    try:
        engine = conectar_bd()

        # Extraer: SQL agrupa y filtra, Python recibe resultados
        resultados = extraer_datos(engine)

        # Guardar: un CSV por cada consulta
        guardar_archivos(resultados)

        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    proceso_completo()
