contagem = {
        'papel': 0,
        'plástico': 0,
        'vidro': 0,
        'metal': 0,
        'orgânico': 0,
        'não reciclável': 0
    }

print("Bem-vindo ao programa de reciclagem!")

while True:
        # Solicita o tipo de material
        material = input("Informe o tipo de material que deseja reciclar (papel, plástico, vidro, metal, orgânico ou resíduos não recicláveis): ").strip().lower()

        
        if material == 'papel':
            contagem['papel'] += 1
            print("Cor da lixeira: azul.")
        elif material == 'plástico':
            contagem['plástico'] += 1
            print("Cor da lixeira: vermelha.")
        elif material == 'vidro':
            contagem['vidro'] += 1
            print("Cor da lixeira: verde.")
        elif material == 'metal':
            contagem['metal'] += 1
            print("Cor da lixeira: amarela.")
        elif material == 'orgânico':
            contagem['orgânico'] += 1
            print("Cor da lixeira: marrom.")
        elif material == 'resíduos não recicláveis':
            contagem['não reciclável'] += 1
            print("Cor da lixeira: cinza.")
        else:
            print("Erro! Tente novamente.")
            continue

        
        continuar = input("Deseja continuar reciclando? (s/n): ").strip().lower()
        if continuar != 's':
            break

    
print("\nResumo da reciclagem:")
for material, quantidade in contagem.items():
        print(f"{material.capitalize()}: {quantidade} unidades")

print("Obrigado por contribuir com a reciclagem!")


                