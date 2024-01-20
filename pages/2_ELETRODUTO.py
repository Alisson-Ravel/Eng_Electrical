import streamlit as st 
import numpy as numpy
import pandas as pd
import math

def calcula_eletroduto():
        # chamando a funcao para calcular taxa de ocupacao
    calcular_taxa_ocupacao()

    #***************************************************************************************
    global area_cabo_1_mm
    global area_cabo_2_mm
    global area_cabo_3_mm
    global area_cabo_4_mm
    global area_cabo_5_mm
    global area_cabo_6_mm

    global taxa_maxima_ocupacao

    global qtd_cabo_1
    global qtd_cabo_2
    global qtd_cabo_3
    global qtd_cabo_4
    global qtd_cabo_5
    global qtd_cabo_6


        
    if secao_cabo_1=="Nao aplicavel":
        qtd_cabo_1=0
        area_cabo_1_mm=0

    if secao_cabo_1=="0,5mm²":
        area_cabo_1_mm=3.5

    if secao_cabo_1=="0,75mm²":
        area_cabo_1_mm=4.2

    if secao_cabo_1=="1mm²":
        area_cabo_1_mm=4.5

    if secao_cabo_1=="1,5mm²":
        area_cabo_1_mm=6.6

    if secao_cabo_1=="2,5mm²":
        area_cabo_1_mm=10.7

    if secao_cabo_1=="4mm²":
        area_cabo_1_mm=12.6

    if secao_cabo_1=="6mm²":
        area_cabo_1_mm=15.9

    if secao_cabo_1=="10mm²":
        area_cabo_1_mm=27.3

    if secao_cabo_1=="16mm²":
        area_cabo_1_mm=38.5

    if secao_cabo_1=="25mm²":
        area_cabo_1_mm=62.2
        
    if secao_cabo_1=="35mm²":
        area_cabo_1_mm=76.9

    if secao_cabo_1=="50mm²":
        area_cabo_1_mm=109.3

    if secao_cabo_1=="70mm²":
        area_cabo_1_mm=147.3

    if secao_cabo_1=="95mm²":
        area_cabo_1_mm=206

    if secao_cabo_1=="120mm²":
        area_cabo_1_mm=248.7

    if secao_cabo_1=="150mm²":
        area_cabo_1_mm=310.5
        
    if secao_cabo_1=="185mm²":
        area_cabo_1_mm=390.4

    if secao_cabo_1=="240mm²":
        area_cabo_1_mm=478.9

    if secao_cabo_1=="300mm²":
        area_cabo_1_mm=611.
        



    # ======================= cabo de 2 ==================================

    if secao_cabo_2=="Nao aplicavel":
        qtd_cabo_2=0
        area_cabo_2_mm=0

    if secao_cabo_2=="0,5mm²":
        area_cabo_2_mm=3.5

    if secao_cabo_2=="0,75mm²":
        area_cabo_2_mm=4.2

    if secao_cabo_2=="1mm²":
        area_cabo_2_mm=4.5

    if secao_cabo_2=="1,5mm²":
        area_cabo_2_mm=6.6

    if secao_cabo_2=="2,5mm²":
        area_cabo_2_mm=10.7

    if secao_cabo_2=="4mm²":
        area_cabo_2_mm=12.6

    if secao_cabo_2=="6mm²":
        area_cabo_2_mm=15.9

    if secao_cabo_2=="10mm²":
        area_cabo_2_mm=27.3

    if secao_cabo_2=="16mm²":
        area_cabo_2_mm=38.5

    if secao_cabo_2=="25mm²":
        area_cabo_2_mm=62.2
        
    if secao_cabo_2=="35mm²":
        area_cabo_2_mm=76.9

    if secao_cabo_2=="50mm²":
        area_cabo_2_mm=109.3

    if secao_cabo_2=="70mm²":
        area_cabo_2_mm=147.3

    if secao_cabo_2=="95mm²":
        area_cabo_2_mm=206

    if secao_cabo_2=="120mm²":
        area_cabo_2_mm=248.7

    if secao_cabo_2=="150mm²":
        area_cabo_2_mm=310.5
        
    if secao_cabo_2=="185mm²":
        area_cabo_2_mm=390.4

    if secao_cabo_2=="240mm²":
        area_cabo_2_mm=478.9

    if secao_cabo_2=="300mm²":
        area_cabo_2_mm=611.1


    # ======================= cabo de 2 ==================================
        

    # ======================= cabo de 3 ==================================

    if secao_cabo_3=="Nao aplicavel":
        qtd_cabo_3=0
        area_cabo_3_mm=0

    if secao_cabo_3=="0,5mm²":
        area_cabo_3_mm=3.5

    if secao_cabo_3=="0,75mm²":
        area_cabo_3_mm=4.2

    if secao_cabo_3=="1mm²":
        area_cabo_3_mm=4.5

    if secao_cabo_3=="1,5mm²":
        area_cabo_3_mm=6.6

    if secao_cabo_3=="2,5mm²":
        area_cabo_3_mm=10.7

    if secao_cabo_3=="4mm²":
        area_cabo_3_mm=12.6

    if secao_cabo_3=="6mm²":
        area_cabo_3_mm=15.9

    if secao_cabo_3=="10mm²":
        area_cabo_3_mm=27.3

    if secao_cabo_3=="16mm²":
        area_cabo_3_mm=38.5

    if secao_cabo_3=="25mm²":
        area_cabo_3_mm=62.2
        
    if secao_cabo_3=="35mm²":
        area_cabo_3_mm=76.9

    if secao_cabo_3=="50mm²":
        area_cabo_3_mm=109.3

    if secao_cabo_3=="70mm²":
        area_cabo_3_mm=147.3

    if secao_cabo_3=="95mm²":
        area_cabo_3_mm=206

    if secao_cabo_3=="120mm²":
        area_cabo_3_mm=248.7

    if secao_cabo_3=="150mm²":
        area_cabo_3_mm=310.5
        
    if secao_cabo_3=="185mm²":
        area_cabo_3_mm=390.4

    if secao_cabo_3=="240mm²":
        area_cabo_3_mm=478.9

    if secao_cabo_3=="300mm²":
        area_cabo_3_mm=611.1


    # ======================= cabo de 3 ==================================
    


    # ======================= cabo de 4 ==================================

    if secao_cabo_4=="Nao aplicavel":
        qtd_cabo_4=0
        area_cabo_4_mm=0

    if secao_cabo_4=="0,5mm²":
        area_cabo_4_mm=3.5

    if secao_cabo_4=="0,75mm²":
        area_cabo_4_mm=4.2

    if secao_cabo_4=="1mm²":
        area_cabo_4_mm=4.5

    if secao_cabo_4=="1,5mm²":
        area_cabo_4_mm=6.6

    if secao_cabo_4=="2,5mm²":
        area_cabo_4_mm=10.7

    if secao_cabo_4=="4mm²":
        area_cabo_4_mm=12.6

    if secao_cabo_4=="6mm²":
        area_cabo_4_mm=15.9

    if secao_cabo_4=="10mm²":
        area_cabo_4_mm=27.3

    if secao_cabo_4=="16mm²":
        area_cabo_4_mm=38.5

    if secao_cabo_4=="25mm²":
        area_cabo_4_mm=62.2
        
    if secao_cabo_4=="35mm²":
        area_cabo_4_mm=76.9

    if secao_cabo_4=="50mm²":
        area_cabo_4_mm=109.3

    if secao_cabo_4=="70mm²":
        area_cabo_4_mm=147.3

    if secao_cabo_4=="95mm²":
        area_cabo_4_mm=206

    if secao_cabo_4=="120mm²":
        area_cabo_4_mm=248.7

    if secao_cabo_4=="150mm²":
        area_cabo_4_mm=310.5
        
    if secao_cabo_4=="185mm²":
        area_cabo_4_mm=390.4

    if secao_cabo_4=="240mm²":
        area_cabo_4_mm=478.9

    if secao_cabo_4=="300mm²":
        area_cabo_4_mm=611.1


    # ======================= cabo de 4 ==================================
    

    # ======================= cabo de 5 ==================================

    if secao_cabo_5=="Nao aplicavel":
        qtd_cabo_5=0
        area_cabo_5_mm=0

    if secao_cabo_5=="0,5mm²":
        area_cabo_5_mm=3.5

    if secao_cabo_5=="0,75mm²":
        area_cabo_5_mm=4.2

    if secao_cabo_5=="1mm²":
        area_cabo_5_mm=4.5

    if secao_cabo_5=="1,5mm²":
        area_cabo_5_mm=6.6

    if secao_cabo_5=="2,5mm²":
        area_cabo_5_mm=10.7

    if secao_cabo_5=="4mm²":
        area_cabo_5_mm=12.6

    if secao_cabo_5=="6mm²":
        area_cabo_5_mm=15.9

    if secao_cabo_5=="10mm²":
        area_cabo_5_mm=27.3

    if secao_cabo_5=="16mm²":
        area_cabo_5_mm=38.5

    if secao_cabo_5=="25mm²":
        area_cabo_5_mm=62.2
        
    if secao_cabo_5=="35mm²":
        area_cabo_5_mm=76.9

    if secao_cabo_5=="50mm²":
        area_cabo_5_mm=109.3

    if secao_cabo_5=="70mm²":
        area_cabo_5_mm=147.3

    if secao_cabo_5=="95mm²":
        area_cabo__mm=206

    if secao_cabo_5=="120mm²":
        area_cabo_5_mm=248.7

    if secao_cabo_5=="150mm²":
        area_cabo_5_mm=310.5
        
    if secao_cabo_5=="185mm²":
        area_cabo_5_mm=390.4

    if secao_cabo_5=="240mm²":
        area_cabo_5_mm=478.9

    if secao_cabo_5=="300mm²":
        area_cabo_5_mm=611.1


    # ======================= cabo de 5 ==================================
        


    # ======================= cabo de 5 ==================================

    if secao_cabo_6=="Nao aplicavel":
        qtd_cabo_6=0
        area_cabo_6_mm=0

    if secao_cabo_6=="0,5mm²":
        area_cabo_6_mm=3.5

    if secao_cabo_6=="0,75mm²":
        area_cabo_6_mm=4.2

    if secao_cabo_6=="1mm²":
        area_cabo_6_mm=4.5

    if secao_cabo_6=="1,5mm²":
        area_cabo_6_mm=6.6

    if secao_cabo_6=="2,5mm²":
        area_cabo_6_mm=10.7

    if secao_cabo_6=="4mm²":
        area_cabo_6_mm=12.6

    if secao_cabo_6=="6mm²":
        area_cabo_6_mm=15.9

    if secao_cabo_6=="10mm²":
        area_cabo_6_mm=27.3

    if secao_cabo_6=="16mm²":
        area_cabo_6_mm=38.5

    if secao_cabo_6=="25mm²":
        area_cabo_6_mm=62.2
        
    if secao_cabo_6=="35mm²":
        area_cabo_6_mm=76.9

    if secao_cabo_6=="50mm²":
        area_cabo_6_mm=109.3

    if secao_cabo_6=="70mm²":
        area_cabo_6_mm=147.3

    if secao_cabo_6=="95mm²":
        area_cabo_6_mm=206

    if secao_cabo_6=="120mm²":
        area_cabo_6_mm=248.7

    if secao_cabo_6=="150mm²":
        area_cabo_6_mm=310.5
        
    if secao_cabo_6=="185mm²":
        area_cabo_6_mm=390.4

    if secao_cabo_6=="240mm²":
        area_cabo_6_mm=478.9

    if secao_cabo_6=="300mm²":
        area_cabo_6_mm=611.1


    # ======================= cabo de 5 ==================================
    

    # calculando area toda dos cabos
    area_total=area_cabo_1_mm*qtd_cabo_1+area_cabo_2_mm*qtd_cabo_2+area_cabo_3_mm*qtd_cabo_3+area_cabo_4_mm*qtd_cabo_4+area_cabo_5_mm*qtd_cabo_5+area_cabo_6_mm*qtd_cabo_6
    
    print(f"\n\nQuantidade cabo 1: {qtd_cabo_1}\n Area cabo 1: {area_cabo_1_mm}\n taxa de ocupacao: {taxa_maxima_ocupacao}")
    print(f"\n\nArea total={area_total}\n\n")
    raio_total=math.sqrt(area_total/math.pi)
    print(f"\n\nraio total={raio_total}\n\n")

    diametro_total=2*raio_total
    print(f"\n\nDiametro total={diametro_total}\n\n")

    global eletroduto_aplicavel
    eletroduto_aplicavel=""

    #if  diametro_total<=15*taxa_maxima_ocupacao:
    #    eletroduto_aplicavel="1/2''"

    if  diametro_total<=(20*taxa_maxima_ocupacao):
        eletroduto_aplicavel="3/4''"

    elif  diametro_total<=(25*taxa_maxima_ocupacao):
        eletroduto_aplicavel="1''"


    elif  diametro_total<=32*taxa_maxima_ocupacao:
        eletroduto_aplicavel="1 1/4''"

    elif  diametro_total<=40*taxa_maxima_ocupacao:
        eletroduto_aplicavel="1 1/2''"

    elif  diametro_total<=50*taxa_maxima_ocupacao:
        eletroduto_aplicavel="2''"

    elif  diametro_total<=60*taxa_maxima_ocupacao:
        eletroduto_aplicavel="2 1/2''"

    elif  diametro_total<=75*taxa_maxima_ocupacao:
        eletroduto_aplicavel="3''"

    elif  diametro_total<=100*taxa_maxima_ocupacao:
        eletroduto_aplicavel="4''"
    
    else:
        st.error("Insira os dados novamente! Não foi possível encontrar um eletroduto para este caso!!")


    texto_explicativo=f"Eletroduto aplicável: {eletroduto_aplicavel}\nQuantidade de cabos: {quantidade_total_cabos}\nTaxa de ocupação aplicada: {taxa_maxima_ocupacao*100}%\n Diâmetro total(mm):{round(diametro_total,2)}"
    

    # dados = {
    # 'Item': ['Eletroduto aplicável','Quantidade de cabos','Taxa de ocupação aplicada(%)','Diâmetro total(mm)'],
    # 'Valor': [eletroduto_aplicavel,quantidade_total_cabos,taxa_maxima_ocupacao*100,round(diametro_total,2)]}


    dados = [['Eletroduto aplicável',eletroduto_aplicavel],
              ['Quantidade de cabos',quantidade_total_cabos],
              ['Taxa de ocupação aplicada(%)',taxa_maxima_ocupacao*100],
              ['Diâmetro total(mm)',round(diametro_total,2)]]
    
    dados_cabos=[]
    if secao_cabo_1!="Não aplicavel" and qtd_cabo_1 !=0:
        lista_secao_1=[secao_cabo_1,area_cabo_1_mm,qtd_cabo_1]
        dados_cabos.append(lista_secao_1)

        lista_secao_1_tab_dados=[f"Quantidade cabo {secao_cabo_1}",qtd_cabo_1]
        dados.append(lista_secao_1_tab_dados)

    if secao_cabo_2!="Não aplicavel"and qtd_cabo_2 !=0:
        lista_secao_2=[secao_cabo_2,area_cabo_2_mm,qtd_cabo_2]
        dados_cabos.append(lista_secao_2)

        lista_secao_2_tab_dados=[f"Quantidade cabo {secao_cabo_2}",qtd_cabo_2]
        dados.append(lista_secao_2_tab_dados)

    if secao_cabo_3!="Não aplicavel" and qtd_cabo_3 !=0:
        lista_secao_3=[secao_cabo_3,area_cabo_3_mm,qtd_cabo_3]
        dados_cabos.append(lista_secao_3)

        lista_secao_3_tab_dados=[f"Quantidade cabo {secao_cabo_3}",qtd_cabo_3]
        dados.append(lista_secao_3_tab_dados)

    if secao_cabo_4!="Não aplicavel"and qtd_cabo_4 !=0:
        lista_secao_4=[secao_cabo_4,area_cabo_4_mm,qtd_cabo_4]
        dados_cabos.append(lista_secao_4)

        lista_secao_4_tab_dados=[f"Quantidade cabo {secao_cabo_4}",qtd_cabo_4]
        dados.append(lista_secao_4_tab_dados)

    if secao_cabo_5!="Não aplicavel"and qtd_cabo_5 !=0:
        lista_secao_5=[secao_cabo_5,area_cabo_5_mm,qtd_cabo_5]
        dados_cabos.append(lista_secao_5)

        lista_secao_5_tab_dados=[f"Quantidade cabo {secao_cabo_5}",qtd_cabo_5]
        dados.append(lista_secao_5_tab_dados)

    if secao_cabo_6!="Não aplicavel" and qtd_cabo_6 !=0:
        lista_secao_6=[secao_cabo_6,area_cabo_6_mm,qtd_cabo_6]
        dados_cabos.append(lista_secao_6)

        lista_secao_6_tab_dados=[f"Quantidade cabo {secao_cabo_6}",qtd_cabo_6]
        dados.append(lista_secao_6_tab_dados)
        

    # 'Item': ['Eletroduto aplicável','Quantidade de cabos','Taxa de ocupação aplicada(%)','Diâmetro total(mm)'],
    # 'Valor': [eletroduto_aplicavel,quantidade_total_cabos,taxa_maxima_ocupacao*100,round(diametro_total,2)]}

    tabela = pd.DataFrame(dados,columns=["Item","Valor"])
    # Supondo que 'df' é o seu DataFrame

    tabela_cabos_selecionado=pd.DataFrame(dados_cabos,columns=["Seção Nominal(mm²)","Seção transv.(mm²)","Quantidade"])

    with coluna1:

        st.header("Resultados")
        st.dataframe(tabela,width=300)

    with coluna2:
        st.header("Tabela Cabos selecionados")
        st.dataframe(tabela_cabos_selecionado,use_container_width=True)


        


