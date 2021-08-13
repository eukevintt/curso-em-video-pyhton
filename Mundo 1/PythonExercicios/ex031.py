print('Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando 0,50 por km para viagens de até 200km e 0,45 para viagens mais longas')

distTravel = float(input('Qual a distância da viagem? '))

if distTravel <= 200:
    precoPass = distTravel * 0.50
    print('O preço da passagem será cobrado R$0,50 por km. Seu preço é R${}'.format(precoPass))
else:
    precoPass = distTravel * 0.45
    print('O preço da passagem será cobrado R$0,45 por km. Seu preço é R${}'.format(precoPass))
