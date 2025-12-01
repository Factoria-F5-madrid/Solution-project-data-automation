# src/dashboard_excel.py - VERSIÓN FINAL SIMPLIFICADA
# Primera vez: crea Excel con datos como tabla
# Siguientes veces: solo actualiza CSV (Excel actualiza con F5)

import pandas as pd
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo
import os

class DashboardExcel:
    def __init__(self, datos_df):
        self.datos = datos_df
        self.excel_file = "dashboard/dashboard_sakila.xlsx"
        self.csv_file = "output/datos_sakila.csv"
    
    def generar(self):
        """Genera Excel inicial O actualiza solo CSV"""
        try:
            if os.path.exists(self.excel_file):
                # Excel existe → solo actualizar CSV
                self.datos.to_csv(self.csv_file, index=False, encoding='utf-8-sig')
                print(f"\n✅ CSV actualizado: {self.csv_file}")
                print("💡 EN EXCEL: Presiona F5 para actualizar")
                return True
            else:
                # Excel no existe → crear nuevo con datos
                return self._crear_excel_con_datos()
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def _crear_excel_con_datos(self):
        """Crear Excel nuevo con datos cargados como tabla"""
        wb = openpyxl.Workbook()
        
        # Eliminar hoja por defecto
        if "Sheet" in wb.sheetnames:
            wb.remove(wb["Sheet"])
        
        # Crear hoja con datos
        ws = wb.create_sheet("Datos_Sakila", 0)
        
        # Título
        ws['A1'] = "🎬 DATOS SAKILA - Base para Dashboard"
        ws['A1'].font = Font(size=14, bold=True, color="366092")
        ws.merge_cells(f'A1:{get_column_letter(len(self.datos.columns))}1')
        ws['A1'].alignment = Alignment(horizontal="center")
        
        ws['A2'] = "💡 Ejecuta 'python main.py' para actualizar → Presiona F5 aquí"
        ws['A2'].font = Font(size=10, italic=True, color="666666")
        ws.merge_cells(f'A2:{get_column_letter(len(self.datos.columns))}2')
        
        # Cargar datos desde fila 4
        for r_idx, r in enumerate(dataframe_to_rows(self.datos, index=False, header=True), start=4):
            for c_idx, value in enumerate(r, start=1):
                ws.cell(row=r_idx, column=c_idx, value=value)
        
        # Formatear encabezados
        for col in range(1, len(self.datos.columns) + 1):
            cell = ws.cell(row=4, column=col)
            cell.fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
            cell.font = Font(color="FFFFFF", bold=True)
            cell.alignment = Alignment(horizontal="center")
        
        # Crear tabla de Excel
        tabla_rango = f"A4:{get_column_letter(len(self.datos.columns))}{len(self.datos) + 4}"
        tabla = Table(displayName="TablaSakila", ref=tabla_rango)
        tabla.tableStyleInfo = TableStyleInfo(
            name="TableStyleMedium9",
            showFirstColumn=False,
            showRowStripes=True
        )
        ws.add_table(tabla)
        
        # Ajustar columnas
        for i in range(1, len(self.datos.columns) + 1):
            col_letter = get_column_letter(i)
            try:
                max_length = max(
                    len(str(self.datos.columns[i-1])),
                    self.datos.iloc[:, i-1].astype(str).str.len().max()
                )
                ws.column_dimensions[col_letter].width = min(max_length + 2, 30)
            except:
                ws.column_dimensions[col_letter].width = 15
        
        # Guardar archivos
        os.makedirs("dashboard", exist_ok=True)
        wb.save(self.excel_file)
        self.datos.to_csv(self.csv_file, index=False, encoding='utf-8-sig')
        
        print(f"\n✅ Archivos creados:")
        print(f"   • {self.excel_file}")
        print(f"   • {self.csv_file}")
        print("\n📋 SIGUIENTE:")
        print("   1. Abre el Excel")
        print("   2. Crea tablas dinámicas desde 'TablaSakila'")
        print("   3. Diseña tu dashboard")
        print("\n🔄 ACTUALIZAR:")
        print("   1. Terminal: python main.py")
        print("   2. Excel: Abre el archivo y presiona F5")
        print("\n⚠️  IMPORTANTE:")
        print("   Si F5 no funciona, elimina la hoja 'Datos_Sakila'")
        print("   y re-importa desde: Datos → Desde CSV")
        return True

def crear_dashboard():
    """Función principal"""
    from .sakila_etl import proceso_completo
    
    datasets = proceso_completo()
    if not datasets:
        return False
    
    datos = datasets['datos_principales']
    print(f"✓ {len(datos)} registros cargados")
    
    dashboard = DashboardExcel(datos)
    return dashboard.generar()

if __name__ == "__main__":
    crear_dashboard()