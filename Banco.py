'''
apenas 3 operações: depósito, saque e extrato
Depositar apenas valores positivos
Todos os depositos devem ser armazenados em uma variavel e exibido no extrato

regras: 
apenas 3 saques diarios
limite de saque = R$500 -- se n tiver saldo, tem que exibir mensagem por falta de saldo
Saques armazenados em variavel'''

import os

saldo = 0
limite = 500
extrato = ""
numeroSaques = 0
limiteSaques = 3

def depositar():
    global saldo, extrato
    valor = float(input('Digite o valor que deseja depositar: '))
    if valor > 0:    
        saldo +=valor
        print('Depósito realizado com sucesso')
        extrato += f'Depósito: R${valor:.2f}\n'
    else:
        print('Digite um valor válido!')
            
def sacar():
        global saldo, extrato, limite, limiteSaques, numeroSaques

        valor = float(input('Digite o valor que deseja sacar: '))

        excedeuSaldo = valor > saldo

        excedeuLimite = valor > limite

        excedeuSaques = numeroSaques >= limiteSaques

        if excedeuSaldo:
            print('Operação Cancelada! Saldo insuficiente!')
        elif excedeuLimite:
            print(f'Operção Cancelada! Limite de saque RS{limite} atingido')
        elif excedeuSaques:
            print(f'Operação cancelada! O limite de saques diários({limiteSaques}) atingido.')
        elif numeroSaques >= limiteSaques:
            print('Operação Cancelada! Número de saques diários atingido')

        elif valor >limite:
            print("Operação Cancelada! A solicitação excede o valor limite de saque")

        elif valor >0:
            saldo -= valor
            
            print('Saque realizado com sucesso!')
            extrato += f'Saque: R${valor:.2f}\n'
            numeroSaques +=1
def puxarExtrato():
        global saldo, extrato, deposito
        print('~~~~~~~~~~~~~~~~~~~~~')
        if not extrato:
            print('não tem movimentações na sua conta bancária')
        else:
            print(extrato)
            print(f'seu saldo é: {saldo:.2f}')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~')

def sair():
    os.system('cls')
    print('Obrigado por usar o banco! Até Breve.')

def main():
    global saldo, extrato, numeroSaques
    menu = """
[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair

Digite a opção que você deseja: 
    """
    while True:

        opcao = input(menu).lower()

        if opcao =="d":
            depositar()
        elif opcao == 's':
            sacar()
        elif opcao == 'e':
            puxarExtrato()
        elif opcao == 'q':
            sair()
            break
        else: 
            print('Opção Inválida! escolha uma opção válida')

if __name__ == "__main__": #só será executado se o script for o ponto de entrada principal do programa
    main()
