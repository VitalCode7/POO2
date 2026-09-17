import json
from models.atendimento import Atendimento


class AtendimentoDAO:

  def __init__(self):
    self.objetos = []

  def abrir(self):
    try:
      with open("atendimentos.json", "r", encoding="utf-8") as f:
        dic = json.load(f)
        self.objetos = [Atendimento.from_json(obj) for obj in dic]
    except (FileNotFoundError, json.JSONDecodeError):
      self.objetos = []

  def salvar(self):
    with open("atendimentos.json", "w", encoding="utf-8") as f:
      json.dump(
          [obj.to_json() for obj in self.objetos],
          f,
          ensure_ascii=False,
          indent=4,
      )

  def inserir(self, obj):
    self.abrir()
    id = 1
    if len(self.objetos) > 0:
      id = max(x.get_id() for x in self.objetos) + 1
    obj.set_id(id)
    self.objetos.append(obj)
    self.salvar()

  def listar(self):
    self.abrir()
    return self.objetos

  def listar_id(self, id):
    self.abrir()
    for obj in self.objetos:
      if obj.get_id() == id:
        return obj
    return None

  def atualizar(self, obj):
    self.abrir()
    for i, x in enumerate(self.objetos):
      if x.get_id() == obj.get_id():
        self.objetos[i] = obj
        self.salvar()
        break

  def excluir(self, obj):
    self.abrir()
    for x in self.objetos:
      if x.get_id() == obj.get_id():
        self.objetos.remove(x)
        self.salvar()
        break