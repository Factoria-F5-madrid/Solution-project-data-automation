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
    print("🚀 Iniciando proceso completo ETL + Excel Multi-Hojas")
    print("=" * 60)
    
    # Ejecutar proceso completo (ETL + Excel)
    print("PASO ÚNICO: Ejecutando ETL + Generando Excel...")
    
    try:
        from src.dashboard_excel import crear_dashboard
        if crear_dashboard():
            print("\n🎉 Proceso completo terminado exitosamente!")
            print("📁 Revisa la carpeta 'output' para los archivos generados")
            print("\n📋 ARCHIVOS CREADOS:")
            print("  • datos_sakila.csv - Datos completos en CSV")
            print("  • dashboard_sakila.xlsx - Excel con múltiples hojas de datos")
            print("\n🎯 SIGUIENTE PASO:")
            print("  1. Abre dashboard_sakila.xlsx")
            print("  2. Diseña tu dashboard manualmente usando las hojas disponibles")
            print("  3. Para actualizar datos: ejecuta 'python main.py' nuevamente")
            print("  4. Tu diseño se mantendrá, solo se actualizarán los datos")
        else:
            print("❌ Error en el proceso")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    return True

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
