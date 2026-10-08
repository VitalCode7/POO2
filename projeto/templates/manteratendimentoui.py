from datetime import datetime
import time

import pandas as pd
import streamlit as st

from service import Service


class ManterAtendimentoUI:

  @staticmethod
  def _horarios_com_clientes(id_horario_atual=None):
    usuario_profissional = (
        st.session_state.get("usuario_tipo") == "profissional"
    )
    id_profissional = st.session_state.get("usuario_id")
    horarios_utilizados = {
        atendimento.get_id_horario()
        for atendimento in Service.atendimento_listar()
        if atendimento.get_id_horario() is not None
        and atendimento.get_id_horario() != id_horario_atual
    }
    return [
        horario
        for horario in Service.horario_listar()
        if horario.get_id_cliente() not in [None, 0]
        and (
            horario.get_id() not in horarios_utilizados
            or horario.get_id() == id_horario_atual
        )
        and (
            not usuario_profissional
            or horario.get_id_profissional() == id_profissional
        )
    ]

  @staticmethod
  def _atendimentos_visiveis():
    if st.session_state.get("usuario_tipo") == "profissional":
      return Service.atendimento_listar_profissional(
          st.session_state["usuario_id"]
      )
    return Service.atendimento_listar()

  @staticmethod
  def _atendimentos_nao_pagos():
    return [
        atendimento
        for atendimento in ManterAtendimentoUI._atendimentos_visiveis()
        if Service.atendimento_pagamento(atendimento.get_id()) is None
    ]

  @staticmethod
  def _servicos_snapshot(servicos):
    return [
        {
            "id": servico.get_id(),
            "descricao": servico.get_descricao(),
            "valor": servico.get_valor(),
        }
        for servico in servicos
    ]

  @staticmethod
  def _horario_label(horario):
    cliente = Service.cliente_listar_id(horario.get_id_cliente())
    nome_cliente = cliente.get_nome() if cliente is not None else "Cliente"
    data = horario.get_data().strftime("%d/%m/%Y %H:%M")
    return f"{data} - {nome_cliente}"

  @staticmethod
  def main():
    st.header("Atendimentos")
    tab1, tab2, tab3, tab4 = st.tabs(
        ["Listar", "Registrar", "Atualizar", "Excluir"]
    )
    with tab1:
      ManterAtendimentoUI.listar()
    with tab2:
      ManterAtendimentoUI.inserir()
    with tab3:
      ManterAtendimentoUI.atualizar()
    with tab4:
      ManterAtendimentoUI.excluir()

  @staticmethod
  def listar():
    atendimentos = ManterAtendimentoUI._atendimentos_visiveis()
    if not atendimentos:
      st.write("Nenhum atendimento cadastrado")
      return

    registros = []
    for atendimento in atendimentos:
      horario = (
          Service.horario_listar_id(atendimento.get_id_horario())
          if atendimento.get_id_horario() is not None
          else None
      )
      id_cliente = atendimento.get_id_cliente()
      if id_cliente is None and horario is not None:
        id_cliente = horario.get_id_cliente()
      cliente = (
          Service.cliente_listar_id(id_cliente)
          if id_cliente is not None
          else None
      )
      servicos = ", ".join(
          servico["descricao"] for servico in atendimento.get_servicos()
      )
      registros.append({
          "id": atendimento.get_id(),
          "cliente": cliente.get_nome() if cliente is not None else "—",
          "data": atendimento.get_data(),
          "queixa principal": atendimento.get_queixa_principal(),
          "histórico de saúde": atendimento.get_historico_saude(),
          "avaliação clínica": atendimento.get_avaliacao(),
          "prescrição (exames e medicamentos)": atendimento.get_prescricao(),
          "serviços realizados": servicos,
          "total (R$)": atendimento.get_valor_total(),
          "pagamento": (
              "Finalizado"
              if Service.atendimento_pagamento(atendimento.get_id())
              is not None
              else "Pendente"
          ),
      })
    st.dataframe(pd.DataFrame(registros), use_container_width=True)

  @staticmethod
  def inserir():
    horarios = ManterAtendimentoUI._horarios_com_clientes()
    servicos_disponiveis = Service.servico_listar()
    if not horarios:
      st.info("Não há horários com clientes para registrar atendimento.")
      return
    if not servicos_disponiveis:
      st.info("Cadastre serviços antes de registrar um atendimento.")
      return

    data = st.text_input(
        "Data e horário do atendimento (dd/mm/aaaa HH:MM)",
        datetime.now().strftime("%d/%m/%Y %H:%M"),
    )
    horario = st.selectbox(
        "Cliente e horário agendado",
        horarios,
        index=None,
        format_func=ManterAtendimentoUI._horario_label,
        key="atendimento_horario_novo",
    )
    queixa = st.text_area("Queixa principal")
    historico = st.text_area("Histórico de saúde")
    avaliacao = st.text_area("Avaliação clínica")
    prescricao = st.text_area("Prescrição de exames e medicamentos")
    servicos_agendados = []
    if horario is not None:
      servicos_agendados = [
          servico
          for servico in servicos_disponiveis
          if servico.get_id() == horario.get_id_servico()
      ]
    servicos = st.multiselect(
        "Serviços e procedimentos realizados",
        servicos_disponiveis,
        default=servicos_agendados,
        format_func=lambda servico: (
            f"{servico.get_descricao()} - R$ {servico.get_valor():.2f}"
        ),
        key="atendimento_servicos_novo",
    )

    if st.button("Registrar atendimento"):
      try:
        data_atendimento = datetime.strptime(data, "%d/%m/%Y %H:%M")
      except ValueError:
        st.error("Informe a data no formato dd/mm/aaaa HH:MM.")
        return
      if horario is None:
        st.error("Selecione o cliente e horário do atendimento.")
        return
      if not queixa.strip():
        st.error("Informe a queixa principal.")
        return
      if not servicos:
        st.error("Selecione ao menos um serviço ou procedimento realizado.")
        return

      Service.atendimento_inserir(
          data_atendimento,
          queixa.strip(),
          historico.strip(),
          avaliacao.strip(),
          prescricao.strip(),
          horario.get_id(),
          ManterAtendimentoUI._servicos_snapshot(servicos),
          horario.get_id_cliente(),
          horario.get_id_profissional(),
      )
      st.success(
          f"Atendimento registrado. Total dos serviços: "
          f"R$ {sum(servico.get_valor() for servico in servicos):.2f}"
      )
      time.sleep(1)
      st.rerun()

  @staticmethod
  def atualizar():
    atendimentos = ManterAtendimentoUI._atendimentos_nao_pagos()
    if not atendimentos:
      st.write("Nenhum atendimento pendente de pagamento para atualizar")
      return

    atendimento = st.selectbox("Atendimento", atendimentos)
    horarios = ManterAtendimentoUI._horarios_com_clientes(
        atendimento.get_id_horario()
    )
    servicos_disponiveis = Service.servico_listar()
    data = st.text_input(
        "Data e horário (dd/mm/aaaa HH:MM)",
        atendimento.get_data().strftime("%d/%m/%Y %H:%M"),
    )
    queixa = st.text_area(
        "Queixa principal", atendimento.get_queixa_principal()
    )
    historico = st.text_area(
        "Histórico de saúde", atendimento.get_historico_saude()
    )
    avaliacao = st.text_area(
        "Avaliação clínica", atendimento.get_avaliacao()
    )
    prescricao = st.text_area(
        "Prescrição de exames e medicamentos",
        atendimento.get_prescricao(),
    )
    id_horario = atendimento.get_id_horario()
    horario_index = next(
        (i for i, item in enumerate(horarios) if item.get_id() == id_horario),
        None,
    )
    horario = st.selectbox(
        "Cliente e horário agendado",
        horarios,
        index=horario_index,
        format_func=ManterAtendimentoUI._horario_label,
        key=f"atendimento_horario_{atendimento.get_id()}",
    )
    ids_servicos = {
        servico["id"] for servico in atendimento.get_servicos()
    }
    servicos_iniciais = [
        servico
        for servico in servicos_disponiveis
        if servico.get_id() in ids_servicos
    ]
    servicos = st.multiselect(
        "Serviços e procedimentos realizados",
        servicos_disponiveis,
        default=servicos_iniciais,
        format_func=lambda servico: (
            f"{servico.get_descricao()} - R$ {servico.get_valor():.2f}"
        ),
        key=f"atendimento_servicos_{atendimento.get_id()}",
    )

    if st.button("Atualizar atendimento"):
      try:
        data_atendimento = datetime.strptime(data, "%d/%m/%Y %H:%M")
      except ValueError:
        st.error("Informe a data no formato dd/mm/aaaa HH:MM.")
        return
      if horario is None:
        st.error("Selecione o cliente e horário do atendimento.")
        return
      if not queixa.strip():
        st.error("Informe a queixa principal.")
        return
      if not servicos:
        st.error("Selecione ao menos um serviço ou procedimento realizado.")
        return

      Service.atendimento_atualizar(
          atendimento.get_id(),
          data_atendimento,
          queixa.strip(),
          historico.strip(),
          avaliacao.strip(),
          prescricao.strip(),
          horario.get_id(),
          ManterAtendimentoUI._servicos_snapshot(servicos),
          horario.get_id_cliente(),
          horario.get_id_profissional(),
      )
      st.success("Atendimento atualizado com sucesso")
      time.sleep(1)
      st.rerun()

  @staticmethod
  def excluir():
    atendimentos = ManterAtendimentoUI._atendimentos_nao_pagos()
    if not atendimentos:
      st.write("Nenhum atendimento pendente de pagamento para excluir")
      return
    atendimento = st.selectbox("Atendimento", atendimentos)
    if st.button("Excluir atendimento"):
      Service.atendimento_excluir(atendimento.get_id())
      st.success("Atendimento excluído com sucesso")
      time.sleep(1)
      st.rerun()