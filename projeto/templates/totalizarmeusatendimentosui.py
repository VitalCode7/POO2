import streamlit as st
from service import Service
import time

class TotalizarMeusAtendimentosUI:
    def main():
        st.header("Totalizar meus atendimentos")
        data_inicial = st.text_input("Informe a data inicial")
        data_final = st.text_input("Informe a data final")
        
        lista_periodica = Service.totalizar_atendimentos_profissionais(data_inicial, data_final, st.session_state["usuario_id"])
        
        dados = {
            "Dia": i for i in lista_periodica,
            "Atendimentos": ,
            "quantidade_de_atendimentos": lista_periodica,
        }

        # Gráfico de barras simples
        st.bar_chart(dados, x="Meses", y="Vendas")