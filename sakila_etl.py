# sakila_etl.py
# Proceso ETL para base de datos Sakila
import pandas as pd
from sqlalchemy import create_engine
import os
from config import *

def conectar_bd():
    """Crear conexión a la base de datos"""
    url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    engine = create_engine(url)
    return engine

def extraer_datos():
    """Extraer datos de MySQL"""
    print("📥 Extrayendo datos de MySQL...")
    
    engine = conectar_bd()
    
    # Query simplificada
    query = """
    SELECT 
        DATE(r.rental_date) as fecha_renta,
        c.customer_id,
        CONCAT(c.first_name, ' ', c.last_name) as cliente,
        f.title as pelicula,
        cat.name as categoria,
        p.amount as monto,
        s.store_id as tienda
    FROM rental r
    JOIN payment p ON r.rental_id = p.rental_id
    JOIN customer c ON r.customer_id = c.customer_id
    JOIN inventory i ON r.inventory_id = i.inventory_id
    JOIN film f ON i.film_id = f.film_id
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category cat ON fc.category_id = cat.category_id
    JOIN store s ON i.store_id = s.store_id
    """
    
    df = pd.read_sql(query, engine)
    print(f"✓ {len(df)} registros extraídos")
    return df

def transformar_datos(df):
    """Transformar y analizar datos"""
    print("🔄 Transformando datos...")
    
    # 1. Resumen diario
    resumen_diario = df.groupby('fecha_renta').agg({
        'monto': 'sum',
        'customer_id': 'nunique',
        'pelicula': 'count'
    }).reset_index()
    resumen_diario.columns = ['Fecha', 'Ingresos', 'Clientes', 'Rentas']
    
    # 2. Top películas
    top_peliculas = df.groupby('pelicula').agg({
        'monto': 'sum',
        'customer_id': 'count'
    }).reset_index()
    top_peliculas.columns = ['Pelicula', 'Ingresos', 'Total_Rentas']
    top_peliculas = top_peliculas.sort_values('Ingresos', ascending=False).head(20)
    
    # 3. Por categoría
    por_categoria = df.groupby('categoria').agg({
        'monto': 'sum',
        'pelicula': 'count'
    }).reset_index()
    por_categoria.columns = ['Categoria', 'Ingresos', 'Total_Rentas']
    
    print("✓ Datos transformados")
    return resumen_diario, top_peliculas, por_categoria

def guardar_archivos(resumen_diario, top_peliculas, por_categoria):
    """Guardar archivos CSV"""
    print("💾 Guardando archivos...")
    
    # Crear carpeta si no existe
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    # Guardar CSVs
    resumen_diario.to_csv(f'{OUTPUT_FOLDER}/resumen_diario.csv', index=False)
    top_peliculas.to_csv(f'{OUTPUT_FOLDER}/top_peliculas.csv', index=False)
    por_categoria.to_csv(f'{OUTPUT_FOLDER}/por_categoria.csv', index=False)
    
    print(f"✓ Archivos guardados en carpeta '{OUTPUT_FOLDER}/'")
    return True

def proceso_completo():
    """Ejecutar proceso ETL completo"""
    try:
        # Extraer
        df = extraer_datos()
        
        # Transformar
        resumen_diario, top_peliculas, por_categoria = transformar_datos(df)
        
        # Guardar
        guardar_archivos(resumen_diario, top_peliculas, por_categoria)
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    proceso_completo()
