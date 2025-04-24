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

with st.expander("Datos cargados 🗂️", expanded=False):
    st.write("Vista previa:")
    st.dataframe(df.head())

st.subheader('Gráficos y Análisis de los datos 📈')

fig_casos_departamento, ax_casos_departamento = plt.subplots()

st.header("1. Evolución Temporal de Casos 📈")
# Descripción omitida para brevedad

st.header("2. Análisis Geográfico 🚩")
casos_departamento = df[df['clasificacion_caso'] == 'Confirmado'].groupby('departamento_residencia').size().sort_values()
sns.barplot(x=casos_departamento.values, y=casos_departamento.index, color='steelblue', edgecolor='black', ax=ax_casos_departamento)
ax_casos_departamento.set_title('Casos Confirmados por Departamento - Formosa')
ax_casos_departamento.set_xlabel('Cantidad de Casos Confirmados')
ax_casos_departamento.set_ylabel('Departamento')
ax_casos_departamento.bar_label(ax_casos_departamento.containers[0], fontsize=10)
plt.tight_layout()
st.pyplot(fig_casos_departamento)

st.header("3. Perfil Demográfico 👥")
fig_distribucion_edad, ax_distribucion_edad = plt.subplots()
sns.histplot(data=df, x='edad', bins=40, ax=ax_distribucion_edad)
ax_distribucion_edad.set_title('Distribución de la edad de los casos de COVID-19 en Formosa')
st.pyplot(fig_distribucion_edad)

st.header("4. Severidad de Casos 🏥")
fig_uci, ax_uci = plt.subplots(figsize=(10, 6))
uci_por_edad = df[df['requirio_uci'] == 1]['grupo_edad'].value_counts().sort_index()
sns.barplot(x=uci_por_edad.index, y=uci_por_edad.values, palette='Purples', ax=ax_uci)
ax_uci.set_title('Casos que requirieron UCI por Grupo Etario')
ax_uci.set_xlabel('Grupo de Edad')
ax_uci.set_ylabel('Cantidad de Casos en UCI')
st.pyplot(fig_uci)

fig_arm, ax_arm = plt.subplots(figsize=(10, 6))
arm_por_edad = df[df['requirio_arm'] == 1]['grupo_edad'].value_counts().sort_index()
sns.barplot(x=arm_por_edad.index, y=arm_por_edad.values, palette='Reds', ax=ax_arm)
ax_arm.set_title('Casos con Asistencia Respiratoria Mecánica (ARM) por Grupo Etario')
ax_arm.set_xlabel('Grupo de Edad')
ax_arm.set_ylabel('Cantidad de Casos con ARM')
st.pyplot(fig_arm)

fig_mortalidad, ax_mortalidad = plt.subplots(figsize=(12, 6))
fallecidos = df[df['indicador_fallecimiento'] == 1]
sns.histplot(data=fallecidos, x='grupo_edad', hue='sexo', multiple='stack', shrink=0.8, palette='Set2', ax=ax_mortalidad)
ax_mortalidad.set_title('Fallecimientos por Grupo Etario y Sexo')
ax_mortalidad.set_xlabel('Grupo de Edad')
ax_mortalidad.set_ylabel('Cantidad de Fallecidos')
st.pyplot(fig_mortalidad)

st.header("5. Análisis por Semana Epidemiológica 📆")
fig_semana_epi, ax_semana_epi = plt.subplots(figsize=(14, 6))
casos_por_semana = df.groupby('sem_epidemiologica').size()
sns.barplot(x=casos_por_semana.index, y=casos_por_semana.values, color='orange', edgecolor='black', ax=ax_semana_epi)
ax_semana_epi.set_title('Casos por Semana Epidemiológica - Formosa')
ax_semana_epi.set_xlabel('Semana Epidemiológica')
ax_semana_epi.set_ylabel('Cantidad de Casos')
st.pyplot(fig_semana_epi)
