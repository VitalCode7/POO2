from datetime import datetime
import time
import pandas as pd
from service import Service
import streamlit as st


class ManterAtendimentoUI:

  def main():
    st.header("Cadastro de Atendimentos")
    tab1, tab2, tab3, tab4 = st.tabs(
        ["Listar", "Inserir", "Atualizar", "Excluir"]
    )
    with tab1:
      ManterAtendimentoUI.listar()
    with tab2:
      ManterAtendimentoUI.inserir()
    with tab3:
      ManterAtendimentoUI.atualizar()
    with tab4:
      ManterAtendimentoUI.excluir()

  def listar():
    atendimentos = Service.atendimento_listar()
    if len(atendimentos) == 0:
      st.write("Nenhum atendimento cadastrado")
    else:
      dic = []
      for obj in atendimentos:
        horario = Service.horario_listar_id(obj.get_id_horario())
        horario_str = (
            horario.get_data().strftime("%d/%m/%Y %H:%M")
            if horario != None
            else "Nenhum"
        )
        dic.append({
            "id": obj.get_id(),
            "data": obj.get_data(),
            "queixa_principal": obj.get_queixa_principal(),
            "historico_saude": obj.get_historico_saude(),
            "avaliacao": obj.get_avaliacao(),
            "prescricao": obj.get_prescricao(),
            "horário": horario_str,
        })
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    horarios = Service.horario_listar()
    data = st.text_input(
        "Informe a data e horário do atendimento",
        datetime.now().strftime("%d/%m/%Y %H:%M"),
    )
    queixa = st.text_area("Queixa Principal")
    historico = st.text_area("Histórico de Saúde")
    avaliacao = st.text_area("Avaliação")
    prescricao = st.text_area("Prescrição")
    horario = st.selectbox("Informe o horário agendado", horarios, index=None)

    if st.button("Inserir"):
      id_horario = None
      if horario != None:
        id_horario = horario.get_id()
      Service.atendimento_inserir(
          datetime.strptime(data, "%d/%m/%Y %H:%M"),
          queixa,
          historico,
          avaliacao,
          prescricao,
          id_horario,
      )
      st.success("Atendimento inserido com sucesso")
      time.sleep(2)
      st.rerun()

  def atualizar():
    atendimentos = Service.atendimento_listar()
    if len(atendimentos) == 0:
      st.write("Nenhum atendimento cadastrado")
    else:
      horarios = Service.horario_listar()
      op = st.selectbox("Atualização de Atendimentos", atendimentos)
      data = st.text_input(
          "Informe a nova data e horário",
          op.get_data().strftime("%d/%m/%Y %H:%M"),
      )
      queixa = st.text_area(
          "Informe a nova queixa principal", op.get_queixa_principal()
      )
      historico = st.text_area(
          "Informe o novo histórico de saúde", op.get_historico_saude()
      )
      avaliacao = st.text_area("Informe a nova avaliação", op.get_avaliacao())
      prescricao = st.text_area(
          "Informe a nova prescrição", op.get_prescricao()
      )

      id_h = (
          None
          if op.get_id_horario() in [0, None]
          else op.get_id_horario()
      )
      idx_h = next(
          (i for i, h in enumerate(horarios) if h.get_id() == id_h), None
      )
      horario = st.selectbox("Informe o novo horário", horarios, index=idx_h)

      if st.button("Atualizar"):
        id_horario = None
        if horario != None:
          id_horario = horario.get_id()
        Service.atendimento_atualizar(
            op.get_id(),
            datetime.strptime(data, "%d/%m/%Y %H:%M"),
            queixa,
            historico,
            avaliacao,
            prescricao,
            id_horario,
        )
        st.success("Atendimento atualizado com sucesso")
        time.sleep(2)
        st.rerun()

  def excluir():
    atendimentos = Service.atendimento_listar()
    if len(atendimentos) == 0:
      st.write("Nenhum atendimento cadastrado")
    else:
      op = st.selectbox("Exclusão de Atendimentos", atendimentos)
      if st.button("Excluir"):
        Service.atendimento_excluir(op.get_id())
        st.success("Atendimento excluído com sucesso")
        time.sleep(2)
        st.rerun()