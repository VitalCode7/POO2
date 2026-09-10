from projeto.templates.q6_manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterhorarioui import ManterHorarioUI
from templates.q5_manterconvenioui import ManterConvenioUI
import streamlit as st

class IndexUI:
    def main():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horários", "Convênios"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == "Horários": ManterHorarioUI.main()
        if op == "Convênios": ManterConvenioUI.main()

IndexUI.main()