class Convenio:
    def __init__(self, id, nome, contato, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_contato(contato)
        self.set_fone(fone)
    
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome = nome
    def set_contato(self, contato):
        if contato == "": raise ValueError("Contato deve ser informado")
        self.__contato = contato
    def set_fone(self, fone):
        if fone == "": raise ValueError("Fone deve ser informado")
        self.__fone = fone

    def get_id(self) : return self.__id
    def get_nome(self) : return self.__nome
    def get_contato(self) : return self.__contato
    def get_fone(self) : return self.__fone

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__contato} - {self.__fone}"
    
    def to_json(self):
        return { "id":self.__id, "nome":self.__nome, "contato":self.__contato, "fone":self.__fone }
    
    @staticmethod
    def from_json(dic):
        return Convenio(dic["id"], dic["nome"], dic["contato"], dic["fone"])