import streamlit as st
from service import Service
import time
from datetime import datetime

class RegistrarAtendimentoUI:
    def main():
        st.header("Registrar Atendimento")
        horarios = Service.profissional_visualizar_agenda(st.session_state["usuario_id"])
        atendimentos = Service.atendimento_listar()
        horarios_filtrados = []
        for h in horarios:
            if h.get_confirmado() == True:
                usado = False
                for a in atendimentos:
                    if a.get_id_horario() == h.get_id():
                        usado = True
                if usado == False:
                    horarios_filtrados.append(h)
        horarios = horarios_filtrados

        if len(horarios) == 0:
            st.write("Nenhum atendimento disponível")
        else:
            horario = st.selectbox("Informe o horário", horarios)
            data = st.text_input("Informe a data e horário do atendimento", datetime.now().strftime("%d/%m/%Y %H:%M"))
            queixa_principal = st.text_input("Informe a queixa principal")
            historico_saude = st.text_input("Informe o histórico de saúde")
            avaliacao = st.text_input("Informe a avaliação")
            prescricao = st.text_input("Informe a prescrição")
            servicos = Service.servico_listar()
            servico = st.selectbox("Informe o serviço realizado", servicos)
            qtd = st.number_input("Quantidade", min_value=1, step=1)

            if st.button("Registrar"):
                total = servico.get_valor() * qtd
                Service.atendimento_inserir(
                    datetime.strptime(data, "%d/%m/%Y %H:%M"), queixa_principal, historico_saude, avaliacao, prescricao, horario.get_id(), total, False)
                atendimento = Service.atendimento_listar()[-1]
                Service.atendimentoitem_inserir(atendimento.get_id(), servico.get_id(), qtd, servico.get_valor())
                st.success("Atendimento registrado")
                time.sleep(2)
                st.rerun()