def calcular_taxa_ocupacao():
    global taxa_maxima_ocupacao
    global quantidade_total_cabos
    quantidade_total_cabos=qtd_cabo_1+qtd_cabo_2+qtd_cabo_3+qtd_cabo_4+qtd_cabo_5+qtd_cabo_6

    if quantidade_total_cabos==1:
        taxa_maxima_ocupacao=0.53 # 53%
    if quantidade_total_cabos==2:
        taxa_maxima_ocupacao=0.31 #31%
    if quantidade_total_cabos>2:
        taxa_maxima_ocupacao=0.40 #40%


global qtd_cabo_1
global qtd_cabo_2
global qtd_cabo_3
global qtd_cabo_4
global qtd_cabo_5
global qtd_cabo_6




st.set_page_config(
    page_title="Dimensionamento Eletrodutos",
)
st.title("Dimensionamento eletrodutos")

lista_secao_cabos=["Não aplicavel","0,5mm²","0,75mm²","1mm²","1,5mm²","2,5mm²","4mm²","6mm²","10mm²","16mm²","25mm²","35mm²","50mm²","95mm²","120mm²","150mm²","185mm²","240mm²","300mm²"]
coluna1, coluna2=st.columns(2)

with coluna1:
    #form1=st.form(key="textos",clear_on_submit=False)

    st.subheader("Seção Cabo(mm²)")

    secao_cabo_1=st.selectbox("Seção cabo 1:",lista_secao_cabos,key="secao_cabo_1",placeholder="Escolha uma opção")
    st.divider()
    secao_cabo_2=st.selectbox("Seção cabo 2:",lista_secao_cabos,key="secao_cabo_2",placeholder="Escolha uma opção")
    st.divider()
    secao_cabo_3=st.selectbox("Seção cabo 3:",lista_secao_cabos,key="secao_cabo_3",placeholder="Escolha uma opção")
    st.divider()
    secao_cabo_4=st.selectbox("Seção cabo 4:",lista_secao_cabos,key="secao_cabo_4",placeholder="Escolha uma opção")
    st.divider()
    secao_cabo_5=st.selectbox("Seção cabo 5:",lista_secao_cabos,key="secao_cabo_5",placeholder="Escolha uma opção")
    st.divider()
    secao_cabo_6=st.selectbox("Seção cabo 6:",lista_secao_cabos,key="secao_cabo_6",placeholder="Escolha uma opção")
    st.divider()

    st.button("Calcular Eletroduto",on_click=calcula_eletroduto,key="btn_calcular_eletroduto",)

