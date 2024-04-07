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
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: #si la casilla de verificacion esta seleccionada
    st.write('Construir un histograma para la columna odómetro')
    # crear un histograma
    fig = px.histogram(car_data, x = "odometer")

    #mostrar un grafico Plotly interactivo
    st.plotly_chart(fig,use_container_width=True)