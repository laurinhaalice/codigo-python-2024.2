# Você é um aventureiro carregando uma mochila que comporta 3 itens, atualmente ela tem 3 itens: uma espada, uma poção e um escudo. Ao longo da aventura encontra um arco no chão e prec decidir se o coloca na mochila ou não. Caso coloue, precisará dscarar outro tem a sua escolha. Faça um programa simulando essa e história usando lista/vetor.
mochila= input("Olá, bem vindo ao jogo, você é um aventureiro e ja possui 3 itens em sua mochila. Digite inventário para saber oque você tem.").lower()
inventario = ["Espada", "poção mágica", "escudo"]
if mochila.lower() == "inventario":
    print("Lista de itens:", inventario)
else:
    print("Palavra não indentificada.")
novoitem = input("Vamos começar a sua aventura, vá em frente para comerçarmos sua missão! Ao longo do caminho você encontra um Arco. Deseja coletá-lo?(s/n)")
if novoitem.lower() == "s":
    itemdel = input("Seu inventário está cheio, você terá que deletar um item. Qual item deseja deletar?").lower()
    if itemdel in inventario:
        inventario.remove(itemdel)
        inventario.append("Arco")
        print("Item removido, e Arco adicionado. Aqui a lista:",inventario)
    else:
        print("item não encontrado no inventário.")
else:
    print("Você decidiu não coletar o Arco.")
