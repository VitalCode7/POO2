from service import Service

class UI: 
    @staticmethod
    def main(): 
        op = 0
        while op != 17: 
            op = UI.menu()
            match op: 
                case 1: UI.cliente_inserir()
                case 2: UI.cliente_listar()
                case 3: UI.cliente_atualizar()
                case 4: UI.cliente_excluir()
                case 5: UI.cliente_pesquisar_nome()
                case 6: UI.servico_inserir()
                case 7: UI.servico_listar()
                case 8: UI.servico_atualizar()
                case 9: UI.servico_excluir()
                case 10: UI.servico_pesquisar_nome()
                case 11: UI.servico_listar_descricao()
                case 12: UI.profissionais_inserir()
                case 13: UI.profissionais_listar()
                case 14: UI.profissionais_atualizar()
                case 15: UI.profissionais_excluir()
                case 16: UI.profissionais_pesquisar_nome()
    @staticmethod
    def menu(): 
        print(' [1] INSERIR CLIENTE \n [2] LISTAR CLIENTE \n [3] ATUALIZAR CLIENTE  \n [4] EXCLUIR CLIENTE \n [5] PESQUISAR CLIENTE \n [6] INSERIR SERVIÇO \n [7] LISTAR SERVIÇOS \n [8] ATUALIZAR SERVIÇOS \n [9] EXCLUIR SERVIÇOS \n [10] PESQUISAR SERVIÇO \n [11] LISTAR DESCRIÇÕES \n [12] INSERIR PROFISSIONAIS \n [13] LISTAR PROFISSIONAIS \n [14] ATUALIZAR PROFISSIONAIS \n [15] EXCLUIR PROFISSIONAIS \n [16] PESQUISAR POR PROFISSIONAIS \n [17] SAIR')
        return int(input('Informe uma opção: '))
    
    # CLIENTES
    @staticmethod
    def cliente_inserir(): 
        nome = input('Informe o nome: \n')
        email = input('Informe o email: \n')
        fone = input('Informe o telefone: \n')
        senha = input('Informe a senha: \n')
        Service.cliente_inserir(nome, email, fone, senha)
    @staticmethod
    def cliente_listar(): 
        for obj in Service.cliente_listar(): print(obj)
    @staticmethod
    def cliente_atualizar(): 
        for obj in Service.cliente_listar(): print(obj)
        id = int(input('Informe o ID a ser atualizado: \n'))
        nome = input('Informe o novo nome: \n')
        email = input('Informe o novo email: \n')
        fone = input('Informe o novo telefone: \n')
        senha = input('Informe a sua senha: \n')
        Service.cliente_atualizar(id, nome, email, fone, senha)
    @staticmethod
    def cliente_excluir():
        for obj in Service.cliente_listar(): print(obj)
        id = int(input('Informe o id do cliente a ser excluido: \n'))
        Service.cliente_excluir(id)
    def cliente_pesquisar_nome(): 
        iniciais = input('Insira as inicias: ')
        lista_nomes = Service.cliente_listar_nomes(iniciais)
        for i in lista_nomes: print(i)
    
    # SERVIÇOS
    @staticmethod
    def servico_inserir(): 
        servico = input('Informe a descricao do servico: \n')
        valor = float(input('Informe o valor do serviço: \n'))
        Service.servico_inserir(servico, valor)
    @staticmethod
    def servico_listar(): 
        for obj in Service.servico_listar: print(obj)
    @staticmethod
    def servico_atualizar(): 
        for obj in Service.servico_listar(): print(obj)
        id = int(input('Informe o ID a ser atualizado: \n'))
        descricao = input('Informe a nova descrição: \n')
        valor = float(input('Informe o novo valor: \n'))
        Service.servico_atualizar(id, descricao, valor)
    @staticmethod
    def servico_excluir(): 
        for obj in Service.servico_listar(): print(obj)
        id = int(input('Informe o id do serviço a ser excluido: \n'))
        Service.servico_excluir(id)
    @staticmethod
    def servico_pesquisar_nome(): 
        iniciais = input('Insira as inicias: \n')
        lista_nomes = Service.servico_listar_nomes(iniciais)
        for i in lista_nomes: print(i)
    @staticmethod
    def servico_listar_descricao():
        iniciais = input('Informe a descrição: \n')
        print(Service.servico_listar_descricao(iniciais))

    # PROFISSIONAIS
    @staticmethod
    def profissionais_inserir(): 
        nome = input('Informe o nome: \n')
        email = input('Informe o email: \n')
        senha = input('Informe a senha: \n')
        especialidade = input('Informe a especialidade: \n')
        Service.profissionais_inserir(nome, email, senha, especialidade)
    @staticmethod
    def profissionais_listar(): 
        for obj in Service.profissionais_listar(): print(obj)
    @staticmethod
    def profissionais_atualizar(): 
        for obj in Service.cliente_listar(): print(obj)
        id = int(input('Informe o ID a ser atualizado: \n'))
        nome = input('Informe o novo nome: \n')
        email = input('Informe o novo email: \n')
        senha = input('Informe a sua senha: \n')
        especialidade = input('Informe uma nova especialidade: \n')
        Service.profissionais_atualizar(id, nome, email, senha, especialidade)
    @staticmethod
    def profissionais_excluir():
        for obj in Service().profissionais_listar(): print(obj)
        id = int(input('Informe o id do cliente a ser excluido: \n'))
        Service.profissionais_excluir(id)
    def profissionais_pesquisar_nome(): 
        iniciais = input('Insira as inicias: ')
        lista_nomes = Service.profissionais_listar_nomes(iniciais)
        for i in lista_nomes: print(i)
UI.main()