def saque(conta, *, valor, limite, numero_saques, limite_saques):
    saldo = conta['saldo']
    extrato_str = conta['extrato']
    
    if valor <= 0:
        return saldo, extrato_str, numero_saques, "Erro! Valor inválido."

    if valor > saldo:
        return saldo, extrato_str, numero_saques, "Erro! Saldo insuficiente."

    if valor > limite:
        return saldo, extrato_str, numero_saques, "Erro! Valor do saque excede o limite."

    if numero_saques >= limite_saques:
        return saldo, extrato_str, numero_saques, "Erro! Número máximo de saques diário excedido."

    saldo -= valor
    extrato_str += f"\tSaque: R$ {valor:.2f}\n"
    numero_saques += 1
    conta['saldo'] = saldo
    conta['extrato'] = extrato_str
    conta['numero_saques'] = numero_saques
    return saldo, extrato_str, numero_saques, "Saque concluído com sucesso!"

def deposito(conta, valor):
    saldo = conta['saldo']
    extrato_str = conta['extrato']
    
    if valor <= 0:
        return saldo, extrato_str, "Erro! Valor inválido."

    saldo += valor
    extrato_str += f"\tDepósito: R$ {valor:.2f}\n"
    conta['saldo'] = saldo
    conta['extrato'] = extrato_str
    return saldo, extrato_str, "Depósito concluído com sucesso!"

def exibir_extrato(conta):
    saldo = conta['saldo']
    extrato_str = conta['extrato']
    
    print("\n\t**************** EXTRATO ****************")
    print("\tSem movimentações." if not extrato_str else extrato_str)
    print(f"\n\tSaldo: R$ {saldo:.2f}")
    print("\t*****************************************")
    print("Extrato exibido com sucesso!")

usuarios = []
contas = []
NUM_AGENCIA = "0001"
NUM_CONTAS = 1  

def criar_usuario(nome, data_nascimento, cpf, endereco):
    cpf = cpf.replace('.', '').replace('-', '') 
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Erro! Usuário já cadastrado com esse CPF.")
        return

    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")

def criar_conta_corrente(cpf):
    if not any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Erro! Usuário não encontrado.")
        return

    global NUM_CONTAS
    conta = {
        'agencia': NUM_AGENCIA,
        'numero': NUM_CONTAS,
        'cpf': cpf,
        'saldo': 0,
        'extrato': "",
        'numero_saques': 0
    }
    contas.append(conta)
    NUM_CONTAS += 1
    print(f"Conta corrente criada com sucesso! Número: {conta['numero']}")

def listar_contas():
    if not contas:
        print("Nenhuma conta corrente cadastrada.")
        return

    print("\n\t**************** CONTAS ****************")
    for conta in contas:
        print(f"Agência: {conta['agencia']} | Número: {conta['numero']} | CPF: {conta['cpf']}")
    print("\t*****************************************")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("\n\t**************** USUÁRIOS ****************")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']} | Data Nascimento: {usuario['data_nascimento']} | CPF: {usuario['cpf']} | Endereço: {usuario['endereco']}")
    print("\t*****************************************")

def selecionar_conta():
    listar_contas()
    numero_conta = int(input("\tDigite o número da conta: "))
    conta = next((c for c in contas if c['numero'] == numero_conta), None)
    if conta is None:
        print("Erro! Conta não encontrada.")
    return conta

def menu_bancario():
    limite = 500
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)

        if opcao == "1":
            conta = selecionar_conta()
            if conta:
                valor = float(input("\tQual valor deseja depositar? "))
                saldo, extrato_str, erro = deposito(conta, valor)
                if erro:
                    print(f"\t{erro}")
                else:
                    print("Depósito concluído com sucesso!")

        elif opcao == "2":
            conta = selecionar_conta()
            if conta:
                valor = float(input("\tQual valor deseja sacar? "))
                saldo, extrato_str, numero_saques, erro = saque(
                    conta, valor=valor, limite=limite,
                    numero_saques=conta['numero_saques'], limite_saques=LIMITE_SAQUES
                )
                if erro:
                    print(f"\t{erro}")
                else:
                    print("Saque concluído com sucesso!")

        elif opcao == "3":
            conta = selecionar_conta()
            if conta:
                exibir_extrato(conta)

        elif opcao == "4":
            nome = input("\tNome do usuário: ")
            data_nascimento = input("\tData de nascimento (dd/mm/aaaa): ")
            cpf = input("\tCPF (apenas números): ")
            endereco = input("\tEndereço (logradouro, nro - bairro - cidade/sigla estado): ")
            criar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == "5":
            cpf = input("\tCPF do usuário para criar a conta (apenas números): ")
            criar_conta_corrente(cpf)

        elif opcao == "6":
            listar_usuarios()

        elif opcao == "7":
            listar_contas()

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("\tErro! Selecione uma operação válida.")

menu = """\n
    -+-+-+-+-+-+ Banco Python +-+-+-+-+-+-
    **************** MENU ****************
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tCriar Usuário
    [5]\tCriar Conta Corrente
    [6]\tListar Usuários
    [7]\tListar Contas Correntes
    [0]\tSair
    => """

menu_bancario()