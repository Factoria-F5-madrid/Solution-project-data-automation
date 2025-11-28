# 📊 Dashboard - Visualización de Datos

Esta carpeta contiene el archivo Excel que sirve como **interfaz visual** del proyecto.

## 📄 Archivo Principal

**`Sakila_Dashboard.xlsx`** - Dashboard de Excel con gráficos y análisis

## 🎯 Propósito

El dashboard es la **capa de visualización** que presenta los datos procesados por Python de forma visual e interactiva.

```
┌─────────────────────────────────────┐
│  MySQL (Base de Datos)              │
│  └─ Datos crudos                    │
└─────────────────────────────────────┘
            ↓
┌─────────────────────────────────────┐
│  Python (Procesamiento)             │
│  └─ src/sakila_etl.py               │
└─────────────────────────────────────┘
            ↓
┌─────────────────────────────────────┐
│  output/ (Datos procesados)         │
│  └─ CSVs con análisis               │
└─────────────────────────────────────┘
            ↓
┌─────────────────────────────────────┐
│  dashboard/ (Visualización)         │
│  └─ Sakila_Dashboard.xlsx           │
└─────────────────────────────────────┘
```

## 🔄 Cómo Funciona

1. **Python procesa** los datos de MySQL
2. **Genera CSVs** en la carpeta `output/`
3. **Excel lee** esos CSVs (conexiones de datos)
4. **Dashboard muestra** gráficos y análisis visual

## 📋 Estructura del Dashboard

### Hojas recomendadas:

1. **Dashboard** - Vista principal con todos los gráficos
2. **Datos Diarios** - Conectada a `output/resumen_diario.csv`
3. **Top Películas** - Conectada a `output/top_peliculas.csv`
4. **Por Categoría** - Conectada a `output/por_categoria.csv`

## 🔄 Actualizar Datos

Después de ejecutar `python main.py`:

```
1. Abrir dashboard/Sakila_Dashboard.xlsx
2. Presionar F5 (o Ctrl + Alt + F5)
3. Los datos se actualizan automáticamente
```

## 💡 Beneficios de esta Organización

- ✅ **Separación clara:** Visualización separada del código
- ✅ **Portable:** Puedes compartir solo el dashboard
- ✅ **Organizado:** Fácil de encontrar y mantener
- ✅ **Escalable:** Puedes agregar más dashboards

## 📖 Más Información

Ver **`docs/GUIA_EXCEL.md`** para instrucciones detalladas sobre cómo crear y configurar el dashboard.
