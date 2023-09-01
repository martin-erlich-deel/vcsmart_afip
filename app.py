import streamlit as st
import pandas as pd
from helper import *
import glob


txt_files = glob.glob("*.txt")
cols = ['col_1','col_2','col_3','col_4','col_5','col_6','col_7','col_8','col_9','col_10']
df = pd.read_csv('columns.txt',sep=';')
txt_files = [txt for txt in txt_files if txt != 'columns.txt']
if len(txt_files) < 1:
    st.markdown('No hay archivos .txt en el repositorio')
elif len(txt_files) >= 1:
    for txt in txt_files:
        temp_df = pd.read_csv(txt,sep=';',names=cols)
        df = pd.concat([df,temp_df])
df.pop(df.columns[-1])
st.data_editor(
        filter_dataframe(
        df
        )
        ,
        column_config={
            "Preview Image": st.column_config.ImageColumn(
                "Preview Image", help="Streamlit app preview screenshots"
            ),
            "Item ID": st.column_config.TextColumn("Item ID"),
            "Nombre del producto": st.column_config.TextColumn("Nombre del producto",),
            "Ventas totales": st.column_config.NumberColumn("Ventas totales",format="$ %.2f"),
            "Precio promedio de unidad": st.column_config.NumberColumn("Precio promedio de unidad",format="$ %.2f"),
            "Costo promedio de unidad": st.column_config.NumberColumn("Costo promedio de unidad",format="$ %.2f"),
            "Costos totales": st.column_config.NumberColumn("Costos totales",format="$ %.2f"),
            "Unidades vendidas": st.column_config.NumberColumn("Unidades vendidas"),
            "Margen bruto": st.column_config.NumberColumn("Margen bruto",format="$ %.2f"),
            "M1 %": st.column_config.NumberColumn("M1 %", format="%.2f%%"),
            "Fees marketplace": st.column_config.NumberColumn("Fees marketplace",format="$ %.2f"),
            "Fees shipping": st.column_config.NumberColumn("Fees shipping", format="$ %.2f"),
            "Margen 2": st.column_config.NumberColumn("Margen 2",format="$ %.2f"),
            "M2 %": st.column_config.NumberColumn("M2 %", format="%.2f%%"),

        },
        hide_index=True,
    )
