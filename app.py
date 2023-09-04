import streamlit as st
import pandas as pd
from helper import *
import warnings
warnings.filterwarnings('ignore')



urls = ['https://vcsmart.s3.us-east-2.amazonaws.com/CABA-PER-092023.txt','https://vcsmart.s3.us-east-2.amazonaws.com/PBA-PER-092023.TXT']
df = pd.read_csv('columns.txt',sep=';')
if len(urls) < 1:
    st.markdown('No hay archivos .txt en el repositorio')
elif len(urls) >= 1:
    for url in urls:
        temp_df = pd.read_csv(url,sep=';',names=df.columns)
        # temp_df = pd.read_csv(url,sep=';',names=df.columns,compression='gzip')
        df = pd.concat([df,temp_df])        

for col in df.columns:
    df[col] = df[col].astype(str)
st.markdown(f'Total {len(df)} lineas')    
st.data_editor(
        filter_dataframe(
        df
        ).head(20)
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
