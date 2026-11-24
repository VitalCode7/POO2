import streamlit as st
import pandas as pd
from service import Service
import time
from datetime import datetime

class FazerPagamentosUI:
    def main():
        st.header("Fazer pagamentos")
        atendimentos_gerais = Service.atendimento_listar()
        atendimentos = []
        for i in atendimentos_gerais:
            horario = Service.horario_listar_id(i.get_id_horario())
            if i.get_pago() == False and horario.get_id_cliente() == st.session_state["usuario_id"]: 
                atendimentos.append(i)

        if len(atendimentos) == 0: st.write("Sem atendimentos disponíveis")
        else: 
            atendimento = st.selectbox("Selecione o atendimento", atendimentos)
            st.write(f"O valor é final é de: R$ {Service.atendimento_calcular_total(atendimento.get_id()):.2f}")
            if st.button("Pagar"):
                Service.pagar_atendimento(atendimento)
                st.success("Atendimento pago com sucesso")
                time.sleep(2)
                st.rerun()