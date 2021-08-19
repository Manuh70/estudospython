from time import sleep

numeros = [
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59,
     61, 63],
    [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31, 34, 35, 38, 39, 42, 43, 46, 47, 50, 51, 54, 55, 58, 59,
     62, 63],
    [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31, 36, 37, 38, 39, 44, 45, 46, 47, 52, 53, 54, 55, 60, 61,
     62, 63],
    [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31, 40, 41, 42, 43, 44, 45, 46, 47, 56, 57, 58, 59, 60,
     61, 62, 63],
    [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
     61, 62, 63],
    [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
     61, 62, 63]]
nova = 0
resultado = 0
print('-' * 30)
print('SEJA BEM VINDO AO PROGRAMA QUE VAI LER A SUA MENTE')
print('PENSE EM UM NÚMERO DE 1 ATÉ 60')
print('-' * 30)

# Essa é a repetição que vai perguntar seis vezes se o usuário viu o número
for numPrincipal in range(0, 6):
    nova = 0

    # Essa é repetição que vai mostrar o bloco de números completo
    for numPrimeiroBloco in range(0, len(numeros[numPrincipal]) // 4):

        # Essa repeção vai mostrar as quatro linhas do código
        for numLinhas in range(nova, nova + 4):
            print('{} '.format(numeros[numPrincipal][numLinhas]), end='')
        nova = nova + 4
        print('')

    opcao = input('O número que você pensou apareceu acima? [S/N]')
    if opcao in 'Ss':
        resultado = resultado + numeros[numPrincipal][0]

print('')
print('-' * 40)
print('Estou pensando ... ')
sleep(4)
print('-' * 40)
print('')

print('Você pensou no número {}'.format(resultado))
print('-' * 40)
