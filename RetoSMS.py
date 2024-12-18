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
distr_puntaje = px.histogram(df, x="performance_score", labels={"performance_score":"Puntaje de desempeño"})
st.plotly_chart(distr_puntaje)

#Código que permita mostrar un gráfico en donde se visualice el promedio de horas trabajadas por el género del empleado
horasGenero=df.groupby('gender')["average_work_hours"].mean()
graf_horas_genero= px.bar(horasGenero, y="average_work_hours")
st.plotly_chart(graf_horas_genero)

#Código que permita mostrar un gráfico en donde se visualice la edad de los empleados con respecto al salario de los mismos.
edad_salario= px.scatter(df, y="salary", x="age", labels={"salary":"Salario", "age": "Edad"}, hover_data=["position"], color="gender")
st.plotly_chart(edad_salario)

#Código que permita mostrar un gráfico en donde se visualice la relación del promedio de horas trabajadas versus el puntaje de desempeño.
desempeño_horas=px.scatter(df, y="average_work_hours", x="performance_score", size="salary", labels={"average_work_hours": "Horas promedio", "salary": "Salario"}, hover_data=["position"])
st.plotly_chart(desempeño_horas)

#Código que permita desplegar una conclusión sobre el análisis mostrado en la aplicación web
st.subheader("Conclusiones")
st.text("En el primer gráfico se puede observar que la mayoría de los empleados tiene un puntaje de desempeño de 3 sobre 4, además de que el gráfico tiene un sesgo hacia los mayores puntajes, esto se traduce en empleados con alto desempeño.")
st.text("El segundo gráfico muestra que en promedio las mujeres trabajan más horas que los hombres.")
st.text("La mayoría de los empleados con salarios más altos tienen entre 30 y 55 años, la excepción siendo la CEO que tiene 67 años y el mayor salario de la empresa.")
st.text("Muchos de los empleados que tienen la calificación de desempeño máxima trabajan menos horas del promedio pero reciben un salario mayor, lo que significa que la productividad en la empresa no sigue una relación lineal con las horas trabajadas.")