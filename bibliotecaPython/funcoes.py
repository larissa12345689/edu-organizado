def adicionar_livro(listaLivros):
    obra = str(input("digite o título da obra: "))
    autor = str(input("digite o autor da obra: "))
    status = "disponível"

    dict = {
        "nome":obra,
        "autor":autor,
        "status": status
    }
    listaLivros.append(dict)



def emprestar_livro(listaLivros):
    livro = str(input("qual livro vc deseja pegar?:  "))
    for i in listaLivros:
        if livro == i['nome']:
            print("livro disponível")
            resp = str(input("vc deseja pegar esse livro? digite sim ou não: "))
            if resp == "sim":
                i["status"] = "alugado"
                print(i)
        
    return listaLivros
listaLivros = [
    {"livro":'pequeno pricipe', "status":'disponivel'},
    {"livro":'sereia', "status":'disponivel'},
    {"livro":'castelo', "status":'disponivel'},
    {"livro":'ratimbum', "status":'disponivel'}
]




def devolver_livro(listaLivros):
    resposta = str(input("vc deseja devolver algum livro?: "))
    if resposta == 'sim':
       livros = input("qual livro vc deseja devolver?: ")
       for livros in listaLivros:
           status = "disponível"

            
