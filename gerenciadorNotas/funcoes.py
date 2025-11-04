listaNotas = [10, 8, 7 , 5 ]
def calcular_media(listaNotas):
    media = 0
    for n in listaNotas:
        media = sum(listaNotas)
    return media/len(listaNotas)
print(calcular_media(listaNotas))


def verificar_situacao(media):
    if media>=7:
        print("aprovdo")
    elif media>5 and media <6.9:
        print("recuperação")
    elif media<5:
        print("reprovado")
media = calcular_media(listaNotas)
verificar_situacao(media)