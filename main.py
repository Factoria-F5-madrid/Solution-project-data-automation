# main.py
# Script principal para ejecutar ETL completo + Dashboard

import sys
import os
from datetime import datetime
from pathlib import Path

# Agregar la carpeta src al path de Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.sakila_etl import proceso_completo
from src.dashboard_excel import crear_dashboard
from src.config import EXCEL_FILE, AUTO_OPEN_EXCEL, OUTPUT_FOLDER

def ejecutar_proceso_completo():
    """Ejecutar proceso ETL completo + generación de Excel con múltiples hojas"""
    print("🚀 Iniciando automatización de datos Sakila")
    print("=" * 60)
    
    # Ejecutar ETL + Generar/Actualizar archivos
    exito = crear_dashboard()
    
    if exito:
        print("\n" + "="*60)
        print("✅ Proceso completado exitosamente")
        print("="*60)
        print("\n📁 ARCHIVOS:")
        print("   • output/datos_sakila.csv - Datos actualizados")
        print("   • dashboard/dashboard_sakila.xlsx - Dashboard Excel")
        print("\n🔄 SIGUIENTE:")
        print("   1. Abre Excel")
        print("   2. Presiona F5 para actualizar")
        print("="*60)
    else:
        print("\n❌ Error en el proceso")
    
    print("\n")
    input("Presiona ENTER para salir...")

if __name__ == "__main__":
    try:
        ejecutar_proceso_completo()
    except KeyboardInterrupt:
        print("\n\n⚠️  Proceso interrumpido por el usuario")
    except Exception as e:
        print(f"\n\n❌ Error inesperado: {e}")
        print("📖 Ver: README.md para troubleshooting")
    finally:
        input("\n\nPresiona ENTER para salir...")
