# Definindo entidade
class Cliente: 
    def __init__(self, id, data, inicio, final, intervalo): 
        self.set_id(id)
        self.set_data(data)
        self.set_inicio(inicio)
        self.set_final(final)
        self.set_intervalo(intervalo)

    def set_id(self, id): 
        if id < 0: raise ValueError('Id deve ser positivo!')
        self.__id = id

    def set_data(self, data): 
        if len(nome) == 0: raise ValueError('Nome deve ser informado!')
        self.__nome = nome

    def set_inicio(self, inicio): 
        if len(email) == 0 and not '@' in email: raise ValueError('E-mail deve ser informado com @!')
        self.__email = email

    def set_final(self, final): 
        if len(fone) == 0: raise ValueError('TELEFONE DEVE SER INFORMADO!')
        self.__fone = fone

    def set_intervalo(self, intervalo):
        if len(senha) == 0: raise ValueError
        self.__senha = senha 
    
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_senha(self): return self.__senha

    def to_json(self): return {'id' : self.__id, 'nome' : self.__nome, 'email' : self.__email, 'fone' : self.__fone, 'senha' : self.__senha}

    @staticmethod
    def from_json(dic): return Cliente(dic['id'], dic['nome'], dic['email'], dic['fone'], dic['senha'])

    def __str__(self): 
        return f'ID: {self.__id} | NOME: {self.__nome} | EMAIL: {self.__email} | TELEFONE: {self.__fone} | SENHA: {self.__senha}'
    