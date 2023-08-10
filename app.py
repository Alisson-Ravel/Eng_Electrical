import streamlit as st
import pdfkit
# criando um titutlo
import streamlit.components.v1 as components


# crinado uma caixa de seleção


st.sidebar.title('Menu')


pagina_selecionada=st.sidebar.selectbox('Selecione a pagina',['Calcular Queda de tensão','Calcular corrente'])

if pagina_selecionada=='Calcular Queda de tensão':
    st.title('CALCULO QUEDA DE TENSÃO')
    tipo_cabo=st.selectbox('Tipo de Cabo', ['Cobre', 'Alumínio'])
else:
    st.title('CALCULO DE CORRENTE DO CABO')
    st.number_input('Tensão')
