# inicio_rapido.py
"""
Script de inicio rápido para estudiantes
Configura todo automáticamente
"""

import sys
import subprocess
import os

def titulo(texto):
    """Mostrar título formateado"""
    print("\n" + "="*60)
    print(f"  {texto}")
    print("="*60)

def paso(numero, texto):
    """Mostrar paso formateado"""
    print(f"\n📌 PASO {numero}: {texto}")
    print("-"*60)

def ejecutar_comando(comando, descripcion):
    """Ejecutar comando y mostrar resultado"""
    print(f"⚙️  {descripcion}...")
    try:
        subprocess.check_call(comando, shell=True)
        print("✓ Completado")
        return True
    except:
        print("❌ Error")
        return False

def verificar_python():
    """Verificar versión de Python"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor} detectado")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor} es muy antiguo")
        print("   Necesitas Python 3.8 o superior")
        return False

def instalar_dependencias():
    """Instalar dependencias de Python"""
    print("📦 Instalando librerías de Python...")
    return ejecutar_comando(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Instalando pandas, mysql-connector, sqlalchemy, openpyxl"
    )

def crear_carpetas():
    """Crear carpetas necesarias"""
    print("📁 Creando carpetas...")
    os.makedirs("output", exist_ok=True)
    print("✓ Carpeta 'output/' creada")

def crear_excel():
    """Crear archivo Excel básico"""
    print("📊 Creando plantilla de Excel...")
    return ejecutar_comando(
        f"{sys.executable} crear_excel_basico.py",
        "Generando Sakila_Dashboard.xlsx"
    )

def verificar_mysql():
    """Intentar conectar a MySQL"""
    print("🔍 Verificando conexión a MySQL...")
    try:
        from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
        import mysql.connector
        
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        conn.close()
        print("✓ Conexión a MySQL exitosa")
        print(f"  Base de datos: {DB_NAME}")
        return True
    except Exception as e:
        print(f"⚠️  No se pudo conectar a MySQL")
        print(f"  Error: {e}")
        print("\n  💡 Edita config.py con tus credenciales:")
        print("     DB_USER = 'tu_usuario'")
        print("     DB_PASSWORD = 'tu_contraseña'")
        return False

def main():
    """Proceso de configuración completo"""
    titulo("🚀 CONFIGURACIÓN AUTOMÁTICA PARA ESTUDIANTES")
    
    print("\nEste script configurará todo lo necesario para tu proyecto.")
    input("Presiona ENTER para continuar...")
    
    # Paso 1: Verificar Python
    paso(1, "Verificando Python")
    if not verificar_python():
        print("\n❌ Actualiza Python antes de continuar")
        return
    
    # Paso 2: Instalar dependencias
    paso(2, "Instalando dependencias")
    if not instalar_dependencias():
        print("\n⚠️  Hubo problemas instalando las dependencias")
        print("   Intenta manualmente: pip install -r requirements_simple.txt")
        return
    
    # Paso 3: Crear carpetas
    paso(3, "Creando estructura de carpetas")
    crear_carpetas()
    
    # Paso 4: Crear Excel
    paso(4, "Creando plantilla de Excel")
    crear_excel()
    
    # Paso 5: Verificar MySQL
    paso(5, "Verificando conexión a MySQL")
    mysql_ok = verificar_mysql()
    
    # Resumen final
    titulo("✅ CONFIGURACIÓN COMPLETADA")
    
    print("\n📋 Estado del proyecto:")
    print("   ✓ Python instalado y verificado")
    print("   ✓ Dependencias instaladas")
    print("   ✓ Carpeta 'output/' creada")
    print("   ✓ Archivo Excel creado")
    
    if mysql_ok:
        print("   ✓ Conexión a MySQL funcional")
    else:
        print("   ⚠️  Configura MySQL en config_simple.py")
    
    print("\n" + "="*60)
    print("🎯 PRÓXIMOS PASOS:")
    print("="*60)
    
    if not mysql_ok:
        print("\n1. Edita config.py con tus credenciales de MySQL")
        print("2. Ejecuta: python sakila_automation.py")
    else:
        print("\n1. Ejecuta: python sakila_automation.py")
        print("2. Abre Sakila_Dashboard.xlsx")
        print("3. Importa los CSV y crea tus gráficos")
    
    print("\n📚 Lee README.md para más ayuda")
    print("\n¡Listo para comenzar! 🎉\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Configuración cancelada por el usuario")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
    
    input("\nPresiona ENTER para salir...")
