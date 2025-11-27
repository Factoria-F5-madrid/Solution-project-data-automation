# 📊 Proyecto Sakila - Automatización MySQL → Python → Excel

Automatiza el análisis de la base de datos Sakila: extrae datos de MySQL, los transforma con Python/Pandas y genera archivos CSV listos para visualizar en Excel.

---

## 🚀 INICIO RÁPIDO (3 pasos)

```powershell
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Configurar MySQL
# Edita el archivo .env con tus credenciales

# 3. Ejecutar (cualquiera de los dos)
python sakila_automation.py
# o
python main.py
```

---

## 📁 Estructura del Proyecto

```
project-data-automation/
├── sakila_automation.py       ⭐ EJECUTAR ESTE (wrapper)
├── main.py                    (o este - lógica principal)
├── sakila_etl.py              (Lógica ETL)
├── config.py                  (Lee configuración de .env)
├── requirements.txt           (Dependencias)
├── .env                       🔒 CONFIGURAR AQUÍ (credenciales)
├── .env.example               (Plantilla de .env)
├── .gitignore                 (Archivos a ignorar en Git)
├── crear_excel_basico.py      (Opcional: crea plantilla Excel)
├── inicio_rapido.py           (Opcional: instalador automático)
├── README.md                  (Esta guía)
├── Sakila_Dashboard.xlsx      (Crear este archivo)
└── output/                    (Archivos CSV generados)
```

**Total: 8 archivos Python + 4 archivos config + 1 carpeta**

**🔒 IMPORTANTE:** El archivo `.env` contiene tus credenciales y NO se sube a Git (está en `.gitignore`)

---

## ⚙️ CONFIGURACIÓN

### 1. Instalar Python y MySQL
- Python 3.8 o superior
- MySQL con base de datos Sakila instalada

### 2. Instalar dependencias
```powershell
pip install -r requirements.txt
```

Esto instala:
```powershell
pip install pandas mysql-connector-python sqlalchemy openpyxl python-dotenv
```

### 3. Configurar MySQL (IMPORTANTE)

Edita el archivo **`.env`** con tus credenciales:

```env
DB_USER=root
DB_PASSWORD=tu_contraseña_mysql
DB_HOST=localhost
DB_PORT=3306
DB_NAME=sakila
```

**¿Dónde encontrar estos datos?**
- `DB_USER`: Usuario de MySQL (generalmente `root`)
- `DB_PASSWORD`: La contraseña que pusiste al instalar MySQL
- `DB_HOST`: `localhost` (si MySQL está en tu PC)
- `DB_NAME`: `sakila` (nombre de la base de datos)

**🔒 SEGURIDAD:** El archivo `.env` NO se sube a Git (protegido por `.gitignore`)

### 4. Crear Dashboard Excel
**Opción A - Automático:**
```powershell
python crear_excel_basico.py
```

**Opción B - Manual:**
- Crear archivo: `Sakila_Dashboard.xlsx` en la carpeta del proyecto
- Agregar 4 hojas: Dashboard, Datos Diarios, Top Peliculas, Por Categoria

---

## 🎯 USO

### Ejecutar el proceso completo:
```powershell
python sakila_automation.py
```

**Esto hará:**
1. ✅ Extrae datos de MySQL (base Sakila)
2. ✅ Transforma y analiza con Pandas
3. ✅ Genera 3 archivos CSV en `output/`
4. ✅ Abre Excel automáticamente

### Archivos generados:
- `output/resumen_diario.csv` - Ingresos, clientes y rentas por día
- `output/top_peliculas.csv` - Las 20 películas más rentables
- `output/por_categoria.csv` - Análisis por categoría de película

---

## 📊 DASHBOARD DE EXCEL

### Ubicación recomendada:
```
project-data-automation/
└── Sakila_Dashboard.xlsx  ← Mismo nivel que main.py
```

También puedes cambiarlo en el archivo **`.env`**:
```env
EXCEL_FILE=Sakila_Dashboard.xlsx
```

### 4 hojas necesarias:

1. **Dashboard** - Tus gráficos y análisis visual
2. **Datos Diarios** - Importar `resumen_diario.csv`
3. **Top Peliculas** - Importar `top_peliculas.csv`
4. **Por Categoria** - Importar `por_categoria.csv`

### Importar CSV en Excel:
1. Datos → Obtener datos → De archivo → De texto/CSV
2. Seleccionar el archivo CSV de la carpeta `output/`
3. Cargar los datos

### Crear gráficos:
- **Gráfico 1:** Línea temporal de ingresos (Datos Diarios)
- **Gráfico 2:** Top 10 películas - barras (Top Peliculas)
- **Gráfico 3:** Ingresos por categoría - circular (Por Categoria)

