import pandas as pd
import streamlit as st
from service import Service


class ListarAgendaProfissionalUI:
    def main():
        st.header("Agenda do profissional")
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
            return

        profissional = st.selectbox("Selecione o profissional", profissionais)
        horarios = Service.horario_listar_profissional(profissional.get_id())
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado na agenda deste profissional")
            return

        dados = []
        for horario in horarios:
            cliente = Service.cliente_listar_id(horario.get_id_cliente())
            servico = Service.servico_listar_id(horario.get_id_servico())
            dados.append({
                "id": horario.get_id(),
                "data e hora": horario.get_data(),
                "cliente": cliente.get_nome() if cliente is not None else "não encontrado",
                "serviço": servico.get_descricao() if servico is not None else "não encontrado",
            })

        st.dataframe(pd.DataFrame(dados))
