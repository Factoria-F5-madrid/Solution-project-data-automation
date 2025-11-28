# 📊 Proyecto Sakila - Automatización MySQL → Python → Excel

Automatiza el análisis de la base de datos Sakila: extrae datos de MySQL, los transforma con Python/Pandas y genera archivos CSV listos para visualizar en Excel.

**✨ Sin macros - Solo Python + Excel con F5**

---

## 📖 Documentación

- **README.md** (este archivo) - Guía completa del proyecto
- **GUIA_RAPIDA.md** - Inicio rápido en 3 pasos
- **GUIA_EXCEL.md** - Cómo crear tu dashboard de Excel sin macros

---

## 🚀 INICIO RÁPIDO (3 pasos)

```powershell
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Configurar MySQL
# Edita el archivo .env con tus credenciales

# 3. Ejecutar
python main.py
```

---

## 📁 Estructura del Proyecto

```
project-data-automation/
│
├── main.py                    ⭐ EJECUTAR ESTE (punto de entrada)
│
├── src/                       📦 Código fuente (procesamiento)
│   ├── __init__.py
│   ├── sakila_etl.py          (extracción y transformación de datos)
│   └── config.py              (configuración desde .env)
│
├── output/                    📂 Datos procesados (CSVs)
│   ├── resumen_diario.csv
│   ├── top_peliculas.csv
│   └── por_categoria.csv
│
├── dashboard/                 📊 Visualización (Excel)
│   ├── Sakila_Dashboard.xlsx  (tu dashboard de Excel)
│   └── README.md              (guía del dashboard)
│
├── docs/                      📚 Documentación
│   ├── GUIA_RAPIDA.md         (inicio rápido - 3 pasos)
│   ├── GUIA_EXCEL.md          (cómo crear dashboard)
│   └── PROYECTO_COMPLETO.md   (resumen del proyecto)
│
├── requirements.txt           (dependencias Python)
├── .env                       🔒 Credenciales (configurado ✓)
├── .env.example               (plantilla)
├── .gitignore                 (protección Git)
└── README.md                  (esta guía)
```

