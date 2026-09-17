from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterhorarioui import ManterHorarioUI
from templates.manterprofissionalui import ManterProfissionalUI
from templates.manteratendimentoui import ManterAtendimentoUI
from templates.manterconvenioui import ManterConvenioUI
import streamlit as st

class IndexUI:
    def main():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horários", "Profissionais", "Atendimentos", "Convênios"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == "Horários": ManterHorarioUI.main()
        if op == "Profissionais": ManterProfissionalUI.main()
        if op == "Atendimentos": ManterAtendimentoUI.main()
        if op == "Convênios": ManterConvenioUI.main()

IndexUI.main()