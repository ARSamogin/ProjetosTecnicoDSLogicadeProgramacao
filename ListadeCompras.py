compras = []

while True:
   print("Escolha uma opção abaixo: \n" \
   "1 - Adicione um Item a lista \n" \
   "2 - Remova um item da lista \n" \
   "3 - Limpe a lista \n" \
   "4 - Mostre a Lista \n" \
   "5 - Sair")
   opcao = int(input("Escolha uma opção: "))
   
   if opcao == 1:
      produto = str(input("Digite um produto: "))
      compras.append(produto)
   elif opcao == 2:
      produto = str(("Digite o produto para remover: "))
      compras.remove(produto)
   elif opcao == 3:
      compras.clear()
   elif opcao == 4:
      print(compras)
   elif opcao == 5:
      break
   else:
      print("Opção Inválida")