**Organización tipo aplicación:**
- **src/** = Procesamiento (Python)
- **output/** = Datos intermedios (CSVs)
- **dashboard/** = Visualización (Excel)
- **docs/** = Documentación

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

### 4. Crear Dashboard Excel (manualmente)

Crea tu archivo Excel en la carpeta `dashboard/`:

**Ubicación:** `dashboard/Sakila_Dashboard.xlsx`

**💡 Estructura recomendada:** 4 hojas
- `Dashboard` - Aquí pondrás tus gráficos y análisis visual
- `Datos Diarios` - Para conectar `../output/resumen_diario.csv`
- `Top Peliculas` - Para conectar `../output/top_peliculas.csv`
- `Por Categoria` - Para conectar `../output/por_categoria.csv`

**📖 Ver:** `dashboard/README.md` y `docs/GUIA_EXCEL.md` para instrucciones detalladas

---

## 🎯 USO

### Ejecutar el proceso completo:
```powershell
python main.py
```

**Esto hará:**
1. ✅ Extrae datos de MySQL (base Sakila)
2. ✅ Transforma y analiza con Pandas
3. ✅ Genera 3 archivos CSV en `output/`
4. ✅ Abre Excel automáticamente (si está configurado)

### Archivos generados:
- `output/resumen_diario.csv` - Ingresos, clientes y rentas por día
- `output/top_peliculas.csv` - Las 20 películas más rentables
- `output/por_categoria.csv` - Análisis por categoría de película

---

## 📊 DASHBOARD DE EXCEL (Sin Macros - Actualización Manual)

### ✅ Ventajas de este enfoque:
- ✅ **Simple y seguro** - No necesitas habilitar macros
- ✅ **Compatible** - Funciona en Windows, Mac, Excel Online
- ✅ **Fácil de entender** - Los estudiantes ven claramente el proceso
- ✅ **Portable** - Tu Excel funciona en cualquier computadora

### 🔄 Flujo de trabajo:

1. **Ejecutar la automatización:**
   ```powershell
   python sakila_automation.py
   ```
   Esto genera/actualiza los CSVs en la carpeta `output/`

2. **Abrir tu Excel** (o si ya está abierto, seguir al paso 3)

3. **Actualizar los datos:**
   - **Opción A:** Presiona **F5** o **Ctrl + Alt + F5** (actualizar todo)
   - **Opción B:** `Datos` → `Actualizar todo`
   - **Opción C:** Clic derecho en tabla dinámica → `Actualizar`

4. **¡Listo!** Tu dashboard se actualiza automáticamente

### 📍 Ubicación del archivo Excel:

```
project-data-automation/
└── dashboard/
    └── Sakila_Dashboard.xlsx  ← Aquí
```

También puedes cambiarlo en el archivo **`.env`**:
```env
EXCEL_FILE=dashboard/Sakila_Dashboard.xlsx
AUTO_OPEN_EXCEL=true
```

### 📑 Estructura recomendada del Excel:

#### Hoja 1: Dashboard
- Aquí van todos tus **gráficos** y **análisis visual**
- Usa tablas dinámicas basadas en los datos de las otras hojas
- Diseña tu dashboard como prefieras

#### Hoja 2: Datos Diarios
- Importa: `output/resumen_diario.csv`
- Datos: Fecha | Ingresos | Clientes | Rentas

#### Hoja 3: Top Peliculas
- Importa: `output/top_peliculas.csv`
- Datos: Película | Ingresos | Total Rentas

#### Hoja 4: Por Categoria
- Importa: `output/por_categoria.csv`
- Datos: Categoría | Ingresos | Total Rentas

### 📥 Cómo importar los CSVs en Excel:

**Método recomendado (conexión actualizable):**

1. En Excel, ve a: `Datos` → `Obtener datos` → `De archivo` → `De texto/CSV`
2. Navega a la carpeta `output/`
3. Selecciona el archivo CSV correspondiente (ej: `resumen_diario.csv`)
4. Haz clic en `Cargar` (o `Cargar a...` si quieres elegir ubicación)
5. Los datos se cargarán como una **tabla conectada**
6. Repite para cada CSV en su hoja correspondiente

**✨ Ventaja:** Con este método, cada vez que ejecutes `python sakila_automation.py` y presiones F5 en Excel, los datos se actualizan automáticamente.

### 📊 Ideas para tu Dashboard:

**Gráficos recomendados:**
- **Línea temporal:** Ingresos diarios a lo largo del tiempo
- **Top 10 películas:** Gráfico de barras horizontales
- **Ingresos por categoría:** Gráfico circular o de dona
- **Clientes vs Rentas:** Gráfico de dispersión o líneas
- **KPIs:** Tarjetas con: Total ingresos, Total rentas, Promedio por día

**Tablas dinámicas:**
- Crea tablas dinámicas desde las tablas importadas
- Usa segmentadores (slicers) para filtrar por fechas o categorías
- Calcula métricas adicionales (promedios, porcentajes, etc.)

### 🔄 Actualización de datos - Proceso completo:

```
1. Ejecutar Python:
   python sakila_automation.py
   └─ Se generan/actualizan los CSV

2. En Excel:
   Presionar F5 (Actualizar todo)
   └─ Las tablas conectadas se actualizan

3. Dashboard:
   └─ Gráficos y tablas dinámicas se actualizan automáticamente
```

**⚡ Total: 2 pasos simples - Sin complicaciones**

---

## 🔄 FLUJO DEL PROYECTO

```
MySQL (Sakila DB)
    ↓
┌─────────────────────────────────────┐
│  src/ (Procesamiento)               │
│  ├─ config.py (credenciales .env)   │
│  └─ sakila_etl.py (extrae/transforma) │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│  output/ (Datos procesados)         │
│  ├─ resumen_diario.csv              │
│  ├─ top_peliculas.csv               │
│  └─ por_categoria.csv               │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│  dashboard/ (Visualización)         │
│  └─ Sakila_Dashboard.xlsx           │
│     (Lee CSVs y muestra gráficos)   │
└─────────────────────────────────────┘
```

**Flujo de actualización:**
1. `python main.py` → Procesa datos → Genera CSVs
2. Abrir Excel → Presionar F5 → Dashboard actualizado

---

## 🛠️ INSTALACIÓN AUTOMÁTICA (OPCIONAL - AVANZADO)

Si prefieres automatizar aún más el proceso de instalación, puedes crear un script personalizado que:
- Verifique Python y MySQL
- Instale dependencias automáticamente
- Configure el entorno

**💡 Para este proyecto, la instalación manual es más educativa y comprensible para estudiantes.**

---

## 🛠️ SOLUCIÓN DE PROBLEMAS

### ❌ Error: "Access denied for user 'root'@'localhost'"
- **Causa:** Las credenciales en `.env` no son correctas
- **Solución:**
  1. Abre MySQL Workbench
  2. Verifica con qué usuario/contraseña te conectas
  3. Actualiza esas credenciales en el archivo `.env`
  4. Si usas XAMPP, generalmente la contraseña está vacía: `DB_PASSWORD=`

### ❌ Error: "Can't connect to MySQL server"
```powershell
# Verificar que MySQL está corriendo
Get-Service MySQL*

# Si no está activo, iniciarlo
Start-Service MySQL80
```
- Asegúrate que la base de datos Sakila esté instalada
- Prueba las credenciales en MySQL Workbench primero

### ❌ Error: "ModuleNotFoundError"
```powershell
pip install -r requirements.txt
```

### ❌ Excel no abre automáticamente
- Verifica que existe `Sakila_Dashboard.xlsx` en la carpeta del proyecto
- Cambia la ruta en archivo **`.env`** si está en otra ubicación
- Si no quieres que se abra automáticamente: `AUTO_OPEN_EXCEL=false`

### ❌ Los datos no se actualizan en Excel
- Asegúrate de haber importado los CSVs como **conexiones** (no copiar/pegar)
- Método correcto: `Datos` → `Obtener datos` → `De texto/CSV`
- Después de ejecutar Python, presiona **F5** en Excel
- Si usas tablas dinámicas: clic derecho → `Actualizar`

### ❌ Archivos CSV vacíos
- Revisa que la base de datos Sakila tenga datos
- Verifica la conexión a MySQL

---

## 📦 QUÉ CONTIENE CADA CARPETA/ARCHIVO

| Carpeta/Archivo | Descripción |
|-----------------|-------------|
| **main.py** | ⭐ Punto de entrada principal - EJECUTAR ESTE |
| **src/** | Paquete con código de procesamiento |
| **src/sakila_etl.py** | Lógica ETL: extrae, transforma y guarda datos |
| **src/config.py** | Lee configuración desde .env |
| **output/** | Datos procesados (CSVs generados automáticamente) |
| **dashboard/** | Visualización (dashboard de Excel) |
| **dashboard/Sakila_Dashboard.xlsx** | Tu dashboard de Excel con gráficos |
| **docs/** | Documentación del proyecto (3 guías + readme) |
| **.env** | 🔒 CREDENCIALES (NO subir a Git) |
| **.env.example** | Plantilla para crear tu .env |
| **.gitignore** | Archivos que Git debe ignorar |
| **requirements.txt** | Lista de dependencias Python (5 librerías) |

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

- [ ] Python 3.8+ instalado (`python --version`)
- [ ] MySQL instalado y corriendo (`Get-Service MySQL*`)
- [ ] Base de datos Sakila instalada en MySQL
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] Archivo `.env` creado con tus credenciales de MySQL
- [ ] Archivo `Sakila_Dashboard.xlsx` creado (manualmente)
- [ ] Primera ejecución exitosa (`python sakila_automation.py`)
- [ ] Archivos CSV generados en carpeta `output/`
- [ ] CSVs importados en Excel como conexiones
- [ ] Gráficos y dashboard creados en Excel
- [ ] Actualización probada (ejecutar Python → presionar F5 en Excel)

---

## 📂 Estructura Final del Proyecto

```
project-data-automation/
│
├── 📄 sakila_automation.py    ⭐ EJECUTAR ESTE
├── 📄 main.py                 (lógica principal)
├── 📄 sakila_etl.py           (extracción y transformación)
├── 📄 config.py               (configuración desde .env)
├── 📄 requirements.txt        (dependencias)
├── 📄 README.md               (esta guía)
│
├── 🔒 .env                    (credenciales - NO subir a Git)
├── 📋 .env.example            (plantilla de .env)
├── 🚫 .gitignore              (archivos ignorados por Git)
│
├── 📊 Sakila_Dashboard.xlsx   (tu dashboard - crear manualmente)
│
├── 📁 output/                 (CSVs generados por Python)
│   ├── resumen_diario.csv
│   ├── top_peliculas.csv
│   └── por_categoria.csv
│
├── 📁 .venv/                  (entorno virtual - opcional)
└── 📁 .git/                   (control de versiones)
```

**Total archivos esenciales:** 10 (7 Python + 3 config)
**Archivos generados:** 3 CSVs en `output/`

---

## 💡 TIPS Y MEJORES PRÁCTICAS

- **Portable:** Toda la carpeta es portable, cópiala y funciona en cualquier PC
- **Simple:** Solo 5 archivos Python esenciales + configuración
- **Rápido:** Ejecuta `python sakila_automation.py` y presiona F5 en Excel
- **Sin macros:** No necesitas habilitar macros, todo es manual y seguro
- **Educativo:** Código comentado y fácil de entender para estudiantes
- **Profesional:** Estructura limpia siguiendo mejores prácticas
- **Seguro:** Las credenciales están en `.env` y nunca se suben a Git
- **Actualizable:** Cada ejecución genera datos frescos desde MySQL

### 🎯 Para estudiantes:
- **Aprende el flujo:** MySQL → Python → CSV → Excel
- **Modifica el código:** Agrega tus propios análisis en `sakila_etl.py`
- **Personaliza Excel:** Crea gráficos y dashboards únicos
- **Practica Git:** El `.gitignore` ya está configurado correctamente

---

## 📚 Recursos

- [Base de datos Sakila](https://dev.mysql.com/doc/sakila/en/) - Documentación oficial
- [Pandas](https://pandas.pydata.org/docs/) - Documentación
- [SQLAlchemy](https://docs.sqlalchemy.org/) - Documentación

---

**¡Listo para automatizar! 🚀**

*Proyecto simplificado para estudiantes - Sin complicaciones*
