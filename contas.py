def cria_conta (numero, titular, saldo, limite):
    conta  = {"numero":numero, "titular":titular, "saldo":saldo, "limite:":limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"]-=valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))

conta1 = cria_conta(123, "Nico", 55.0, 1000.0)
print(conta1)
