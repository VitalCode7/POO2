import streamlit as st
import pandas as pd
import time
from service import Service

class AdminUI: 
    def main():
        admin = Service.cliente_listar_id(Service.get_id_admin())
        st.subheader("Alteração de senha")
        st.text_input('Nome', admin.get_nome(), disabled = True)
        st.text_input('Email', admin.get_email(), disabled = True)
        st.text_input('Telefone', admin.get_fone(), disabled = True)
        senha = st.text_input('Nova senha', admin.get_senha())
        if st.button("Atualizar"):
            Service.cliente_atualizar(admin.get_nome(), admin.get_email(), admin.get_fone(), senha)
            st.success("Cliente atualizado com sucesso")
            time.sleep(2)
            st.rerun()