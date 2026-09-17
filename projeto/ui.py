from datetime import datetime
from service import Service


class UI:

  @staticmethod
  def main():
    op = 0
    while op != 21:
      op = UI.menu()
      if op == 1:
        UI.cliente_inserir()
      elif op == 2:
        UI.cliente_listar()
      elif op == 3:
        UI.cliente_atualizar()
      elif op == 4:
        UI.cliente_excluir()
      elif op == 5:
        UI.servico_inserir()
      elif op == 6:
        UI.servico_listar()
      elif op == 7:
        UI.servico_atualizar()
      elif op == 8:
        UI.servico_excluir()
      elif op == 9:
        UI.horario_inserir()
      elif op == 10:
        UI.horario_listar()
      elif op == 11:
        UI.horario_atualizar()
      elif op == 12:
        UI.horario_excluir()
      elif op == 13:
        UI.profissional_inserir()
      elif op == 14:
        UI.profissional_listar()
      elif op == 15:
        UI.profissional_atualizar()
      elif op == 16:
        UI.profissional_excluir()
      elif op == 17:
        UI.atendimento_inserir()
      elif op == 18:
        UI.atendimento_listar()
      elif op == 19:
        UI.atendimento_atualizar()
      elif op == 20:
        UI.atendimento_excluir()

  @staticmethod
  def menu():
    print("\n----------- Cadastro de Clientes ----------")
    print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
    print("----------- Cadastro de Serviços ----------")
    print("5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir")
    print("----------- Cadastro de Horários ----------")
    print("9-Inserir, 10-Listar, 11-Atualizar, 12-Excluir")
    print("----------- Cadastro de Profissionais ----------")
    print("13-Inserir, 14-Listar, 15-Atualizar, 16-Excluir")
    print("----------- Cadastro de Atendimentos ----------")
    print("17-Inserir, 18-Listar, 19-Atualizar, 20-Excluir")
    print("----------- Outras opções -----------------")
    print("21-Fim")
    return int(input("Informe uma opção: "))

  @staticmethod
  def cliente_inserir():
    nome = input("Informe o nome: ")
    email = input("Informe o e-mail: ")
    fone = input("Informe o telefone: ")
    id_convenio = input("Informe o id convenio: ")
    Service.cliente_inserir(nome, email, fone, id_convenio)

  @staticmethod
  def cliente_listar():
    for obj in Service.cliente_listar():
      print(obj)

  @staticmethod
  def cliente_atualizar():
    UI.cliente_listar()
    id = int(input("Informe o id do cliente a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    email = input("Informe o novo e-mail: ")
    fone = input("Informe o novo telefone: ")
    id_convenio = int(input("Informe o novo id convenio: "))
    Service.cliente_atualizar(id, nome, email, fone, id_convenio)

  @staticmethod
  def cliente_excluir():
    UI.cliente_listar()
    id = int(input("Informe o id do cliente a ser excluído: "))
    Service.cliente_excluir(id)

  @staticmethod
  def servico_inserir():
    descricao = input("Informe a descrição: ")
    valor = float(input("Informe o valor: "))
    Service.servico_inserir(descricao, valor)

  @staticmethod
  def servico_listar():
    for obj in Service.servico_listar():
      print(obj)

  @staticmethod
  def servico_atualizar():
    UI.servico_listar()
    id = int(input("Informe o id do serviço a ser atualizado: "))
    descricao = input("Informe a nova descrição: ")
    valor = float(input("Informe o novo valor: "))
    Service.servico_atualizar(id, descricao, valor)

  @staticmethod
  def servico_excluir():
    UI.servico_listar()
    id = int(input("Informe o id do serviço a ser excluído: "))
    Service.servico_excluir(id)

  @staticmethod
  def horario_inserir():
    data_str = input("Informe a data e hora (dd/mm/aaaa HH:MM): ")
    data = datetime.strptime(data_str, "%d/%m/%Y %H:%M")

    confirmado_str = input("Confirmado? (s/n): ").strip().lower()
    confirmado = confirmado_str == "s"

    UI.cliente_listar()
    id_cliente_input = input(
        "Informe o ID do cliente (ou pressione Enter para nenhum): "
    )
    id_cliente = int(id_cliente_input) if id_cliente_input.strip() else 0

    UI.servico_listar()
    id_servico_input = input(
        "Informe o ID do serviço (ou pressione Enter para nenhum): "
    )
    id_servico = int(id_servico_input) if id_servico_input.strip() else 0

    UI.profissional_listar()
    id_prof_input = input(
        "Informe o ID do profissional (ou pressione Enter para nenhum): "
    )
    id_profissional = int(id_prof_input) if id_prof_input.strip() else 0

    Service.horario_inserir(
        data, confirmado, id_cliente, id_servico, id_profissional
    )

  @staticmethod
  def horario_listar():
    horarios = Service.horario_listar()
    if not horarios:
      print("Nenhum horário cadastrado.")
      return

    for h in horarios:
      cliente = Service.cliente_listar_id(h.get_id_cliente())
      servico = Service.servico_listar_id(h.get_id_servico())
      profissional = Service.profissional_listar_id(h.get_id_profissional())
      cliente_nome = cliente.get_nome() if cliente else "Nenhum"
      servico_descr = servico.get_descricao() if servico else "Nenhum"
      prof_nome = profissional.get_nome() if profissional else "Nenhum"

      print(
          f"{h.get_id()} - {h.get_data().strftime('%d/%m/%Y %H:%M')} | "
          f"Confirmado: {h.get_confirmado()} | Cliente: {cliente_nome} | "
          f"Serviço: {servico_descr} | Profissional: {prof_nome}"
      )

  @staticmethod
  def horario_atualizar():
    UI.horario_listar()
    id = int(input("Informe o ID do horário a ser atualizado: "))

    data_str = input("Informe a nova data e hora (dd/mm/aaaa HH:MM): ")
    data = datetime.strptime(data_str, "%d/%m/%Y %H:%M")

    confirmado_str = input("Confirmado? (s/n): ").strip().lower()
    confirmado = confirmado_str == "s"

    UI.cliente_listar()
    id_cliente_input = input(
        "Informe o novo ID do cliente (ou pressione Enter para nenhum): "
    )
    id_cliente = int(id_cliente_input) if id_cliente_input.strip() else 0

    UI.servico_listar()
    id_servico_input = input(
        "Informe o novo ID do serviço (ou pressione Enter para nenhum): "
    )
    id_servico = int(id_servico_input) if id_servico_input.strip() else 0

    UI.profissional_listar()
    id_prof_input = input(
        "Informe o novo ID do profissional (ou pressione Enter para nenhum): "
    )
    id_profissional = int(id_prof_input) if id_prof_input.strip() else 0

    Service.horario_atualizar(
        id, data, confirmado, id_cliente, id_servico, id_profissional
    )

  @staticmethod
  def horario_excluir():
    UI.horario_listar()
    id = int(input("Informe o ID do horário a ser excluído: "))
    Service.horario_excluir(id)

  @staticmethod
  def profissional_inserir():
    nome = input("Informe o nome: ")
    email = input("Informe o e-mail: ")
    especialidade = input("Informe a especialidade: ")
    Service.profissional_inserir(nome, email, especialidade)

  @staticmethod
  def profissional_listar():
    for obj in Service.profissional_listar():
      print(obj)

  @staticmethod
  def profissional_atualizar():
    UI.profissional_listar()
    id = int(input("Informe o id do profissional a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    email = input("Informe o novo e-mail: ")
    especialidade = input("Informe a nova especialidade: ")
    Service.profissional_atualizar(id, nome, email, especialidade)

  @staticmethod
  def profissional_excluir():
    UI.profissional_listar()
    id = int(input("Informe o id do profissional a ser excluído: "))
    Service.profissional_excluir(id)

  @staticmethod
  def atendimento_inserir():
    data_str = input(
        "Informe a data e hora do atendimento (dd/mm/aaaa HH:MM): "
    )
    data = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
    queixa = input("Informe a queixa principal: ")
    historico = input("Informe o histórico de saúde: ")
    avaliacao = input("Informe a avaliação: ")
    prescricao = input("Informe a prescrição: ")

    UI.horario_listar()
    id_h_input = input(
        "Informe o ID do horário (ou pressione Enter para nenhum): "
    )
    id_horario = int(id_h_input) if id_h_input.strip() else 0

    Service.atendimento_inserir(
        data, queixa, historico, avaliacao, prescricao, id_horario
    )

  @staticmethod
  def atendimento_listar():
    atendimentos = Service.atendimento_listar()
    if not atendimentos:
      print("Nenhum atendimento cadastrado.")
      return

    for a in atendimentos:
      horario = Service.horario_listar_id(a.get_id_horario())
      horario_str = (
          horario.get_data().strftime("%d/%m/%Y %H:%M") if horario else "Nenhum"
      )
      print(
          f"{a.get_id()} - {a.get_data().strftime('%d/%m/%Y %H:%M')} | "
          f"Queixa: {a.get_queixa_principal()} | Horário: {horario_str}"
      )

  @staticmethod
  def atendimento_atualizar():
    UI.atendimento_listar()
    id = int(input("Informe o ID do atendimento a ser atualizado: "))

    data_str = input("Informe a nova data e hora (dd/mm/aaaa HH:MM): ")
    data = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
    queixa = input("Informe a nova queixa principal: ")
    historico = input("Informe o novo histórico de saúde: ")
    avaliacao = input("Informe a nova avaliação: ")
    prescricao = input("Informe a nova prescrição: ")

    UI.horario_listar()
    id_h_input = input(
        "Informe o novo ID do horário (ou pressione Enter para nenhum): "
    )
    id_horario = int(id_h_input) if id_h_input.strip() else 0

    Service.atendimento_atualizar(
        id, data, queixa, historico, avaliacao, prescricao, id_horario
    )

  @staticmethod
  def atendimento_excluir():
    UI.atendimento_listar()
    id = int(input("Informe o ID do atendimento a ser excluído: "))
    Service.atendimento_excluir(id)

  @staticmethod
  def convenio_inserir():
    nome = input("Informe o nome: ")
    contato = input("Informe o contato: ")
    fone = input("Informe o telefone: ")
    Service.convenio_inserir(nome, contato, fone)

  @staticmethod
  def convenio_listar():
    for obj in Service.convenio_listar():
      print(obj)

  @staticmethod
  def convenio_atualizar():
    UI.convenio_listar()
    id = int(input("Informe o id do convênio a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    contato = input("Informe o novo contato: ")
    fone = input("Informe o novo telefone: ")
    Service.convenio_atualizar(id, nome, contato, fone)

  @staticmethod
  def convenio_excluir():
    UI.convenio_listar()
    id = int(input("Informe o id do convênio a ser excluído: "))
    Service.convenio_excluir(id)


if __name__ == "__main__":
  UI.main()