import streamlit as st
from service import Service
import time

class ConfirmarServicoUI:
    def main():
        st.header("Confirmar Serviço")
        horarios = Service.profissional_visualizar_agenda(st.session_state["usuario_id"])
        horarios_filtrados = []
        for h in horarios:
            if h.get_id_cliente() != None and h.get_confirmado() == False:
                horarios_filtrados.append(h)
        horarios = horarios_filtrados
        if len(horarios) == 0: st.write("Nenhuma serviço a confirmar")
        else:
            horario = st.selectbox("Informe o horário", horarios)
            cliente = Service.cliente_listar_id(horario.get_id_cliente())
            st.selectbox("Cliente", [cliente], disabled=True)
            if st.button("Confirmar"):
                Service.horario_atualizar(horario.get_id(), horario.get_data(), True, horario.get_id_cliente(), horario.get_id_servico(), horario.get_id_profissional())
                st.success("Serviço confirmado")
                time.sleep(2)
                st.rerun()