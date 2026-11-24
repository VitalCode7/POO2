import streamlit as st
import pandas as pd
from service import Service
import time
from datetime import datetime

class ListarAgendaProfissionalUI:
    def main():
        st.header("Agenda dos profissionais")
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0: st.write("Sem profissionais disponíveis")
        else:
            profissional = st.selectbox("Selecione o profissional", profissionais)
            horarios = Service.agenda_profissionais(profissional.get_id())
            if horarios == None: st.write("Sem horários disponíveis")
            else: 
                dic = []
                for obj in horarios:
                    cliente = Service.cliente_listar_id(obj.get_id_cliente())
                    servico = Service.servico_listar_id(obj.get_id_servico())
                    if cliente != None: cliente = cliente.get_nome()
                    if servico != None: servico = servico.get_descricao()
                    dic.append({"id" : obj.get_id(), "data" : obj.get_data(),
                    "cliente" : cliente,
                    "serviço" : servico})
                df = pd.DataFrame(dic)
                st.dataframe(df)