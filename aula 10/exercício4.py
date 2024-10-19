pikachupoderes = ["choque do trovão", "calda de ferro", "ataque rapido", "esquiva"]
print(pikachupoderes)
add = input("Gostaria adicionar um poder novo aos poderes do pikachu?s/n:")
if add == "s":
    addumpoder = input("Coloque aqui o poder:").lower()
    pikachupoderes.append(addumpoder)
    removerpoder = input("Escolha um poder para remover: Choque do trovão, Calda de ferro, Ataque rapido, Esquiva:").lower()
    pikachupoderes.remove(removerpoder)
    print("Os poderes são esses:", pikachupoderes)
else:
    print("Os poderes serão os mesmos então:", pikachupoderes)

