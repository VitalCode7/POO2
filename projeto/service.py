from models.cliente import Cliente
from dao_sql.clientedao import ClienteDAO
from models.servico import Servico
from dao_sql.servicodao import ServicoDAO
from models.horario import Horario
from dao_sql.horariodao import HorarioDAO
from models.atendimento import Atendimento
from dao_sql.atendimentodao import AtendimentoDAO
from models.profissional import Profissional
from dao_sql.profissionaldao import ProfissionalDAO
from models.atendimentoitens import AtendimentoItens
from dao_sql.atendimentoitensdao import AtendimentoItensDAO
from datetime import datetime, timedelta

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        clientes = ClienteDAO().listar()
        for c in clientes: 
            if c.get_email().strip() == email.strip(): raise ValueError('Email igual a existente')
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
    def cliente_atualizar(id, nome, email, fone, senha, foto):
        clientes = ClienteDAO().listar()
        for c in clientes: 
            if c.get_email().strip() == email.strip() or email.strip() == 'admin': raise ValueError('Email igual a existente')
        obj = Cliente(id, nome, email, fone, senha)
        obj.set_foto(foto)
        ClienteDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        atendimentos = AtendimentoDAO().listar()
        for a in atendimentos: 
            id_horario = a.get_id_horario()
            horario = HorarioDAO().listar_id(id_horario)
            if horario.get_id_cliente() == id and horario.get_confirmado(): raise ValueError
            ClienteDAO().excluir(id)

    @staticmethod
    def cliente_criar_admin():
        for c in Service.cliente_listar():
            if c.get_email() == "admin": return
        Service.cliente_inserir("admin", "admin", "fone", "1234") # Aqui se cria o adm
    @staticmethod
    def cliente_autenticar(email, senha):
        for c in Service.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()} # retorna id e nome
        return None
    @staticmethod
    def get_id_admin(): 
        for i in Service.cliente_listar(): 
            if i.get_email() == 'admin': 
                return i.get_id()

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
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        #Não pode ser o mesmo profissional
        horarios = HorarioDAO().listar()
        for h in horarios: 
            profissional = h.get_id_profissional()
            if h.get_data() == data and profissional == id_profissional: raise ValueError
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
        horarios = HorarioDAO().listar()
        for h in horarios: 
            profissional = h.get_id_profissional()
            if h.get_data() == data and profissional == id_profissional: raise ValueError
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO().atualizar(c)
    @staticmethod
    def horario_excluir(id):
        horario = HorarioDAO().listar_id(id)
        atendimentos = AtendimentoDAO().listar()
        for a in atendimentos: 
            cliente = a.get_id_cliente()
            if a.get_id_horario() == horario and cliente != None: raise ValueError
        HorarioDAO().excluir(id)
    @staticmethod
    def horario_listar_disponiveis(id_profissional): 
        r = []
        agora = datetime.now()
        for h in Service.horario_listar(): 
            if h.get_data() >= agora and h.get_id_profissional() == id_profissional and not h.get_confirmado(): 
                r.append(h)
        r.sort(key = lambda h : h.get_data())
        return r
    @staticmethod
    def horario_listar_confirmacao(id_profissional): 
        r = []
        agora = datetime.now()
        for h in Service.horario_listar(): 
            if h.get_data() >= agora and h.get_id_profissional() == id_profissional and h.get_id_cliente() != None and h.get_confirmado() != True: 
                r.append(h)
        r.sort(key = lambda h : h.get_data())
        return r
    @staticmethod
    def cliente_visualizar_agenda(id_cliente):
        r = []
        for h in Service.horario_listar(): 
            if h.get_id_cliente() == id_cliente: 
                r.append(h)
        return r
    @staticmethod
    def horarios_atendimento(id_profissional): 
        r = []
        for h in Service.horario_listar(): 
            if h.get_id_profissional() == id_profissional and h.get_confirmado(): 
                r.append(h)
        r.sort(key = lambda h : h.get_data())
        return r
    
    @staticmethod
    def horario_abrir_minha_agenda(data, horario_inicio, horario_fim, intervalo, id_profissional): 
        data_inicio = datetime.strptime(data + " " + horario_inicio, "%d/%m/%Y %H:%M")
        data_fim = datetime.strptime(data + " " + horario_fim, "%d/%m/%Y %H:%M")
        delta = timedelta(minutes = intervalo) 
        x = data_inicio
        while x <= data_fim:
            Service.horario_inserir(x, False, None, None, id_profissional)
            x += delta
    @staticmethod
    def horarios_listar_confirmados_hoje(): 
        horarios = Service.horario_listar()
        horarios_hoje = []
        for h in horarios:
            data = h.get_data().strftime("%d/%m/%Y %M:%H")
            data = data[:10]
            data = datetime.strptime(data, "%d/%m/%Y")
            data_agora = datetime.now().strftime("%d/%m/%Y")
            data_agora = datetime.strptime(data_agora, "%d/%m/%Y")
            if h.get_confirmado() and data == data_agora: 
                horarios_hoje.append(h)
        if len(horarios_hoje) == 0: return None
        horarios_hoje.sort(key = lambda h : h.get_data())
        return horarios_hoje
    @staticmethod
    def agenda_profissionais(id_profissional): 
        horarios = Service.horario_listar()
        agendamentos = []
        for h in horarios: 
            if h.get_id_profissional() == id_profissional: agendamentos.append(h)
        if len(agendamentos) == 0: return None
        agendamentos.sort(key = lambda h : h.get_data())
        return agendamentos

    @staticmethod
    def atendimento_inserir(data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        obj = Atendimento(0, data, queixa_principal, historico_saude, avaliacao, prescricao)
        obj.set_id_horario(id_horario)
        AtendimentoDAO().inserir(obj)
    @staticmethod
    def atendimento_listar():
        return AtendimentoDAO().listar()
    @staticmethod
    def atendimento_listar_id(id):
        return AtendimentoDAO().listar_id(id)
    @staticmethod
    def atendimento_atualizar(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        obj = Atendimento(id, data, queixa_principal, historico_saude, avaliacao, prescricao)
        obj.set_id_horario(id_horario)
        AtendimentoDAO().atualizar(obj)
    @staticmethod
    def atendimento_excluir(id):
        AtendimentoDAO().excluir(id)

    @staticmethod
    def atendimento_itens_listar_por_atendimento(id_atendimento):
        atendimento_itens = []
        for i in Service.atendimento_itens_listar(): 
            if i.get_id_atendimento() == id_atendimento: 
                atendimento_itens.append(i)
        return atendimento_itens
    @staticmethod
    def atendimento_calcular_total(id_atendimento):
        itens = Service.atendimento_itens_listar_por_atendimento(id_atendimento)
        total = 0.0
        for item in itens:
            total += item.get_valor()
        return total

    @staticmethod
    def pagar_atendimento(a): 
        a.set_pago(True)
        AtendimentoDAO().atualizar(a)

    @staticmethod
    def atendimento_itens_inserir(id_atendimento, id_servico, qnt, valor):
        obj = AtendimentoItens(0, id_atendimento, id_servico, qnt, valor)
        total = Service.atendimento_calcular_total(id_atendimento)
        atendimento = Service.atendimento_listar_id(id_atendimento)
        atendimento.set_total(total)
        AtendimentoDAO().atualizar(atendimento)
        AtendimentoItensDAO().inserir(obj)
    @staticmethod
    def atendimento_itens_listar():
        return AtendimentoItensDAO().listar()
    @staticmethod
    def atendimento_itens_listar_id(id):
        return AtendimentoItensDAO().listar_id(id)
    @staticmethod
    def atendimento_itens_atualizar(id, id_atendimento, id_servico, qnt):
        obj = AtendimentoItens(id, id_atendimento, id_servico, qnt)
        AtendimentoItensDAO().atualizar(obj)
    @staticmethod
    def atendimento_itens_excluir(id):
        AtendimentoItensDAO().excluir(id)
     
    @staticmethod
    def profissional_inserir(nome, email, especialidade, senha):
        profissionais = ProfissionalDAO().listar()
        for p in profissionais: 
            if p.get_email().strip() == email.strip(): raise ValueError
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
    def profissional_atualizar(id, nome, email, especialidade, senha, imagem = ""):
        profissionais = ProfissionalDAO().listar()
        for p in profissionais: 
            if p.get_email().strip() == email.strip() or email.strip() == 'admin': raise ValueError
        obj = Profissional(id, nome, email, especialidade, senha)
        obj.set_imagem(imagem)
        ProfissionalDAO().atualizar(obj)

    @staticmethod
    def profissional_excluir(id):
        atendimentos = AtendimentoDAO().listar()
        for a in atendimentos: 
            id_horario = a.get_id_horario()
            horario = HorarioDAO().listar_id(id_horario)
            if horario.get_id_profissional() == id and horario.get_confirmado(): raise ValueError
            ProfissionalDAO().excluir(id)
    @staticmethod
    def profissional_autenticar(email, senha): # Aqui ocorre a autenticação
        for c in Service.profissional_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None

    @staticmethod
    def totalizar_atendimentos_profissionais(inicio, fim, id_profissional):
        data_inicio = inicio[:10]
        data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")

        data_fim = fim[:10]
        data_fim = datetime.strptime(data_fim, "%d/%m/%Y")

        atendimentos = Service.atendimento_listar()
        horarios = Service.horario_listar()
        atendimentos_profissional = []

        for a in atendimentos: 
            id_horario = a.get_id_horario()
            horario = Service.horario_listar_id(id_horario)
            if horario.get_id_profissional == id_profissional: 
                atendimentos_profissional.append(a)

        # filtro
        atendimentos_tempo = []
        for ap in atendimentos_profissional: 
            horario = ap.get_id_horario()
            horario_obj = Service.horario_listar_id(horario)
            # Transformando horário: 
            data = horario_obj.get_data().strftime("%d/%m/%Y %M:%H")
            data = data[:10]
            data = datetime.strptime(data, "%d/%m/%Y")
            if data_inicio <= data <= data_fim: 
                atendimentos_tempo.append(ap)
    
        return atendimentos_tempo