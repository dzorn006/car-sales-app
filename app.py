import pandas as pd
import plotly.express as px
import streamlit as st

#Cargar datos
df = pd.read_csv("vehicles_us.csv")

#Filtrar precios razonables (entre 500 y 100,000 dólares)
df = df[(df["price"] >= 500) & (df["price"] <= 100000)]

#Gráfica 1: Precio promedio por Año del Modelo 
st.header("Relación entre Año del Modelo y Precio")
df_grouped_year = df.groupby("model_year", as_index=False)["price"].mean()
fig_year = px.bar(df_grouped_year, x="model_year", y="price", title="Precio Promedio por Año del Modelo")
st.plotly_chart(fig_year)
st.markdown("**Insight:** Los vehículos más recientes tienden a tener precios promedio más altos, como era de esperarse.")


#Gráfica 2: Relación entre Precio y Kilometraje 
st.header("Relación entre Precio y Kilometraje")
fig_odometer = px.scatter(df, x="odometer", y="price", title="Precio vs Kilometraje", opacity=0.5)
st.plotly_chart(fig_odometer)
st.markdown("**Insight:** Los vehículos más recientes tienden a tener precios promedio más altos, como era de esperarse.")


#Gráfica 3: Relación entre Precio y Condición del Vehículo 
st.header("Relación entre Precio y Condición del Vehículo")
fig_condition = px.box(df, x="condition", y="price", title="Precio vs Condición del Vehículo")
st.plotly_chart(fig_condition)
st.markdown("**Insight:** Los vehículos en mejor estado(‘excellent’ y ‘like new’) tienen un precio claramente más alto, lo cual es consistente con lo esperado.")

#Conclusión general de mi análisis y proyecto
st.header("Conclusiones Finales") 
st.markdown("""
Este análisis permite observar cómo diferentes características influyen en el precio de los vehículos usados:

- El año del modelo tiene una relación positiva con el precio: cuanto más nuevo, mayor el valor.
- El kilometraje afecta negativamente al precio, como es lógico por el desgaste.
- La condición física del vehículo también tiene un impacto importante: los autos en mejor estado se venden a precios considerablemente más altos.

Estas relaciones pueden servir como base para futuros análisis predictivos o decisiones de negocio en torno a la compra-venta de vehículos usados.
""") 