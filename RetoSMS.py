import pandas as pd
import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import plotly.express as px

#Leer dataframe
df=pd.read_csv("kpis.csv")

#Codigo que despliegue un título y una breve descripción
st.title("KPI's Socialize your knowledge")
st.write("El objetivo es mostrar los indicadores de los empleados de la empresa. Utiliza los filtros del panel izquierdo para navegar por distintos escenarios")

#Código que permita desplegar el logotipo
response = requests.get("https://thumbs.dreamstime.com/b/creative-rounded-initial-letters-syk-logo-will-be-suitable-which-company-brand-name-start-225611136.jpg")
logo = Image.open(BytesIO(response.content))
st.sidebar.image(logo,caption="Logotipo de la empresa")

#Código que permita desplegar un control para seleccionar el género del empleado
sexo=st.sidebar.selectbox("Selecciona el género:", df["gender"].unique())

#Código que permita desplegar un control ára seleccionar el rango del puntaje del desempeño del empleado
puntaje=st.sidebar.slider("Selecciona el rango de puntaje:", min_value=int(df["performance_score"].min()),max_value=int(df["performance_score"].max()))

#Código que permita desplegar un control para seleccionar el estado civil del empleado
estado_civil=st.sidebar.selectbox("Selecciona el estado civil:", df["marital_status"].unique())

#Código que permita mostrar un gráfico donde se vislualize la distribución de los puntajes de desempeño
distr_puntaje = px.histogram(df, x="performance_score")
#distr_puntaje.show()
st.plotly_chart(distr_puntaje)

#Código que permita mostrar un gráfico en donde se visualice el promedio de horas trabajadas por el género del empleado
#horasGenero=df.groupby('gender')["average_work_hours"].sum()
#graf_horas_genero= px.bar(horasGenero, x='gender', y="average_work_hours")
#st.plotly_chart(graf_horas_genero)

#Código que permita mostrar un gráfico en donde se visualice la edad de los empleados con respecto al salario de los mismos.
edad_salario= px.scatter(df, x="salary", y="age")
#edad_salario.show()
st.plotly_chart(edad_salario)

#Código que permita mostrar un gráfico en donde se visualice la relación del promedio de horas trabajadas versus el puntaje de desempeño.
desempeño_horas=px.scatter(df, x="average_work_hours", y="performance_score")
#desempeño_horas.show()
st.plotly_chart(desempeño_horas)

#Código que permita desplegar una conclusión sobre el análisis mostrado en la aplicación web
st.subheader("Conclusiones")
st.text("Se puede observar que...")