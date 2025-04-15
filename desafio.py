print("Bem-Vindo ao Sistema do ZanBank")

dic_usuarios =  {}

while True:
    
    resposta = input(("Deseja criar uma conta? S/N"))

    if resposta == 's':
        nome = input(("Digite o seu nome: "))
        cpf = input(("Digite o seu cpf: "))
        dic_usuarios["nome"] = nome
        dic_usuarios["cpf"] = cpf
        break

    elif resposta == "n":
        print("Precisa se cadastrar no sistema. ")
    else:
        print("Opção inválida: ")

   
print(dic_usuarios)



print("Selecione umas das opções")
print("[1] - Criar uma conta corrente")
print("[2] - Sacar")
print("[3] - Depositar")
print("[4] - Exibir o extrato")
print("[7] - Sair ")
  
saldo_bancario = 500

limites_para_saques = 10

saques_realizados = 0

extrato = []

conta_corrente = []

saldo_atualizado = 0

def sacar():
    global limites_para_saques, saldo_atualizado
    
    valor_saque = int(input("Digite um valor para sacar: "))

    if valor_saque > saldo_bancario and limites_para_saques < 0:
        print("Saldo insuficiente.")
        print("Limite de saques diários atingido.")
    elif valor_saque < saldo_bancario:
        saldo_atualizado = saldo_bancario - valor_saque 
        limites_para_saques -= 1
        extrato.append(f"Saque: R${valor_saque:.2f}")
        print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
        print(f"Saldo atualizado: R${saldo_atualizado:.2f}")
        print(f"Saques restantes hoje: {limites_para_saques}")

def depositar(): 
    global saldo_atualizado

    valor_depositado = int(input("Digite um valor para depositar: "))
    
    saldo_atualizado_depositado = saldo_atualizado + valor_depositado 
    print(saldo_atualizado_depositado)   


def exibirExtrato():
   
    print("\n---Extrato Bancário---")

    if extrato == 0:
        print(f"O extrato {transacao}")
    else:
        for transacao in extrato:
            print(transacao)

while True:


    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
       
        print("Conta Corrente Criada ")

    elif opcao == 2: 
        sacar()

    elif opcao == 3:
        depositar()
        print("Depositado")
        

    elif opcao == 4:
        exibirExtrato()
        print("Exibindo o extrato")
        
    
    elif opcao == 7:
        print("Saindo do sistema... Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")

