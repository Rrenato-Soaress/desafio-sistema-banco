menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Operacao falhou! O valor informado e invalido:")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = valor > limite

        if excedeu_saldo:
            print("Operacao falhou! Voce nao tem saldo suficiente:")

        elif excedeu_limite:
            print("Operacao falhou! O valor do saque excede o limite:")

        elif excedeu_saques:
            print("OPeracao falhou! Numero maximo de saques permitido para hoje:")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$  {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operacao falhou! O valor informado é invalido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================" )
        print("Nao foram realizadas movimentacoes." if not extrato else extrato )
        print( f"\nsaldo: R$ {saldo:.2f}")
        print("============================================")

    elif opcao == "q":
        break

    else:
        print("Operacao invalida! Por favor selecione novamente a operacao desejada.")     

