from datetime import datetime

class Atendimento:
    def __init__(self, id, id_atendimento, id_servico, qtd, valor):
        self.set_id(id)
        self.set_id_atendimento(id_atendimento)
        self.set_id_servico(id_servico)
        self.__qtd = 0
        self.__valor = 0
    
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_id_atendimento(self, id_atendimento): 
        if id_atendimento < 0: raise ValueError("Id deve ser positivo")
        self.__id_atendimento = id_atendimento
    def set_id_servico(self, id_servico): 
        if id_servico < 0: raise ValueError("Id deve ser positivo")
        self.__id_servico = id_servico
    def get_id(self) : return self.__id
    def get_data(self) : return self.__data
    def get_queixa_principal(self) : return self.__queixa_principal
    def get_historico_saude(self) : return self.__historico_saude
    def get_avaliacao(self) : return self.__avaliacao
    def get_prescricao(self) : return self.__prescricao
    def get_id_horario(self) : return self.__id_horario # Aqui vai ocorrer o relacionamento
    def get_total(self): return self.__total
    def get_pago(self): return self.__pago
    
    def __str__(self):
        return f"{self.__id} - {self.__data.strftime("%d/%m/%Y %H:%M")} - {self.__queixa_principal} - {self.__historico_saude} - {self.__historico_saude} - {self.__avaliacao} - {self.__prescricao}"
    
    def to_json(self):
        return { "id":self.__id, "data":self.__data.strftime("%d/%m/%Y %H:%M"), "queixa_principal":self.__queixa_principal, "historico_saude":self.__historico_saude, "historico_saude":self.__historico_saude, "avaliacao":self.__avaliacao, "prescricao":self.__prescricao, "id_horario":self.__id_horario }
    
    @staticmethod
    def from_json(dic):
        atendimento = Atendimento(dic["id"], datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"), dic["queixa_principal"], dic["historico_saude"], dic["avaliacao"], dic["prescricao"])
        atendimento.set_id_horario(dic["id_horario"])
        return atendimento