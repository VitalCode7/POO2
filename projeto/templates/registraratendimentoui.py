import streamlit as st
import pandas as pd
from service import Service
import time
from datetime import datetime

class RegistrarAtendimentoUI:
    def main():
        st.header("Atendimentos")
        tab1, tab2 = st.tabs(["Inserir", "Valores"]) # Abas
        with tab1: RegistrarAtendimentoUI.inserir()
        with tab2: RegistrarAtendimentoUI.valores()

    def inserir():
        data = st.text_input("Informe a Data", datetime.strftime(datetime.now(), "%d/%m/%Y"))
        queixa_principal = st.text_input("Informe a queixa principal")
        historico_saude = st.text_input("Informe o histórico de saúde")
        avaliacao = st.text_input("Informe a avaliação")
        prescricao = st.text_input("Informe a prescrição")
        horarios = Service.horarios_atendimento(st.session_state["usuario_id"])

        horario = st.selectbox("Selecione o horário", horarios)

        pago = st.checkbox("Pago")
        if st.button("Inserir"):
            Service.atendimento_inserir(datetime.strptime(data, "%d/%m/%Y"), queixa_principal, historico_saude, avaliacao, prescricao, horario.get_id())
            st.success("Atendimento atualizado com sucesso")
            time.sleep(2)
            st.rerun()
    
    def valores(): 
        atendimentos = Service.atendimento_listar()
        servicos = Service.servico_listar()
        atendimento = st.selectbox("Selecione um atendimento", atendimentos)
        servico = st.selectbox("Selecione um serviço", servicos)
        qnt = st.number_input("Informe a quantidade", min_value = 1, step = 1)
        valor = st.number_input("Valor", servico.get_valor() * qnt, disabled = True)
        if st.button('Enviar'):
            try: 
                Service.atendimento_itens_inserir(atendimento.get_id(), servico.get_id(), qnt, valor)
                st.success("Registro realizado com sucesso")
            except ValueError: 
                st.error("Não foi possível fazer as alterações!")
            finally: 
                time.sleep(2)
                st.rerun()