# Direito a meia-entrada
estudante = input("Você é estudante?(sim/não)").lower()
sessentaanosoumais = input("Você tem 60 anos ou mais?(sim/não)").lower()
deficiência = input("Você possui alguma deficiência(sim/não)").lower()
cadastroúnico = input("Você tem cadastro único?(sim//não)").lower()
profredepubliRJ = input("Você é professor de rede pública muncipal do RJ?(sim/não)").lower()
    

if estudante =="sim" or sessentaanosoumais =="sim" or deficiência =="sim" or cadastroúnico =="sim" or profredepubliRJ =="sim":
        print("Você tem direito à meia-entrada.")
else:
    print("Você não tem direito à meia-entrada.")

verificaçao = input("Deseja fazer verificação para outra pessoa?(sim/não)").lower()
     
    if verificaçao =="sim":
      estudante = input("Você é estudante?(sim/não)").lower()
sessentaanosoumais = input("Você tem 60 anos ou mais?(sim/não)").lower()
deficiência = input("Você possui alguma deficiência(sim/não)").lower()
cadastroúnico = input("Você tem cadastro único?(sim//não)").lower()
profredepubliRJ = input("Você é professor de rede pública muncipal do RJ?(sim/não)").lower()

    elif verificaçao =="não":
        print("Sistema de verificação encerrado.")