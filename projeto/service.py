from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.horario import Horario
from models.horariodao import HorarioDAO
from models.profissional import Profissional
from models.profissionaldao import ProfissionalDAO
from models.atendimento import Atendimento
from models.atendimentodao import AtendimentoDAO
from models.pagamento import Pagamento
from models.pagamentodao import PagamentoDAO
from datetime import datetime, timedelta

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        obj = Cliente(0, nome, email, fone, senha)
        ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_listar():
        r = ClienteDAO().listar()
        r.sort(key = lambda obj : obj.get_nome().casefold())
        return r
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        obj = Cliente(id, nome, email, fone, senha)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)
    @staticmethod
    def cliente_criar_admin():
        for c in Service.cliente_listar():
            if c.get_email() == "admin": return
        Service.cliente_inserir("admin", "admin", "fone", "1234")
    @staticmethod
    def cliente_autenticar(email, senha):
        for c in Service.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None        


    @staticmethod
    def servico_inserir(descricao, valor):
        obj = Servico(0, descricao, valor)
        ServicoDAO().inserir(obj)
    @staticmethod
    def servico_listar():
        r = ServicoDAO().listar()
        r.sort(key = lambda obj : obj.get_descricao().casefold())
        return r
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
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO().inserir(c)
    @staticmethod
    def horario_listar():
        r = HorarioDAO().listar()
        r.sort(key = lambda obj : obj.get_data())
        return r
    @staticmethod
    def horario_listar_id(id):
        return HorarioDAO().listar_id(id)
    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO().atualizar(c)
    @staticmethod
    def horario_excluir(id):
        HorarioDAO().excluir(id)
    @staticmethod
    def horario_listar_disponiveis(id_profissional):
        r = []
        agora = datetime.now()
        for h in Service.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False \
            and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort (key = lambda h : h.get_data())
        return r
    @staticmethod
    def horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo, id_profissional):
        data_inicio = datetime.strptime(data + " " + hora_inicio, "%d/%m/%Y %H:%M")
        data_fim = datetime.strptime(data + " " + hora_fim, "%d/%m/%Y %H:%M")
        delta = timedelta(minutes = intervalo)
        x = data_inicio
        while x <= data_fim:
            # insira um horário
            Service.horario_inserir(x, False, None, None, id_profissional)
            # vá para o próximo horário
            x = x + delta

    @staticmethod
    def profissional_inserir(nome, email, especialidade, senha):
        obj = Profissional(0, nome, email, especialidade, senha)
        ProfissionalDAO().inserir(obj)
    @staticmethod
    def profissional_listar():
        r = ProfissionalDAO().listar()
        r.sort(key = lambda obj : obj.get_nome().casefold())
        return r
    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)
    @staticmethod
    def profissional_atualizar(id, nome, email, especialidade, senha):
        obj = Profissional(id, nome, email, especialidade, senha)
        ProfissionalDAO().atualizar(obj)
    @staticmethod
    def profissional_excluir(id):
        ProfissionalDAO().excluir(id)
    @staticmethod
    def profissional_autenticar(email, senha):
        for c in Service.profissional_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None       
    @staticmethod
    def horario_confirmar_servico(id_profissional):
        r = []
        for h in Service.horario_listar():
            if h.get_confirmado() == False \
            and h.get_id_cliente() != None and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort (key = lambda h : h.get_data())
        return r

    @staticmethod
    def atendimento_inserir(
        data,
        queixa_principal,
        historico_saude,
        avaliacao,
        prescricao,
        id_horario,
        servicos=None,
        id_cliente=None,
        id_profissional=None,
    ):
        obj = Atendimento(
            0,
            data,
            queixa_principal,
            historico_saude,
            avaliacao,
            prescricao,
            id_horario,
            servicos,
            id_cliente,
            id_profissional,
        )
        AtendimentoDAO().inserir(obj)

    @staticmethod
    def atendimento_listar():
        atendimentos = AtendimentoDAO().listar()
        atendimentos.sort(key=lambda obj: obj.get_data())
        return atendimentos

    @staticmethod
    def atendimento_listar_id(id):
        return AtendimentoDAO().listar_id(id)

    @staticmethod
    def atendimento_listar_profissional(id_profissional):
        atendimentos = []
        for obj in Service.atendimento_listar():
            profissional_id = obj.get_id_profissional()
            if profissional_id is None and obj.get_id_horario() is not None:
                horario = Service.horario_listar_id(obj.get_id_horario())
                if horario is not None:
                    profissional_id = horario.get_id_profissional()
            if profissional_id == id_profissional:
                atendimentos.append(obj)
        return atendimentos

    @staticmethod
    def atendimento_listar_cliente(id_cliente):
        atendimentos = []
        for obj in Service.atendimento_listar():
            cliente_id = obj.get_id_cliente()
            if cliente_id is None and obj.get_id_horario() is not None:
                horario = Service.horario_listar_id(obj.get_id_horario())
                if horario is not None:
                    cliente_id = horario.get_id_cliente()
            if cliente_id == id_cliente:
                atendimentos.append(obj)
        return atendimentos

    @staticmethod
    def atendimento_pagamento(id_atendimento):
        return PagamentoDAO().listar_id_atendimento(id_atendimento)

    @staticmethod
    def atendimento_registrar_pagamento(id_atendimento, id_cliente, forma):
        atendimento = next(
            (
                obj for obj in Service.atendimento_listar_cliente(id_cliente)
                if obj.get_id() == id_atendimento
            ),
            None,
        )
        if atendimento is None:
            raise ValueError("Atendimento não encontrado para este cliente.")
        if Service.atendimento_pagamento(id_atendimento) is not None:
            raise ValueError("Este atendimento já foi pago.")
        valor = atendimento.get_valor_total()
        if valor <= 0:
            raise ValueError("O atendimento não possui valor para pagamento.")
        formas_validas = {"Pix", "Cartão", "Dinheiro"}
        if forma not in formas_validas:
            raise ValueError("Selecione uma forma de pagamento válida.")

        pagamento = Pagamento(
            0, id_atendimento, id_cliente, valor, datetime.now(), forma
        )
        PagamentoDAO().inserir(pagamento)
        return pagamento

    @staticmethod
    def atendimento_atualizar(
        id,
        data,
        queixa_principal,
        historico_saude,
        avaliacao,
        prescricao,
        id_horario,
        servicos=None,
        id_cliente=None,
        id_profissional=None,
    ):
        if Service.atendimento_pagamento(id) is not None:
            raise ValueError("Atendimentos pagos não podem ser alterados.")
        obj = Atendimento(
            id,
            data,
            queixa_principal,
            historico_saude,
            avaliacao,
            prescricao,
            id_horario,
            servicos,
            id_cliente,
            id_profissional,
        )
        AtendimentoDAO().atualizar(obj)

    @staticmethod
    def atendimento_excluir(id):
        if Service.atendimento_pagamento(id) is not None:
            raise ValueError("Atendimentos pagos não podem ser excluídos.")
        AtendimentoDAO().excluir(id)