print('===== EXERCICIO 011 =====')
print('Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2')

larg = float(input("Digite a largura da parede em metros: "))
altu = float(input('Digite a altura da parede em metros: '))
area = larg * altu
litros = area / 2

print('A largura e altura respectivamente são {}m e {}m, a área da parede é {}m² e são necessários {}L de tinta para pintá-la'.format(larg, altu, area, litros))
