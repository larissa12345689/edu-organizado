import colorama 
print(colorama.Fore.BLUE + "Bem vindo ao gerenciador de notas")


#cadastro de alunos e notas
#exibir relatório de alunos e notas 
x = 1
y = 2
z = 3
listanome = []
listanotas = []
contador = 0
while True:   
    print("1-cadastrar aluno e notas")
    print("2-exibir relatório")
    print("0-sair")
    num = int(input("digite sua opção: "))
    if num == x:
        print("ok, vamos fazer o cadstro.")
        nome = str(input("digite o nome do aluno: "))
        listanome.append(nome)
    nota1 = int(input("digite as tres notas:"))
    nota2 = int(input("digite as tres notas:"))
    nota3 = int(input("digite as tres notas:"))
   
    dict = {f'nome: {listanome}, nota:  {nota1}, nota2: {nota2}, nota3: {nota3}'}
   
    listanotas.append(nota1)
    listanotas.append(nota2)
    listanotas.append(nota3)
    contador +=1
    print(dict)
    