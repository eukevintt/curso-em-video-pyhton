print('===== EXERCICIO 006 =====')
print('Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada')

n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print('O número escolhido foi {}, o dobro dele é {}, o triplo dele é {} e a raiz quadrada dele é {:.2f}'. format(n, dobro, triplo,raiz))
