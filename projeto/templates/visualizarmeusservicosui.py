import time

import streamlit as st

from service import Service


class VisualizarMeusServicosUI:

  @staticmethod
  def main():
    st.header("Meus Atendimentos")
    st.caption(
        "O sistema registra a quitação localmente; não há integração com "
        "banco ou provedor externo de pagamentos."
    )
    atendimentos = Service.atendimento_listar_cliente(
        st.session_state["usuario_id"]
    )
    if not atendimentos:
      st.info("Você ainda não possui atendimentos registrados.")
      return

    for atendimento in atendimentos:
      pagamento = Service.atendimento_pagamento(atendimento.get_id())
      data = atendimento.get_data().strftime("%d/%m/%Y %H:%M")
      estado = "Finalizado" if pagamento is not None else "Pendente"
      with st.expander(f"Atendimento de {data} — {estado}"):
        st.write(f"**Queixa principal:** {atendimento.get_queixa_principal()}")
        st.write(
            f"**Histórico de saúde:** {atendimento.get_historico_saude()}"
        )
        st.write(f"**Avaliação clínica:** {atendimento.get_avaliacao()}")
        st.write(
            "**Prescrição de exames e medicamentos:** "
            f"{atendimento.get_prescricao()}"
        )

        servicos = atendimento.get_servicos()
        if servicos:
          st.write("**Serviços e procedimentos realizados:**")
          for servico in servicos:
            st.write(
                f"- {servico['descricao']}: R$ {servico['valor']:.2f}"
            )

        total = atendimento.get_valor_total()
        st.metric("Total", f"R$ {total:.2f}")
        if pagamento is not None:
          data_pagamento = pagamento.get_data().strftime("%d/%m/%Y %H:%M")
          st.success(
              f"Pagamento registrado em {data_pagamento} por "
              f"{pagamento.get_forma()}. Atendimento finalizado."
          )
        elif total <= 0:
          st.warning(
              "Este atendimento não possui serviços com valor registrado "
              "e não pode ser pago."
          )
        else:
          forma = st.selectbox(
              "Forma de pagamento",
              ["Pix", "Cartão", "Dinheiro"],
              key=f"forma_pagamento_{atendimento.get_id()}",
          )
          if st.button(
              "Pagar e finalizar atendimento",
              key=f"pagar_atendimento_{atendimento.get_id()}",
          ):
            try:
              Service.atendimento_registrar_pagamento(
                  atendimento.get_id(),
                  st.session_state["usuario_id"],
                  forma,
              )
            except ValueError as erro:
              st.error(str(erro))
              return
            st.success(
                f"Pagamento de R$ {total:.2f} registrado. "
                "Atendimento finalizado."
            )
            time.sleep(1)
            st.rerun()