with coluna2:
    st.subheader("Quantidade de Cabos")
    qtd_cabo_1=st.number_input("Quantidade cabo 1",min_value=0,max_value=1000,step=1,key="qtd_cabo_1")
    if secao_cabo_1=="Não aplicavel" and qtd_cabo_1>0:
        st.warning(":rotating_light: Informe a seção do cabo 1")
    st.divider()
    qtd_cabo_2=st.number_input("Quantidade cabo 2",min_value=0,max_value=1000,step=1,key="qtd_cabo_2")
    if secao_cabo_2=="Não aplicavel" and qtd_cabo_2>0:
        st.warning(":rotating_light: Informe a seção do cabo 2")
    st.divider()
    qtd_cabo_3=st.number_input("Quantidade cabo 3",min_value=0,max_value=1000,step=1,key="qtd_cabo_3")
    if secao_cabo_3=="Não aplicavel" and qtd_cabo_3>0:
        st.warning(":rotating_light: Informe a seção do cabo 3")
    st.divider()
    qtd_cabo_4=st.number_input("Quantidade cabo 4",min_value=0,max_value=1000,step=1,key="qtd_cabo_4")
    if secao_cabo_4=="Não aplicavel" and qtd_cabo_4>0:
        st.warning(":rotating_light: Informe a seção do cabo 4")
    st.divider()
    qtd_cabo_5=st.number_input("Quantidade cabo 5",min_value=0,max_value=1000,step=1,key="qtd_cabo_5")
    if secao_cabo_5=="Não aplicavel" and qtd_cabo_5>0:
        st.warning(":rotating_light: Informe a seção do cabo 5")
    st.divider()
    qtd_cabo_6=st.number_input("Quantidade cabo 6",min_value=0,max_value=1000,step=1,key="qtd_cabo_6")
    if secao_cabo_6=="Não aplicavel" and qtd_cabo_6>0:
        st.warning(":rotating_light: Informe a seção do cabo 6")
    st.divider()

    
    #st.button("Calcular Eletroduto",on_click=calcula_eletroduto,key="btn_calcular_eletroduto",)
        

