print("Sistema do ZanBank")
print("Selecione umas das opções")

print("[1] - Sacar")
print("[2] - Depositar")
print("[3] - Exibir o extrato")
print("[7] - Sair " )
  
saldo_bancario = 500

limites_para_saques = 3

saques_realizados = 0

extrato = []

saldo_bancario_atualizado = 0


def sacar():
    global saldo_bancario, limites_para_saques  
    
    valor_saque = int(input("Digite um valor para sacar: "))

    if valor_saque > saldo_bancario:
        print("Saldo insuficiente.")
    elif limites_para_saques <= 0:
        print("Limite de saques diários atingido.")
    else:
        saldo_bancario -= valor_saque
        limites_para_saques -= 1
        extrato.append(f"Saque: R${valor_saque:.2f}")
        print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
        print(f"Saldo atualizado: R${saldo_bancario:.2f}")
        print(f"Saques restantes hoje: {limites_para_saques}")


def depositar():
    valor_depositado = int(input("Digite um valor para depositar: "))
    print("Deposito realizado com sucesso")
   
    
    saldo_bancario_atualizado = saldo_bancario + valor_depositado
    extrato.append(f"Depósito: R${valor_depositado:.2f}")
    print(f"Depósito de R${valor_depositado:.2f} realizado com sucesso!")
    print(f"O valor do saldo é {saldo_bancario_atualizado}")

def exibirExtrato():
   
   print("\n--- Extrato Bancário ---")
if len(extrato) == 0:
        print("Não há transações registradas.")
else:
        for transacao in extrato:
            print(transacao)
        print(f"Saldo Atual: R${saldo_bancario:.2f}")
        

while True:

    opcao = int(input("Escolha uma opção: "))


    if opcao == 1: 
        sacar()
    
    elif opcao == 2:
        depositar()
        print("Depositado")
        

    elif opcao == 3:
        exibirExtrato()
        print("Exibindo o extrato")
        
    
    elif opcao == 7:
        print("Saindo do sistema... Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")

