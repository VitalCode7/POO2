import streamlit as st
from service import Service
import time
from datetime import datetime

class RegistrarAtendimentoUI:
    def main():
        st.header("Registrar atendimeto")
        atendimentos = Service.atendimento_listar()
        atendimento = st.selectbox("Selecione o atendimento", atendimentos)
        data = st.text_input("Informe a Data", datetime.strftime(datetime.now(), "%d/%m/%Y"))
        queixa_principal = st.text_input("Informe a queixa principal")
        historico_saude = st.text_input("Informe o histórico de saúde")
        avaliacao = st.text_input("Informe a avaliação")
        prescricao = st.text_input("Informe a prescrição")
        horarios = Service.horario_listar()
        horario = st.selectbox("Selecione o horário", horarios)
        pago = st.text_input("Pago")
        if st.button("Atualizar"):
            id_atendimento = atendimento.get_id()
            Service.atendimento_atualizar(id_atendimento, data, queixa_principal, historico_saude, avaliacao, prescricao, horario.get_id())
            st.success("Atendimento atualizado com sucesso")
            time.sleep(2)
            st.rerun()