from projeto.models.q2_cliente import Cliente         # entidade
from models.clientedao import ClienteDAO   # persistência
from projeto.models.servico import Servico
from models.servicodao import ServicoDAO
from teste.profissional import Profissional
from teste.profissionaldao import ProfissionalDAO
from models.q1_convenio import Convenio
from models.q3_conveniodao import ConvenioDAO

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone):
        obj = Cliente(0, nome, email, fone)
        ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)
    
    @staticmethod
    def servico_inserir(descricao, valor):
        obj = Servico(0, descricao, valor)
        ServicoDAO().inserir(obj)
    @staticmethod
    def servico_listar():
        return ServicoDAO().listar()
    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)
    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)
    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)

    @staticmethod
    def profissional_inserir(id, nome, email, especialidade):
        obj = Profissional(id, nome, email, especialidade)
        ProfissionalDAO().inserir(obj)
    @staticmethod
    def profissional_listar():
        return ProfissionalDAO().listar()
    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)
    @staticmethod
    def profissional_atualizar(id, nome, email, esp):
        obj = Profissional(id, nome, email, esp)
        ProfissionalDAO().atualizar(obj)
    @staticmethod
    def profissional_excluir(id):
        ProfissionalDAO().excluir(id)

    @staticmethod
    def convenio_inserir(nome, email, fone):
        obj = Convenio(0, nome, email, fone)
        ConvenioDAO().inserir(obj)
    @staticmethod
    def convenio_listar():
        return ConvenioDAO().listar()
    @staticmethod
    def convenio_listar_id(id):
        return ConvenioDAO().listar_id(id)
    @staticmethod
    def convenio_atualizar(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ConvenioDAO().atualizar(obj)
    @staticmethod
    def convenio_excluir(id):
        ConvenioDAO().excluir(id)