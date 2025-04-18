import datetime

# Lista para armazenar contas
contas = []

# Função para cadastrar nova conta
def cadastrar_conta():
    print("\n=== Cadastro de Conta ===")
    nome = input("Digite seu nome: ")
    numero_conta = int(input("Digite o número da sua conta: "))
    agencia = input("Digite o número da agência: ")
    senha = input("Digite sua senha: ")
    contas.append({
        'nome': nome,
        'cadastro': numero_conta,
        'agencia': agencia,
        'senha': senha,
        'saldo': 0.0,
        'extrato': [],
        'saques_hoje': 0  # contador de saques diários
    })
    print("Conta cadastrada com sucesso!")

# Função para login
def fazer_login():
    print("\n=== Login no Sistema ===")
    entrada_numero = int(input("Digite o número da sua conta: "))
    entrada_senha = input("Digite sua senha: ")

    for conta in contas:
        if conta['cadastro'] == entrada_numero and conta['senha'] == entrada_senha:
            print(f"\nBem-vindo ao banco Tricell, {conta['nome']}!")
            print(f"Agência: {conta['agencia']} | Conta: {conta['cadastro']}")
            menu_operacoes(conta)
            return
    print("Número da conta ou senha incorretos.")

# Função de operações após login
def menu_operacoes(usuario):
    while True:
        print("\nO que deseja fazer agora?")
        print("0 - Saque")
        print("1 - Depósito")
        print("2 - Extrato")
        print("3 - Sair da conta")

        try:
            acao = int(input("Escolha uma opção: "))

            if acao == 0:  # Saque
                if usuario['saques_hoje'] >= 3:
                    print("Limite diário de saques atingido (3 saques por dia).")
                    continue
                valor = float(input("Qual a quantia que deseja sacar? R$ "))
                if valor > 500:
                    print("Limite por saque é de R$ 500,00.")
                elif valor > usuario['saldo']:
                    print("Saldo insuficiente para saque.")
                elif valor <= 0:
                    print("Valor inválido para saque.")
                else:
                    usuario['saldo'] -= valor
                    usuario['saques_hoje'] += 1
                    hora = datetime.datetime.now()
                    usuario['extrato'].append(f"{hora.strftime('%d/%m/%Y %H:%M:%S')} - Saque: -R$ {valor:.2f}")
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

            elif acao == 1:  # Depósito
                valor = float(input("Qual o valor que deseja depositar? R$ "))
                if valor <= 0:
                    print("Valor inválido para depósito.")
                else:
                    usuario['saldo'] += valor
                    hora = datetime.datetime.now()
                    usuario['extrato'].append(f"{hora.strftime('%d/%m/%Y %H:%M:%S')} - Depósito: +R$ {valor:.2f}")
                    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

            elif acao == 2:  # Extrato
                print("\n===== EXTRATO BANCÁRIO =====")
                hora = datetime.datetime.now()
                print(f"Data do extrato: {hora.strftime('%d/%m/%Y %H:%M:%S')}")
                print(f"Agência: {usuario['agencia']} | Conta: {usuario['cadastro']}")
                if usuario['extrato']:
                    for item in usuario['extrato']:
                        print(item)
                else:
                    print("Nenhuma movimentação registrada.")
                print(f"Saldo atual: R$ {usuario['saldo']:.2f}")
                print("=============================")

            elif acao == 3:
                print("Saindo da conta...")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError:
            print("Por favor, digite apenas números.")

# Menu principal do sistema
while True:
    print("\n=== BANCO TRICELL ===")
    print("1 - Cadastrar nova conta")
    print("2 - Entrar")
    print("3 - Sair do sistema")

    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_conta()
        elif opcao == 2:
            if not contas:
                print("Nenhuma conta cadastrada ainda. Cadastre primeiro.")
            else:
                fazer_login()
        elif opcao == 3:
            print("Saindo do sistema... Obrigado por usar o Banco Tricell!")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Digite um número válido.")
