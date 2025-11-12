# o Nome do motorista
# o Destino
# o Distância percorrida (em km)
# o Valor gasto com combustível (em R$)

# consumo = gasto_combustivel / distancia


def registrar_viagem(listaViagens):
    nome = str(input('qual o nome do motorista?'))
    destino = str(input('qual o seu destino?'))
    distancia = float(input('qual a distancia?'))
    valor = float(input('qual o valor gasto do combustivel?'))
    consumo = valor/distancia
    dict = {
        'motorista' : nome,
        'destino' : destino,
        'distancia' : distancia,
        'consumo' : consumo,
        'valor': valor,
    }
    listaViagens.append(dict)
    
    

def exibir_viagens(listaViagens):
    print(listaViagens)


def buscar_motorista(listaViagens, motorista):
    motorista = input("digite qual motorista vc deseja verificar: ")
    resultados = []
    for i in listaViagens:
        if i["motorista"] == motorista:
            resultados.append(i)
    return resultados

def viagem_mais_cara(listaViagens):
    maiorGasto = 0
    for i in listaViagens:
        if i['valor'] >= maiorGasto:
            maiorGasto = i['valor']
    return maiorGasto        

def media_consumo(listaViagens):
    lista = []
    for n in listaViagens:
        if n['consumo']:
            
          
        


