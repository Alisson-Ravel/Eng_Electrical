import streamlit as st
import pdfkit
import math
# criando um titutlo
import streamlit.components.v1 as components


# crinado uma caixa de seleção

st.sidebar.title('Menu')


pagina_selecionada_queda_de_tensao=st.sidebar.selectbox('QUEDA DE TENSÃO',['Queda de tensão - CABO','Queda de tensão - CONDUTOR MÍNIMO'])

#********************************************************************************************************************************************************************
#********************************************************** QUEDA DE TENSAO  - CABO ********************************************************************************
#********************************************************************************************************************************************************************
if pagina_selecionada_queda_de_tensao=='Queda de tensão - CABO':

    st.title('CALCULO QUEDA DE TENSÃO - CABO')

    #******************** Entradas do usuario****************
    tipo_cabo =st.selectbox('Material do Cabo', ['Cobre', 'Alumínio'])
    tensão=st.number_input('Tensão(V)',0,500000)
    corrente_amperes=st.number_input('Corrente de projeto(A)',0,50000)
    comprimento_circuito=st.number_input('Comprimento do circuito(m)',0)
    secao_cabo =st.selectbox('Seção do cabo(mm²)', [1, 1.5,2.5,4,6,10,16,25,35,50,70,95,120,150,185,240,300,400,500,630,800,1000])

    print(type(secao_cabo))
    #secao_cabo =float(st.selectbox('Seção do cabo', [1, 1.5,2.5,'4','6','10','16','25','35','50','70,']))
    #******************** Entradas do usuario****************

    resistividade_cobre=0.0178; #ohms*mm²/metro
    resistividade_aluminio=0.0292; #ohms*mm²/metro
    resistividade_do_cabo=resistividade_cobre

    if tipo_cabo=='Alumínio':
        resistividade_do_cabo=resistividade_aluminio
    else:
        resistividade_do_cabo=resistividade_cobre
    


    botao_calcular=st.button('CALCULAR')
    print(type(botao_calcular))

    if botao_calcular:
        print('\n\n\n botao acionado\n\n\n')

        Queda_de_tensao=((2*resistividade_do_cabo*comprimento_circuito*corrente_amperes)/(secao_cabo*tensão))*100 #%

        texto_queda=f'Queda de tensão do circuito: {round(Queda_de_tensao,2)}%'
        st.write(texto_queda)
    


#********************************************************************************************************************************************************************
#********************************************************** QUEDA DE TENSAO  - CABO ********************************************************************************
#********************************************************************************************************************************************************************

#********************************************************************************************************************************************************************
#********************************************************** QUEDA DE TENSAO  - CONDUTOR MINIMO **********************************************************************
#********************************************************************************************************************************************************************

else:
    st.title('Queda de tensão - CONDUTOR MÍNIMO')

    #******************** Entradas do usuario****************
    tipo_instalação =st.selectbox('Tipo de Ligação', ['Monofásico', 'Bifásico','Trifásico'])
    tipo_cabo =st.selectbox('Material do Cabo', ['Cobre', 'Alumínio'])
    tensão=st.number_input('Tensão(V)',0,500000)
    corrente_amperes=st.number_input('Corrente de projeto(A)',0,50000)
    comprimento_circuito=st.number_input('Comprimento do circuito(m)',0)
    queda_de_tensao_desejavel=st.number_input('Queda de tensão desejável(%)',0,100)

    #******************** Entradas do usuario****************

    resistividade_cobre=0.0178; #ohms*mm²/metro
    resistividade_aluminio=0.0292; #ohms*mm²/metro
    resistividade_do_cabo=resistividade_cobre

    if tipo_cabo=='Alumínio':
        resistividade_do_cabo=resistividade_aluminio
    else:
        resistividade_do_cabo=resistividade_cobre
    


    botao_calcular=st.button('CALCULAR')
    print(type(botao_calcular))

    if botao_calcular:
        print('\n\n\n botao acionado\n\n\n')

        if tipo_instalação=='Monofásico' or tipo_instalação=='Bifásico':


            secao_minima_condutor=((2*resistividade_do_cabo*comprimento_circuito*corrente_amperes)/(queda_de_tensao_desejavel*tensão))*100 #mm²

            texto_secao_minima=f'\n\n Seção mínima do condutor: {round(secao_minima_condutor,2)}mm²\n'
            st.write(texto_secao_minima)
        else:

            secao_minima_condutor=((math.sqrt(3)*resistividade_do_cabo*comprimento_circuito*corrente_amperes)/(queda_de_tensao_desejavel*tensão))*100   #mm²

            texto_secao_minima=f'\n\n Seção mínima do condutor: {round(secao_minima_condutor,2)}mm²\n'
            st.write(texto_secao_minima)

#********************************************************************************************************************************************************************
#********************************************************** QUEDA DE TENSAO  - CONDUTOR MINIMO **********************************************************************
#********************************************************************************************************************************************************************