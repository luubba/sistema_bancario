usuario = input("Digite seu nome: ")
saldo = 1000
option = ""

print(f"""
========= BANCO DO BRASIL ==========

Seja bem-vindo, {usuario}
Seu saldo é de: R$ {saldo},00
""")
while option != 4:

  option = input(f"""
  ========= BANCO DO BRASIL ==========

  O que deseja fazer a seguir:

  1. Realizar Saque;
  2. Realizar Depósito;
  3. Exibir Saldo;
  4. Sair
  """)
  match option:
    case "1":
      valor_saque = input("Digite o valor: R$ ")
      saldo -= int(valor_saque)
      if int(saldo) <= 0:
        print("Você nãp tem mais dinheiro seu pobre")
      elif int(valor_saque) > int(saldo):
        print("Você não tem esse dinheiro todo")
    case "2":
      valor_deposito = input("Digite o valor: R$ ")
      saldo += int(valor_deposito)
    case "3":
      print(f'''
      ========= BANCO DO BRASIL ==========
      
      Seu saldo é de {saldo}''')
    case "4":
      print("Encerrando...")
      break
    case "5":
      print("opção Inválida")



