'''https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py

apenas 3 operações: depósito, saque e extrato
Depositar apenas valores positivos
Todos os depositos devem ser armazenados em uma variavel e exibido no extrato

regras: apenas 3 saques diarios
limite de saque = R$500 -- se n tiver saldo, tem que exibir mensagem por falta de saldo
Saques armazenados em variavel

'''
import os
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Digite a opção que você deseja: 
"""
saldo = 0
limite = 500
extrato = ""
numeroSaques = 0
limiteSaques = 3

while True:

    opcao = input(menu).lower

    if opcao == 'd':

        valor = float(input('Digite o valor que deseja depositar: '))
        if valor > 0:
            saldo +=valor
            print('Depósito realizado com sucesso')
            extrato += f'Depósito: R${valor:.2f}\n'
            
    elif opcao == 's':
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

    elif opcao == "e":
        print('~~~~~~~~~~~~~~~~~~~~~')
        if not extrato:
            print('não tem movimentações na sua conta bancária')
        else:
            print(extrato)
            print(f'seu saldo é: {saldo:.2f}')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~')

    elif opcao == 'q':
        os.system('cls')
        print('Obrigado por usar o banco! Até Breve.')
        
        break

    else: 
        print('Opção Inválida! escolha uma opção válida')
