import emoji
print(emoji.emojize('a matemática é :thumbs_up:'))



from operacoes import *
while True:
  y = int(input(' digite seu primeiro valor para realizar alguma operação:'))
  x = int(input(' digite seu segundo valor:'))
  print('se escolher 1, será a soma')
  print('se escolher 2, será a subtração')
  print('se escolher 3, será a multiplicação')
  print('se escolher 4, será a divisão')
  print('se escolher 0, encerrará o código')
  escolha = int(input('digite o número da operação: '))
  if escolha == 0:
      print('obrigado(a) por participar')
      break
  if escolha == 1:
        print(soma(x,y))
  if escolha == 2:
      print(subtracao(x,y))
  if escolha == 3:
       print(multiplicacao(x,y))
  if escolha == 4:
      print(divisao(x,y))
