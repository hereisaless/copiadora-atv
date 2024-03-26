#Atribuição das funções escolha_serviço()
def escolha_servico():
  print('--------------------------------------------------------------------------')
  print('--------------|    Escolha o serviço:       | Valores por unidade:|-------')
  print('--------------|  DIG - Digitalização        |       R$ 1,10       |-------')
  print('--------------|  ICO - Impressão colorida   |       R$ 1,00       |-------')
  print('--------------|  IPB - Impressão P&B        |       R$ 0,40       |-------')
  print('--------------|  FOT - Fotocópia            |       R$ 0,20       |-------')
  print('--------------------------------------------------------------------------')
  while True:
    servico = input('>>')
    servico = servico.upper()
    if servico != 'DIG' and servico != 'ICO' and servico != 'IPB' and servico != 'FOT':
      print('Serviço inválido. Tente novamente!')
    if servico == 'DIG':
       return  1.10
    elif servico == 'ICO':
       return  1
    elif servico == 'IPB':
       return 0.40
    elif servico == 'FOT':
       return 0.20
#Atribuição das funções num_pagina para cálculo do desconto e retorno da pergunta inicial
def num_pagina():
  while True:
    try:
      quantidade = int(input('Digite a quantidade de páginas: '))
      if quantidade <= 10:
        return quantidade
      elif quantidade <= 100:
        return quantidade * 0.85
      elif quantidade <= 1000:
        return quantidade * 0.90
      elif quantidade <= 10000:
        return quantidade * 0.95
      else:
        print('Número de páginas inválido. Tente novamente!')
    except:
        print('Número de páginas inválido.')

#Atribuição das funções servico_extra()
def servico_extra():
  print('--------------------------------------------------------------------------')
  print('--------------|       Serviço extra:        |  Valor por unidade: |-------')
  print('--------------|  1 - Encadernação simples   |      R$ 10,00       |-------')
  print('--------------|  2 - Encadernação capa dura |      R$ 25,00       |-------')
  print('--------------|  0 - Continuar sem extra    |      R$ 00,00       |-------')
  print('--------------------------------------------------------------------------')
  acumulador = 0
  while True:
    extra = input('Deseja mais alguma coisa? ')
    if extra == '1':
      return acumulador + 10
    elif extra == '2':
      return acumulador + 25
    elif extra == '0':
      return acumulador
    else:
      print('Opção inválida!')
      break
#Função de saída
print('Seja bem-vindo(a) a copiadora JB - Alessandra de Souza Oliveira')
servico = escolha_servico()
paginas = num_pagina()
extra = servico_extra()
total = servico * paginas + extra
print(f'Total R$ {total:.2f} (Serviço: {servico} * página(s): {paginas} + extra(s): {extra})')
print('Agradecemos pela preferência, até a próxima!')