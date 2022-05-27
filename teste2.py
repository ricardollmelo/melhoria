from ctypes import alignment
from gettext import install
from bcb import sgs
from pyparsing import Opt
import streamlit as st
import bcb
import pandas as pd
import numpy as np 

#Definindo os títulos

st.set_page_config(
    page_title = 'Dashboard Macroeconômico',
    page_icon = '📊',
    layout = 'wide')


st.markdown("##  📈 Painel com os principais indicadores econômicos")
escolha = st.selectbox('Selecione sua categoria de análise',
 ('Escolha seu tema de análise','Preços', 'Desemprego', 'Juros'))

#Importando dados

selic = sgs.get({'selic': 432}, start='2010-01-01')
ipca = sgs.get({'IPCA': 433}, start='2010-01-01')
desem = sgs.get({'Taxa de desemprego (%)': 24369}, start='2012-03-01')
inpc = sgs.get({'INPC': 188}, start='2010-01-01')
igpm = sgs.get({'IGP-M': 189}, start='2010-01-01')
ipca15 = sgs.get({'IPCA-15': 7478}, start='2010-01-01')
incc = sgs.get({'INCC': 7457}, start='2010-01-01')
ic = sgs.get({'IC-BR': 7457}, start='2010-01-01')

#Criando layout
if escolha == "Juros":
    st.markdown('**SELIC**')
    chart_data = selic
    st.line_chart(chart_data)
if escolha == "Preços":
    st.markdown('**IPCA**')
    chart_data2 = ipca
    st.line_chart(chart_data2)
    st.markdown('**IPCA-15**')
    chart_data2 = ipca15
    st.line_chart(chart_data2)
if escolha == "Desemprego":
    st.markdown('**Taxa de desemprego**')
    chart_data2 = desem
    st.line_chart(chart_data2)

grafico1, grafico2, grafico3, grafico4 = st.columns(4)

with grafico1:
    st.markdown('**SELIC**')
    chart_data = selic
    st.line_chart(chart_data)
    st.markdown('**IGP-M**')
    chart_data2 = igpm
    st.line_chart(chart_data2)

with grafico2:
    st.markdown('**IPCA**')
    chart_data2 = ipca
    st.line_chart(chart_data2)
    st.markdown('**IPCA-15**')
    chart_data2 = ipca15
    st.line_chart(chart_data2)

with grafico3:
    st.markdown('**INPC**')
    chart_data2 = inpc
    st.line_chart(chart_data2)
    st.markdown('**INCC**')
    chart_data2 = incc
    st.line_chart(chart_data2)
with grafico4:
    st.markdown('**Taxa de desemprego**')
    chart_data2 = desem
    st.line_chart(chart_data2)
    st.markdown('**Índice de commodities**')
    chart_data2 = ic
    st.line_chart(ic)


