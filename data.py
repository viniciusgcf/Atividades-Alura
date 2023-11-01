def iniciar():
 dia1()
 mes1()
 ano1()
 final()

def dia1():
  dia = int(input("Digite o dia de seu nascimento: "))
  if (dia < 1):
    print ("O dia tem que ser maior que 1")
    return dia1()
  if (dia > 31):
   print ("O dia tem que ser menor que 31")
   return dia1()
    
def mes1():
  mes = int(input("Digite o seu mes de nascimento: "))
  if (mes < 1):
    print ("O mes tem que ser maior que 1")
    return mes1()
  if (mes > 12):
    print ("O mes tem que ser 12 ou menor")
    return mes1()
  
def ano1():
  ano = int(input("Digite o seu ano de nascimento: "))
  if (ano > 2024):
    return ano1()
  
def final (dia, mes, ano):
  print ("Sua data de nascimento é: ", dia, mes, ano)
