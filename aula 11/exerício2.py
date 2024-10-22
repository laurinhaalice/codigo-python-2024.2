mochila= input("Olá, bem vindo ao jogo, você é um aventureiro e ja possui 3 itens em sua mochila. Digite inventário para saber oque você tem.").lower()
inventario = ["Espada", "poção mágica", "escudo"]
if mochila.lower() in "inventario":
    print("Lista de itens:", inventario)
else:
    print("Palavra não indentificada.")
novoitem = input("Vamos começar a sua aventura, vá em frente para comerçarmos sua missão! Ao longo do caminho você encontra um Arco. Deseja coletá-lo?(s/n)")
if novoitem in "s":
    itemdel = input("Seu inventário está cheio, você terá que deletar um item. Qual item deseja deletar?").lower()
    if itemdel in inventario:
        inventario.remove(itemdel)
        inventario.append("Arco")
        print("Item removido, e Arco adicionado. Aqui a lista:",inventario)
    else:
        print("item não encontrado no inventário.")
else:
    print("Você decidiu não coletar o Arco.")

bandidofloresta = input("Você está andando pela floresta e pelo cominho você enconta um bandido, ameaçando você para entregar sua poção. Você tem a opção de: (1- lutar com ele/2- entregar a poção para ele.)")
if bandidofloresta == "1":
    print("Você lutará com ele. Pegue sua espada!")
    if "Espada" in inventario:
        print("Você conseguiu! Continue seu caminho pela floresta.")
    else:
        print("Você perdeu. O bandido se zangou. Fim do jogo.")
elif bandidofloresta == "2":
        print("Você entregará a poção a ele.")
        if "poção mágica" in inventario:
            print("Você entregou a poção a ele, você agora está sem poção. Continue seu caminho.")
        else:
            print("Você não tem a poção para entrega-lo, ele se irritou. \nVocê perdeu o jogo.")
else:
    print("o bandido te atacou pois você demorou muito. \nFim do jogo.")