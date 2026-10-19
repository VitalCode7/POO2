import streamlit as st
from service import Service
import time
import pandas as pd
from datetime import datetime

class ConfirmarServicoUI: 
    def main(): 
        st.header("Confirmar Serviços")
        horarios = Service.horario_listar_confirmacao(st.session_state["usuario_id"])
        if len(horarios) == 0: st.write("Nenhum horário disponível para confirmação")
        else: 
            horario = st.selectbox("Selecione o horário", horarios)
            cliente = st.selectbox("Cliente", Service.cliente_listar_id(horario.get_id_cliente()), disabled = True)
            if st.button("Confirmar"): 
                Service.horario_atualizar(horario.get_id(), horario.get_data(), True, horario.get_id_cliente(), horario.get_id_servico(), horario.get_id_profissional())
                st.success("Confirmado!")
                time.sleep(2)
                st.rerun()