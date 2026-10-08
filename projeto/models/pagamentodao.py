import json

from models.pagamento import Pagamento


class PagamentoDAO:

  def __init__(self):
    self.arquivo = "pagamentos.json"
    self.objetos = []

  def abrir(self):
    try:
      with open(self.arquivo, "r", encoding="utf-8") as arquivo:
        self.objetos = [
            Pagamento.from_json(dic) for dic in json.load(arquivo)
        ]
    except FileNotFoundError:
      self.objetos = []

  def salvar(self):
    with open(self.arquivo, "w", encoding="utf-8") as arquivo:
      json.dump(
          [obj.to_json() for obj in self.objetos],
          arquivo,
          ensure_ascii=False,
          indent=2,
      )

  def inserir(self, obj):
    self.abrir()
    if any(
        pagamento.get_id_atendimento() == obj.get_id_atendimento()
        for pagamento in self.objetos
    ):
      raise ValueError("Este atendimento já possui um pagamento registrado.")
    obj.id = max(
        (pagamento.get_id() for pagamento in self.objetos), default=0
    ) + 1
    self.objetos.append(obj)
    self.salvar()

  def listar(self):
    self.abrir()
    return self.objetos

  def listar_id_atendimento(self, id_atendimento):
    self.abrir()
    for obj in self.objetos:
      if obj.get_id_atendimento() == id_atendimento:
        return obj
    return None
