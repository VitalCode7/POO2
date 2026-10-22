import pandas as pd
import streamlit as st
from service import Service


class ListarHorariosConfirmadosHojeUI:
    def main():
        st.header("Horários confirmados hoje")
        horarios = Service.horario_listar_confirmados_hoje()
        if len(horarios) == 0:
            st.write("Nenhum horário confirmado para hoje")
            return

        dados = []
        for horario in horarios:
            cliente = Service.cliente_listar_id(horario.get_id_cliente())
            servico = Service.servico_listar_id(horario.get_id_servico())
            profissional = Service.profissional_listar_id(horario.get_id_profissional())
            dados.append({
                "id": horario.get_id(),
                "data e hora": horario.get_data(),
                "cliente": cliente.get_nome() if cliente is not None else "Não encontrado",
                "serviço": servico.get_descricao() if servico is not None else "Não encontrado",
                "profissional": profissional.get_nome() if profissional is not None else "Não encontrado",
            })

        st.dataframe(pd.DataFrame(dados))