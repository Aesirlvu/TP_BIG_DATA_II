import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Dashboard COVID-19 Formosa",
    page_icon="🦠",
    layout="wide"
)

st.title('Análisis de Casos COVID-19 en Formosa 🦠')

# Leer CSV
df = pd.read_csv('Covid19Casos_Formosa.csv')

# st.subheader('Datos cargados 🗂️')

with st.expander("Datos cargados 🗂️", expanded=False):
    st.write("Vista previa:")
    st.dataframe(df.head())

st.subheader('Gráficos y Análisis de los datos 📈')

fig, ax = plt.subplots()


st.header("1. Evolución Temporal de Casos 📈")
st.markdown("""
Esta sección presenta la evolución temporal de los casos de COVID-19 en Formosa.
Podrás observar las tendencias semanales y mensuales, así como el comportamiento
acumulativo de los contagios a lo largo del tiempo.
""")



st.header("2. Análisis Geográfico 🗺️")
st.markdown("""
Aquí exploramos la distribución geográfica de los casos de COVID-19 en la provincia.
Identificamos las zonas con mayor incidencia y comparamos la situación entre diferentes
departamentos y localidades de Formosa.
""")

st.header("3. Perfil Demográfico 👥")
st.markdown("""
En esta sección analizamos las características demográficas de los casos de COVID-19,
incluyendo la distribución por género, edad y franjas etarias, para comprender
qué grupos poblacionales fueron más afectados durante la pandemia.
""")

st.write('🔷 Histograma')
ax = sns.histplot(data=df, x='edad', bins=40, ax=ax)
ax.set_title('Distribución de la edad de los casos de COVID-19 en Formosa')
st.pyplot(fig)

st.header("4. Severidad de Casos 🏥")
st.markdown("""
Esta sección evalúa la severidad de los casos de COVID-19 en Formosa,
enfocándose en pacientes que requirieron cuidados intensivos o
asistencia respiratoria mecánica, y su distribución por características demográficas.
""")

st.header("5. Análisis por Semana Epidemiológica 📆")
st.markdown("""
Esta sección muestra la evolución de la pandemia organizada por semanas epidemiológicas,
permitiendo identificar los picos de contagio y evaluar posibles patrones estacionales
en la transmisión del virus.
""")

st.header("Conclusiones y Hallazgos Principales 🔍")
st.markdown("""
Basados en el análisis de los datos de COVID-19 en la provincia de Formosa, podemos destacar los siguientes hallazgos:

1. **Evolución temporal**: [Espacio para conclusiones sobre patrones temporales]
2. **Distribución geográfica**: [Espacio para conclusiones sobre las zonas más afectadas]
3. **Perfil demográfico**: [Espacio para conclusiones sobre grupos etarios y géneros más afectados]
4. **Severidad**: [Espacio para conclusiones sobre tasas de hospitalización e intubación]
5. **Mortalidad**: [Espacio para conclusiones sobre tasas de mortalidad y factores asociados]

> Nota: Este dashboard proporciona información visual para una mejor comprensión de la evolución y el impacto de la pandemia en la provincia de Formosa.
""")