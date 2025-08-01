import random
import getpass 
from conta import Conta

import csv
def escreveArquivo(agencia, numero, titular, saldo, senha):
    with open('contas.csv', 'a', newline='') as csvfile:
        escritor = csv.writer(csvfile, delimiter=',')
        escritor.writerow([agencia, numero, titular, saldo, senha])


while(True):
    print("### CADASTRO DE CONTA B0ANCÁRIAS - BANCO VAI LÉO ###")
    print("Preencha os seguintes dados:")
    agencia = int(input("Número da agência: "))
    numero = random.randint(10000, 99999)
    titular = input("Nome do cliente: ")
    saldo = float(input("Saldo inicial: "))
    senha = getpass.getpass ("Digite uma nova senha: ")
    escreveArquivo(agencia, numero, titular, saldo, senha)
    novaConta = Conta(agencia, numero, titular, saldo, senha)
    print(f'Conta {novaConta.numero}criada com sucesso!\n')