st.header("Como o programa funciona?\n")
st.write("Os valores das seções dos eletrodutos estão em conformidade com a tabela disponível no site Mundo da Elétrica. Nessa tabela, é possível consultar os diâmetros internos nominais correspondentes a cada seção específica.")
st.image("https://www.mundodaeletrica.com.br/y/1293/conversao-polegada-milimetro-720.jpg",caption="Tabela eletrodutos (Fonte: Mundo da elétrica)",width=400)
st.write("Os valores na seção transversal dos cabos levam em consideração a área que abrange não apenas a espessura dos próprios cabos, mas também a camada de isolamento que os envolve. Essa abordagem visa proporcionar uma avaliação mais precisa no dimensionamento dos eletrodutos, considerando não apenas o núcleo condutor, mas também a totalidade das dimensões que compõem a seção transversal dos cabos. Os dados dos cabos foram retirados da Fabricante SIL, como mostra a tabela abaixo.")

st.image("https://www.sil.com.br/media/103616/FlexSIL750V.png",caption="Tabela eletrodutos (Fonte: SIL cabos elétricos)",width=400)



# ------------- VALIDANDO AS ENTRDAS------------

global eletroduto_aplicavel

global area_cabo_1_mm
global area_cabo_2_mm
global area_cabo_3_mm
global area_cabo_4_mm
global area_cabo_5_mm
global area_cabo_6_mm

area_cabo_1_mm=0
area_cabo_2_mm=0
area_cabo_3_mm=0
area_cabo_4_mm=0
area_cabo_5_mm=0
area_cabo_6_mm=0




# ******* determinando taxa maxima de ocupacao******
# De acordo com a norma NBR5410, a taxa máxima de ocupação de eletrodutos em relação à área da seção transversal
# não deve ser superior a 53% para um condutor ou cabo, 31% para dois condutores ou cabos e 40% para três ou mais condutores ou cabos.

global taxa_maxima_ocupacao
taxa_maxima_ocupacao=0.4

global quantidade_total_cabos                               
quantidade_total_cabos=0





        
