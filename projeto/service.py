from models.cliente import Cliente         # entidade
from models.clientedao import ClienteDAO   # persistência
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.horario import Horario
from models.horariodao import HorarioDAO
from models.profissional import Profissional
from models.profissionaldao import ProfissionalDAO
from models.atendimento import Atendimento
from models.atendimentodao import AtendimentoDAO
from models.atendimentoitens import AtendimentoItens
from models.atendimentoitensdao import AtendimentoItensDAO
from datetime import datetime, timedelta

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        profissionais = Service.profissional_listar()
        clientes = Service.cliente_listar()
        for p in profissionais:
            if email == p.get_email():
                raise ValueError('Email não deve ser igual')
        for c in clientes:
            if email == c.get_email():
                raise ValueError('Email não deve ser igual')
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
        profissionais = Service.profissional_listar()
        clientes = Service.cliente_listar()
        for p in profissionais:
            if email == p.get_email():
                raise ValueError('Email não deve ser igual')
        for c in clientes:
            if id != c.get_id() and email == c.get_email():
                raise ValueError('Email não deve ser igual')
        obj = Cliente(id, nome, email, fone, senha)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        horarios = Service.horario_listar()
        for c in horarios:
            if id == c.get_id_cliente():
                raise ValueError('Não pode excluir clientes com horário confirmado')
        ClienteDAO().excluir(id)
    @staticmethod
    def cliente_visualizar_servicos(id_cliente):
        h = []
        horarios = Service.horario_listar()
        for obj in horarios:
            if obj.get_id_cliente() == id_cliente: h.append(obj)
        h.sort(key = lambda obj : obj.get_data())
        return h
    
    @staticmethod
    def servico_inserir(descricao, valor):
        for obj in Service.servico_listar():
            if obj.get_descricao() == descricao:
                raise ValueError('Serviço já cadastrado')
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
        for obj in Service.servico_listar():
            if obj.get_id() != id and obj.get_descricao() == descricao:
                raise ValueError('Descrição já cadastrada em outro serviço')
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)
    @staticmethod
    def servico_excluir(id):
        for obj in Service.horario_listar():
            if obj.get_id_servico() == id:
                raise ValueError('Serviço já agendado: não é possível excluir')
        ServicoDAO().excluir(id)

    @staticmethod
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        horarios = Service.horario_listar()
        for h in horarios:
            if h.get_id_profissional() == id_profissional:
                if h.get_data() == data:
                    raise ValueError('Não pode haver mais de um horário cadastrado no mesmo momento')
        obj = Horario(0, data)
        obj.set_confirmado(confirmado)
        obj.set_id_cliente(id_cliente)
        obj.set_id_servico(id_servico)
        obj.set_id_profissional(id_profissional)
        HorarioDAO().inserir(obj)
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
        horarios = Service.horario_listar()
        for h in horarios:
            if h.get_id() != id:
                if h.get_id_profissional() == id_profissional:
                    if h.get_data() == data:
                        raise ValueError('Não pode haver mais de um horário cadastrado no mesmo momento para o mesmo profissional')
        obj = Horario(id, data)
        obj.set_confirmado(confirmado)
        obj.set_id_cliente(id_cliente)
        obj.set_id_servico(id_servico)
        obj.set_id_profissional(id_profissional)
        HorarioDAO().atualizar(obj)
    @staticmethod
    def horario_excluir(id):
        horarios = Service.horario_listar()
        for h in horarios:
            if h.get_id() == id:
                cliente = Service.cliente_listar_id(h.get_id_cliente())
                if cliente != None:
                    raise ValueError('Não pode excluir um horário já agendado por um cliente')
        HorarioDAO().excluir(id)

    @staticmethod
    def horario_listar_disponiveis(id_profissional):
        r = []
        agora = datetime.now()
        for h in Service.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional: r.append(h)
        r.sort(key = lambda h : h.get_data())
        return r

    @staticmethod
    def abrir_agenda(data, horario_inicial, horario_final, intervalo, id_profissional):
        h_inicio, m_inicio = map(int, horario_inicial.split(":"))
        h_final, m_final = map(int, horario_final.split(":"))
        inicial = timedelta(hours=h_inicio, minutes=m_inicio)
        final = timedelta(hours=h_final, minutes=m_final)
        inter = timedelta(minutes=int(intervalo))
        data = datetime.strptime(data, "%d/%m/%Y")
        while inicial <= final:
            data_datetime = data + inicial
            Service.horario_inserir(data_datetime, False, None, None, id_profissional)
            inicial += inter



    @staticmethod
    def profissional_inserir(nome, email, especialidade, senha):
        profissionais = Service.profissional_listar()
        clientes = Service.cliente_listar()
        for p in profissionais:
            if email == p.get_email():
                raise ValueError('Email não deve ser igual')
        for c in clientes:
            if email == c.get_email():
                raise ValueError('Email não deve ser igual')
        obj = Profissional(0, nome, email, especialidade, senha)
        ProfissionalDAO().inserir(obj)
    @staticmethod
    def profissional_listar():
        r = ProfissionalDAO().listar()
        r.sort(key = lambda obj : obj.get_especialidade() + obj.get_nome())
        return r
    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)
    @staticmethod
    def profissional_atualizar(id, nome, email, especialidade, senha):
        profissionais = Service.profissional_listar()
        clientes = Service.cliente_listar()
        for p in profissionais:
            if id != p.get_id() and email == p.get_email():
                raise ValueError('Email não deve ser igual')
        for c in clientes:
            if email == c.get_email():
                raise ValueError('Email não deve ser igual')
        obj = Profissional(id, nome, email, especialidade, senha)
        ProfissionalDAO().atualizar(obj)
    @staticmethod
    def profissional_excluir(id):
        horarios = Service.horario_listar()
        for c in horarios:
            if id == c.get_id_profissional():
                raise ValueError('Não pode excluir profissionais com horário confirmado')
        ProfissionalDAO().excluir(id)
    
    @staticmethod
    def profissional_visualizar_agenda(id_profissional):
        h = []
        horarios = Service.horario_listar()
        for obj in horarios:
            if obj.get_id_profissional() == id_profissional: h.append(obj)
        h.sort(key = lambda obj : obj.get_data())
        return h


    @staticmethod
    def atendimento_inserir(data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario, total, pago):
        obj = Atendimento(0, data, queixa_principal, historico_saude, avaliacao, prescricao)
        obj.set_id_horario(id_horario)
        obj.set_total(total)
        obj.set_pago(pago)
        AtendimentoDAO().inserir(obj)
    @staticmethod
    def atendimento_listar():
        r = AtendimentoDAO().listar()
        r.sort(key = lambda obj : obj.get_data())
        return r
    @staticmethod
    def atendimento_listar_id(id):
        return AtendimentoDAO().listar_id(id)
    @staticmethod
    def atendimento_atualizar(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario, total, pago):
        obj = Atendimento(id, data, queixa_principal, historico_saude, avaliacao, prescricao)
        obj.set_id_horario(id_horario)
        obj.set_total(total)
        obj.set_pago(pago)
        AtendimentoDAO().atualizar(obj)
    @staticmethod
    def atendimento_excluir(id):
        AtendimentoDAO().excluir(id)

    @staticmethod
    def atendimentoitem_inserir(id_atendimento, id_servico, qtd, valor):
        obj = AtendimentoItens(0, qtd, valor)
        obj.set_id_atendimento(id_atendimento)
        obj.set_id_servico(id_servico)
        AtendimentoItensDAO().inserir(obj)

    @staticmethod
    def atendimentoitem_listar():
        return AtendimentoItensDAO().listar()

    @staticmethod
    def atendimentoitem_listar_id(id):
        return AtendimentoItensDAO().listar_id(id)

    @staticmethod
    def atendimentoitem_atualizar(id, id_atendimento, id_servico, qtd, valor):
        obj = AtendimentoItens(id, qtd, valor)
        obj.set_id_atendimento(id_atendimento)
        obj.set_id_servico(id_servico)
        AtendimentoItensDAO().atualizar(obj)

    @staticmethod
    def atendimentoitem_excluir(id):
        AtendimentoItensDAO().excluir(id)

    @staticmethod
    def atendimentoitem_listar_atendimento(id_atendimento):
        h = []
        atendimentos = Service.atendimentoitem_listar()
        for obj in atendimentos:
            if obj.get_id_atendimento() == id_atendimento: h.append(obj)
        h.sort(key = lambda obj : obj.get_data())
        return h

    @staticmethod
    def total_atendimentos(dt_incial, dt_final):
        r = ProfissionalDAO().listar()
        r.sort(key = lambda obj : obj.get_nome().casefold())
        dic = {}
        for obj in r:
            dic[obj.get_id()] = 0
        horarios = HorarioDAO().listar()
        for h in horarios:
            if h.get_confirmado() and dt_incial <= h.get_data().date() <= dt_final: dic[h.get_id_profissional()] = dic[h.get_id_profissional()] + 1
        return dic

    @staticmethod
    def horarios_confirmados():
        h = []
        horarios = Service.horario_listar()
        for obj in horarios:
            if obj.get_confirmado() and obj.get_data().day == datetime.now().day: h.append(obj)
        h.sort(key = lambda obj : obj.get_data())
        return h
    
    @staticmethod
    def admin_visualizar_agenda(id_profissional):
        h = []
        horarios = Service.horario_listar()
        for obj in horarios:
            if obj.get_id_profissional() == id_profissional: h.append(obj)
        h.sort(key = lambda obj : obj.get_data())
        return h

    @staticmethod
    def cliente_criar_admin():
        for c in Service.cliente_listar():
            if c.get_email() == "admin": return
        Service.cliente_inserir("admin", "admin", "fone", "1234")

    @staticmethod
    def cliente_autenticar(email, senha):
        for c in Service.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha: return {"id": c.get_id(), "nome": c.get_nome()}
        return None
    
    @staticmethod
    def profissional_autenticar(email, senha):
        for p in Service.profissional_listar():
            if p.get_email() == email and p.get_senha() == senha: return {"id": p.get_id(), "nome": p.get_nome()}
        return None