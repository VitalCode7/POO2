import streamlit as st
import time
from service import Service

class PagarAtendimentoUI:
    def main():
        st.header("Pagar Atendimento")
        atendimentos = Service.atendimento_listar()
        meus_atendimentos = []
        for a in atendimentos:
            horario = Service.horario_listar_id(a.get_id_horario())
            if horario != None:
                if horario.get_id_cliente() == st.session_state["usuario_id"]:
                    if a.get_pago() == False:
                        meus_atendimentos.append(a)

        if len(meus_atendimentos) == 0:
            st.write("Nenhum atendimento a pagar")
        else:
            atendimento = st.selectbox("Informe o atendimento", meus_atendimentos)
            st.write("Total:", atendimento.get_total())
            if st.button("Pagar"):
                Service.atendimento_atualizar(atendimento.get_id(), atendimento.get_data(), atendimento.get_queixa_principal() ,atendimento.get_historico_saude(), atendimento.get_avaliacao(), atendimento.get_prescricao(), atendimento.get_id_horario(), atendimento.get_total(), True)
                st.success("Atendimento pago")
                time.sleep(2)
                st.rerun()