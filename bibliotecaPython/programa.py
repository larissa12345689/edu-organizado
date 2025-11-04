from funcoes import *

listaLivros = [
    {"nome":'pequeno pricipe', "status":'disponivel'},
]   
print("1-  Adicionar livro")
print("2-  Exibir todos os livros")
print("3-  Emprestar livro")
print("4-  Devolver livro")
print("0-  Sair")
while True:
    escolha = int(input( 'digite o número de sua escolha: '))
    if escolha == 1:
        adicionar_livro(listaLivros)
    if escolha == 2:
        print(listaLivros)
    if escolha == 3:
        emprestar_livro(listaLivros)
    if escolha == 4:
        devolver_livro(listaLivros)
    if escolha == 0:
        break      
          
          

   