### Actualizar datos:
Después de ejecutar `python sakila_automation.py`, en Excel:
- Click derecho en tabla dinámica → **Actualizar**
- O presiona: **Alt + F5**

---

## 🔄 FLUJO DEL PROYECTO

```
MySQL (Sakila DB)
    ↓
Python: sakila_automation.py
    ↓
├─ Extrae datos (sakila_etl.py)
├─ Transforma con Pandas
└─ Genera CSV
    ↓
output/
├─ resumen_diario.csv
├─ top_peliculas.csv
└─ por_categoria.csv
    ↓
Excel Dashboard
└─ Visualización con gráficos
```

---

## 🛠️ INSTALACIÓN AUTOMÁTICA (OPCIONAL)

Si quieres que todo se configure automáticamente:

```powershell
python inicio_rapido.py
```

Esto:
- ✅ Verifica Python
- ✅ Instala dependencias
- ✅ Crea carpeta `output/`
- ✅ Genera plantilla de Excel
- ✅ Verifica conexión a MySQL

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### ❌ Error: "Can't connect to MySQL"
```powershell
# Verificar que MySQL está corriendo
Get-Service MySQL*

# Si no está activo, iniciarlo
Start-Service MySQL80
```
- Verifica usuario/contraseña en archivo **`.env`**
- Asegúrate que la base de datos Sakila esté instalada
- Prueba las credenciales en MySQL Workbench primero

### ❌ Error: "ModuleNotFoundError"
```powershell
pip install -r requirements.txt
```

### ❌ Excel no abre
- Verifica que existe `Sakila_Dashboard.xlsx`
- Cambia la ruta en archivo **`.env`** si está en otra ubicación

### ❌ Archivos CSV vacíos
- Revisa que la base de datos Sakila tenga datos
- Verifica la conexión a MySQL

---

## 📦 QUÉ CONTIENE CADA ARCHIVO

| Archivo | Descripción |
|---------|-------------|
| `sakila_automation.py` | Script principal - EJECUTAR ESTE (llama a main.py) |
| `main.py` | Lógica principal del proceso (también ejecutable) |
| `sakila_etl.py` | Lógica ETL: extrae, transforma y guarda datos |
| `config.py` | Lee configuración desde .env |
| `.env` | 🔒 CREDENCIALES (NO subir a Git) |
| `.env.example` | Plantilla para crear tu .env |
| `.gitignore` | Archivos que Git debe ignorar |
| `requirements.txt` | Lista de dependencias Python (5 librerías) |
| `crear_excel_basico.py` | Opcional: crea plantilla de Excel |
| `inicio_rapido.py` | Opcional: instalador automático |

---

## 🎓 PARA ENTREGAR TU PROYECTO

Incluye:
1. ✅ Carpeta completa del proyecto (todos los archivos .py)
2. ✅ `Sakila_Dashboard.xlsx` con gráficos creados
3. ✅ Captura de pantalla del dashboard
4. ✅ Archivos CSV de ejemplo en `output/`
5. ✅ Este README.md

---

## 📝 DATOS GENERADOS

### 1. Resumen Diario
| Fecha | Ingresos | Clientes | Rentas |
|-------|----------|----------|--------|
| 2005-05-24 | $234.53 | 45 | 89 |

### 2. Top Películas
| Película | Ingresos | Total Rentas |
|----------|----------|--------------|
| BUCKET BROTHERHOOD | $105.78 | 34 |

### 3. Por Categoría
| Categoría | Ingresos | Total Rentas |
|-----------|----------|--------------|
| Sports | $4,892.19 | 1,179 |

---

## ✅ Checklist de Instalación

- [ ] Python 3.8+ instalado
- [ ] MySQL instalado y corriendo
- [ ] Base de datos Sakila instalada
- [ ] `pip install -r requirements.txt` ejecutado
- [ ] Archivo `.env` creado y configurado con tus credenciales
- [ ] `Sakila_Dashboard.xlsx` creado
- [ ] `python sakila_automation.py` ejecutado sin errores
- [ ] Archivos CSV generados en `output/`
- [ ] Gráficos creados en Excel

---

## 💡 TIPS

- **Portable:** Toda la carpeta es portable, cópiala y funciona
- **Simple:** Solo 7 archivos Python esenciales
- **Rápido:** Ejecuta `python sakila_automation.py` y listo
- **Educativo:** Código comentado y fácil de entender
- **Profesional:** Estructura limpia y organizada

---

## 📚 Recursos

- [Base de datos Sakila](https://dev.mysql.com/doc/sakila/en/) - Documentación oficial
- [Pandas](https://pandas.pydata.org/docs/) - Documentación
- [SQLAlchemy](https://docs.sqlalchemy.org/) - Documentación

---

**¡Listo para automatizar! 🚀**

*Proyecto simplificado para estudiantes - Sin complicaciones*
