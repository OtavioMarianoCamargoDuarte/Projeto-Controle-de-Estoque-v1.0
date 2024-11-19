def cabeçalho(simbolo='-', quantidade=50, titulo='Titulo'):
    print(simbolo * quantidade)
    print(f' {titulo} '.center(50))
    print(simbolo * quantidade)


def pulaLinha(simbolo = '-', quantidade = 50):
    print(simbolo * quantidade)


def menu():
    pulaLinha('=', 50)
    print('[1] - ADCIONAR ITEM\n[2] - REMOVER ITEM\n[3] - ATUALIZAR ITEM\n[4] - VER PRODUTOS\n[0] - SAIR DO PROGRAMA')
    pulaLinha('=', 50)
    