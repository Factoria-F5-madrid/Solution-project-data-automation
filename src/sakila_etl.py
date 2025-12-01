# src/sakila_etl.py
# Proceso ETL para base de datos Sakila
import pandas as pd
from sqlalchemy import create_engine
import os
from .config import *

def conectar_bd():
    """Crear conexión a la base de datos"""
    url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    engine = create_engine(url)
    return engine

def extraer_datos():
    """Extraer datos de MySQL"""
    print("📥 Extrayendo datos de MySQL...")
    
    engine = conectar_bd()
    
    # Query para análisis de clientes
    query = """
    SELECT 
        c.customer_id,
        CONCAT(c.first_name, ' ', c.last_name) as cliente,
        c.email,
        c.active,
        a.address,
        a.district,
        a.postal_code,
        ci.city,
        co.country,
        DATE(r.rental_date) as fecha_renta,
        DATE(r.return_date) as fecha_devolucion,
        p.amount as monto,
        DATE(p.payment_date) as fecha_pago
    FROM customer c
    JOIN address a ON c.address_id = a.address_id
    JOIN city ci ON a.city_id = ci.city_id
    JOIN country co ON ci.country_id = co.country_id
    JOIN rental r ON c.customer_id = r.customer_id
    JOIN payment p ON p.rental_id = r.rental_id
    """   
    df = pd.read_sql(query, engine)
    print(f"✓ {len(df)} registros extraídos")
    return df

def transformar_datos(df):
    """Transformar y limpiar datos"""
    print("🔄 Transformando datos...")
    
    # Agregar columnas útiles
    df['nombre_completo'] = df['cliente']
    df['año_renta'] = pd.to_datetime(df['fecha_renta']).dt.year
    df['mes_renta'] = pd.to_datetime(df['fecha_renta']).dt.month
    df['dia_semana'] = pd.to_datetime(df['fecha_renta']).dt.day_name()
    df['estado_cliente'] = df['active'].map({1: 'Activo', 0: 'Inactivo'})
    df['mes_año'] = pd.to_datetime(df['fecha_renta']).dt.to_period('M').astype(str)
    
    print("✓ Datos transformados correctamente")
    return df

def guardar_csv(df):
    """Guardar archivo CSV principal"""
    print("💾 Guardando CSV...")
    
    # Crear carpeta si no existe
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    # Guardar CSV
    df.to_csv(f'{OUTPUT_FOLDER}/datos_sakila.csv', index=False, encoding='utf-8-sig')
    
    print(f"✓ CSV guardado en '{OUTPUT_FOLDER}/datos_sakila.csv'")
    return True

def proceso_completo():
    """Ejecutar proceso ETL completo"""
    try:
        # Extraer
        df = extraer_datos()
        
        # Transformar
        df_transformado = transformar_datos(df)
        
        # Guardar CSV principal
        guardar_csv(df_transformado)
        
        # Retornar dataset para el dashboard
        return {
            'datos_principales': df_transformado
        }
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    proceso_completo()
