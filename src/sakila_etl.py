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
    """Transformar y limpiar datos principales + crear datasets para tablas dinámicas"""
    print("🔄 Transformando datos...")
    
    # Dataset principal con columnas adicionales
    df['nombre_completo'] = df['cliente']
    df['año_renta'] = pd.to_datetime(df['fecha_renta']).dt.year
    df['mes_renta'] = pd.to_datetime(df['fecha_renta']).dt.month
    df['dia_semana'] = pd.to_datetime(df['fecha_renta']).dt.day_name()
    df['estado_cliente'] = df['active'].map({1: 'Activo', 0: 'Inactivo'})
    
    # 1. Resumen por fechas (para gráfico temporal)
    resumen_fechas = df.groupby('fecha_renta').agg({
        'monto': 'sum',
        'customer_id': ['nunique', 'count']
    }).reset_index()
    resumen_fechas.columns = ['Fecha', 'Ingresos_Total', 'Clientes_Unicos', 'Transacciones']
    
    # 2. Análisis por país
    por_pais = df.groupby('country').agg({
        'monto': ['sum', 'mean', 'count'],
        'customer_id': 'nunique'
    }).reset_index()
    por_pais.columns = ['Pais', 'Ingresos_Total', 'Ingreso_Promedio', 'Total_Transacciones', 'Clientes_Unicos']
    por_pais = por_pais.sort_values('Ingresos_Total', ascending=False)
    
    # 3. Análisis por ciudad (top 20)
    por_ciudad = df.groupby(['country', 'city']).agg({
        'monto': ['sum', 'mean'],
        'customer_id': 'nunique'
    }).reset_index()
    por_ciudad.columns = ['Pais', 'Ciudad', 'Ingresos_Total', 'Ingreso_Promedio', 'Clientes_Unicos']
    por_ciudad = por_ciudad.sort_values('Ingresos_Total', ascending=False).head(20)
    
    # 4. Análisis de clientes
    clientes_resumen = df.groupby(['customer_id', 'nombre_completo', 'country', 'city', 'estado_cliente']).agg({
        'monto': ['sum', 'mean', 'count']
    }).reset_index()
    clientes_resumen.columns = ['Customer_ID', 'Cliente', 'Pais', 'Ciudad', 'Estado', 'Total_Gastado', 'Gasto_Promedio', 'Num_Transacciones']
    clientes_resumen = clientes_resumen.sort_values('Total_Gastado', ascending=False)
    
    # 5. Análisis temporal (por mes/año)
    df['mes_año'] = pd.to_datetime(df['fecha_renta']).dt.to_period('M').astype(str)
    por_mes = df.groupby('mes_año').agg({
        'monto': 'sum',
        'customer_id': ['nunique', 'count']
    }).reset_index()
    por_mes.columns = ['Mes_Año', 'Ingresos_Total', 'Clientes_Unicos', 'Transacciones']
    
    print("✓ Datos transformados con 5 datasets listos para Excel")
    return df, resumen_fechas, por_pais, por_ciudad, clientes_resumen, por_mes

def guardar_archivos(df_principal):
    """Guardar archivo CSV principal"""
    print("💾 Guardando archivo principal...")
    
    # Crear carpeta si no existe
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    # Guardar CSV principal
    df_principal.to_csv(f'{OUTPUT_FOLDER}/datos_sakila.csv', index=False)
    
    print(f"✓ Archivo principal guardado en '{OUTPUT_FOLDER}/datos_sakila.csv'")
    return True

def proceso_completo():
    """Ejecutar proceso ETL completo"""
    try:
        # Extraer
        df = extraer_datos()
        
        # Transformar
        df_transformado, resumen_fechas, por_pais, por_ciudad, clientes_resumen, por_mes = transformar_datos(df)
        
        # Guardar CSV principal
        guardar_archivos(df_transformado)
        
        # Retornar todos los datasets para el dashboard
        return {
            'datos_principales': df_transformado,
            'resumen_fechas': resumen_fechas,
            'por_pais': por_pais,
            'por_ciudad': por_ciudad,
            'clientes_resumen': clientes_resumen,
            'por_mes': por_mes
        }
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    proceso_completo()
