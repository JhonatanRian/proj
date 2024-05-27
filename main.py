print("olá mundo")

print("Estou estudando python")

idade = input("Qual sua idade? ")

nome = input("Qual seu nome? ")

print(f"Olá {nome}, como vai?")

confirmar = input(f"Você tem {idade} anos? ")

if confirmar == "s":
    print("Será?")
    if int(idade) >= 18:
        print("Você está falando a verdade")
        print("Acesso ao conteudo")
    else:
        print("Você não está falando a verdade")
else:
    print("Você não tem acesso ao conteúdo")
