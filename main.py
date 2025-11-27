# main.py
# Script principal para automatización Sakila
import os
import subprocess
from datetime import datetime
from sakila_etl import proceso_completo
from config import EXCEL_FILE, AUTO_OPEN_EXCEL

def main():
    """Ejecutar automatización completa"""
    print("\n" + "="*50)
    print("🚀 AUTOMATIZACIÓN SAKILA")
    print("="*50)
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # 1. Ejecutar ETL
    print("PASO 1: Procesando datos de MySQL...\n")
    if proceso_completo():
        print("\n✅ Datos procesados exitosamente!")
        
        # 2. Abrir Excel si está configurado
        if AUTO_OPEN_EXCEL:
            print("\nPASO 2: Abriendo Excel...")
            if os.path.exists(EXCEL_FILE):
                os.startfile(EXCEL_FILE)
                print(f"✓ Excel abierto: {EXCEL_FILE}")
                print("\n💡 Ahora actualiza las tablas dinámicas en Excel:")
                print("   1. Click derecho en tabla dinámica")
                print("   2. 'Actualizar' o presiona Alt + F5")
            else:
                print(f"\n⚠️  Archivo Excel no encontrado: {EXCEL_FILE}")
                print("   Crea el archivo Excel y vuelve a ejecutar")
        
        print("\n" + "="*50)
        print("✅ PROCESO COMPLETADO")
        print("="*50)
        print("\n📂 Archivos generados en carpeta 'output/':")
        print("   • resumen_diario.csv")
        print("   • top_peliculas.csv")
        print("   • por_categoria.csv")
        
    else:
        print("\n❌ Hubo un error en el proceso")
        print("Verifica tu conexión a MySQL en config_simple.py")

if __name__ == "__main__":
    main()
    input("\nPresiona ENTER para salir...")
