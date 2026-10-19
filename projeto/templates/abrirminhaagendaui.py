import streamlit as st
from service import Service
import time
import pandas as pd
from datetime import datetime

class AbrirMinhaAgendaUI: 
    def main(): 
        st.header("Abrir minha agenda")
        tab1, tab2 = st.tabs(["Listar", "Inserir"])
        with tab1: AbrirMinhaAgendaUI.listar()
        with tab2: AbrirMinhaAgendaUI.inserir()

    def listar(): 
        agendamentos = Service.horario_listar_disponiveis(st.session_state["usuario_id"])
        if len(agendamentos) == 0: st.write("Nenhum agendamento registrado")
        else:
            list_dic = []
            for obj in agendamentos: 
                cliente = Service.cliente_listar_id(obj.get_id_cliente())
                servico = Service.servico_listar_id(obj.get_id_servico())
                profissional = Service.profissional_listar_id(obj.get_id_profissional())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_descricao()
                if profissional != None: profissional = profissional.get_nome()
                list_dic.append({"id" : obj.get_id(), "data" : obj.get_data(),
                "confirmado" : obj.get_confirmado(), "cliente" : cliente,
                "serviço" : servico})
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
        
    def inserir(): 
        data = st.text_input("Informe a data no formato dd/mm/aaaa", datetime.now().strftime("%d/%m/%Y"))
        horario_inicio = st.text_input("Informe o horário inicial no formato HH:MM")
        horario_fim = st.text_input("Informe o horário final no formato HH:MM")
        intervalo = st.text_input("Informe o intervalo entre cada consulta")
        if st.button("Abrir agenda"): 
            Service.horario_abrir_minha_agenda(data, horario_inicio, horario_fim, int(intervalo), st.session_state["usuario_id"])
            st.success("Horários inseridos com sucesso")
            time.sleep(2)
            st.rerun()