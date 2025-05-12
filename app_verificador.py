import pandas as pd
import re
import dns.resolver
import streamlit as st
import plotly.express as px

# ----------- CONFIGURACIÓN DE LA PÁGINA -----------
st.set_page_config(page_title="Validador de Correos Empresariales", layout="centered")

# ----------- ESTILO PERSONALIZADO -----------
custom_css = """
<style>
    body {
        background-color: #0f0f0f;
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp {
        background-color: #121212;
        color: #f5f5f5;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 20px #00ffe1;
    }
    h1 {
        color: #00ffe1;
        text-align: center;
    }
    footer {
        text-align: center;
        color: #888;
        margin-top: 2rem;
        font-size: 14px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ----------- TÍTULO -----------
st.title("🔍 Validador de Correos Empresariales")

# ----------- FUNCIONES DE VALIDACIÓN -----------
dominios_publicos = ['gmail.com', 'hotmail.com', 'outlook.com', 'yahoo.com', 'icloud.com', 'live.com']

def es_correo_valido(correo):
    if pd.isnull(correo):
        return False
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron, correo) is not None

def dominio_tiene_mx(correo):
    try:
        dominio = correo.split('@')[1]
        if dominio.lower() in dominios_publicos:
            return False
        respuestas = dns.resolver.resolve(dominio, 'MX')
        return len(respuestas) > 0
    except Exception:
        return False

# ----------- SUBIR ARCHIVO -----------
archivo_cargado = st.file_uploader("📁 Sube tu archivo Excel (.xlsx)", type=["xlsx"])

if archivo_cargado:
    df = pd.read_excel(archivo_cargado)

    if 'E-mail' not in df.columns:
        st.error("❌ El archivo no contiene una columna llamada 'E-mail'.")
    else:
        df['formato_valido'] = df['E-mail'].apply(es_correo_valido)
        df['dominio_valido'] = df['E-mail'].apply(lambda x: dominio_tiene_mx(x) if es_correo_valido(x) else False)
        df['correo_valido'] = df['formato_valido'] & df['dominio_valido']

        st.success("✅ Verificación completada.")

        # ----------- GRÁFICO DE RESULTADOS -----------
        total = len(df)
        validos = df['correo_valido'].sum()
        invalidos_formato = ((df['formato_valido'] == False) & (df['E-mail'].notnull())).sum()
        invalidos_dominio = ((df['formato_valido']) & (df['dominio_valido'] == False)).sum()
        nulos = df['E-mail'].isnull().sum()

        datos_grafico = pd.DataFrame({
            'Estado': ['✅ Válidos', '❌ Inválido (formato)', '⚠️ Inválido (dominio)', '🟥 Vacíos'],
            'Cantidad': [validos, invalidos_formato, invalidos_dominio, nulos]
        })

        fig = px.pie(
            datos_grafico, 
            names='Estado', 
            values='Cantidad', 
            title='📊 Distribución de Correos Validados',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig)

        # ----------- DESCARGA DE RESULTADOS -----------
        archivo_salida = "resultado_correos.xlsx"
        df.to_excel(archivo_salida, index=False)
        with open(archivo_salida, "rb") as file:
            st.download_button("📥 Descargar archivo con resultados detallados", file, file_name=archivo_salida)

# ----------- PIE DE PÁGINA -----------
st.markdown("""<footer>By José L. Robles</footer>""", unsafe_allow_html=True)
