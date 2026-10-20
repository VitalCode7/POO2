class AtendimentoItens:
    def __init__(self, id, qtd, valor):
        self.set_id(id)
        self.set_qtd(qtd)
        self.set_valor(valor)
        self.set_id_atendimento(0)
        self.set_id_servico(0)

    def get_id(self): return self.__id
    def get_id_atendimento(self): return self.__id_atendimento
    def get_id_servico(self): return self.__id_servico
    def get_qtd(self): return self.__qtd
    def get_valor(self): return self.__valor

    def set_id(self, id): self.__id = id
    def set_id_atendimento(self, id_atendimento): self.__id_atendimento = id_atendimento
    def set_id_servico(self, id_servico): self.__id_servico = id_servico
    def set_qtd(self, qtd): self.__qtd = qtd
    def set_valor(self, valor): self.__valor = valor

    def to_json(self):
        return {"id": self.__id, "id_atendimento": self.__id_atendimento, "id_servico": self.__id_servico, "qtd": self.__qtd, "valor": self.__valor}

    @staticmethod
    def from_json(dic):
        item = AtendimentoItens(dic["id"], dic["qtd"], dic["valor"])
        item.set_id_atendimento(dic["id_atendimento"])
        item.set_id_servico(dic["id_servico"])
        return item