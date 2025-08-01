from conta import Conta 
import maskpass
import csv

contas = []
conEnc = None
acessLiberado = False

def lerArquivo():
    with open('contas.csv', newline="", encoding='utf-8', errors='ignore') as lerCont:
        leitor = csv.reader(lerCont, delimiter=',')
        for l in leitor:
            # Ajuste os índices conforme seu CSV: aqui assumo
            # l[0] = agencia (int), l[1] = numero da conta (str), l[2] = senha (str), l[3] = saldo (float), l[4] = nome/titular (str)
            conta = Conta(int(l[0]), l[1], l[2], float(l[3]), l[4])
            contas.append(conta)

def encontraConta(agencia, numCon):
    global conEnc
    for conta in contas:
        # Atenção aqui: ajuste o nome do atributo que representa o número da conta na classe Conta
        if conta.agencia == agencia and conta.numero == numCon:
            conEnc = conta
            break 

def verificaAcess(numCon, senha):
    global acessLiberado
    if conEnc is not None:
        if conEnc.entrar(numCon, senha):
            print('Acesso liberado')
            acessLiberado = True
        else:
            print('Senha incorreta')
    else:
        print('Conta não encontrada')

def buscarContaPorNumero(numContaDestino):
    for conta in contas:
        if conta.numero == numContaDestino:
            return conta
    return None

def inicia():
    global acessLiberado
    global conEnc
    acessLiberado = False
    conEnc = None

    lerArquivo()
    agencia = int(input('Digite o número da sua agencia: '))
    numCon = input('Digite o número da conta: ')
    senha = maskpass.askpass(prompt="Digite sua senha: ", mask="*")

    encontraConta(agencia, numCon)
    verificaAcess(numCon, senha)

inicia()

while acessLiberado:
    print('\nEscolha o número da opção desejada:')
    print('1 - Extrato')
    print('2 - Saque')
    print('3 - Depósito')
    print('4 - Transferir')
    print('5 - Sair')

    transacao = int(input('Digite a opção: '))

    if transacao == 1:
        print(f'O saldo da conta é R$:{conEnc.extrato()}')

    elif transacao == 2:
        valor = float(input('R$: '))
        sucesso = conEnc.sacar(valor)
        if sucesso:
            print('Saque realizado')
        else:
            print('Saque inválido')

    elif transacao == 3:
        valor = float(input('R$: '))
        sucesso = conEnc.depositar(valor)
        if sucesso:
            print('Depósito realizado')
        else:
            print('Depósito negado')

    elif transacao == 4:
        valor = float(input('R$: '))
        numContaDestino = input('Número Conta: ')
        contaDestino = buscarContaPorNumero(numContaDestino)
        if contaDestino:
            sucesso = conEnc.transferir(valor, contaDestino)
            if sucesso:
                print('Transferência realizada')
            else:
                print('Transferência negada')
        else:
            print('Conta destino não encontrada')

    elif transacao == 5:
        print('Saindo... Obrigado!')
        break

    else:
        print('Opção incorreta')
