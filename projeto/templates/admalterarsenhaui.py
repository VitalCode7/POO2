import streamlit as st
from service import Service
import time

class ADMAlterarSenhaUI:
    def main():
        st.header("Alterar senha")
        op = Service.cliente_listar_id(st.session_state["usuario_id"])
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
        if st.button("Atualizar"): 
            id = op.get_id()
            Service.cliente_atualizar(id, op.get_nome(), op.get_email(), op.get_fone(), senha)
            st.success("Senha atualizada com sucesso")
            time.sleep(2)
            st.rerun()