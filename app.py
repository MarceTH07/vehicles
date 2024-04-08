import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') #leer los datos
st.header('Analisis de datos de anuncios de venta de coches') #encabezado

hist_button = st.button('Construir histogramas') #Crear un boton

if hist_button: #al hacer clic en el boton
    #escribir el mensaje
    st.write('Creacion de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x = "odometer")

    #mostrar un grafico Plotly interactivo
    st.plotly_chart(fig,use_container_width=True)

import streamlit as st

#crear una casilla de verificacion
build_dispersion = st.checkbox('Construir un grafico de dispersión')

if build_dispersion: #si la casilla de verificacion esta seleccionada
    st.write('Construir un grafico de dispersión entre uso y precio')
    # crear un grafico de dispersion
    fig = px.scatter(car_data, x = "odometer", y="price")

    #mostrar un grafico Plotly interactivo
    st.plotly_chart(fig,use_container_width=True)
