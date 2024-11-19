from modulos.models_text import *
from modulos.models_sql import *
from time import sleep
import sqlite3

conn = sqlite3.connect('banco_de_dados.db')

cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        quantidade INTEGER,
        preço REAL
    )
''')

def main():
    while True:
        sleep(1)
        cabeçalho(simbolo='=', titulo=' CONTROLE DE ESTOQUE ')
        menu()
        opc = int(input('Digite a opção: '))
        pulaLinha('=')
        sleep(2)
        if opc != 1 and opc != 2 and opc != 3 and opc != 4 and opc != 0:
            print('Opção inválida!')
            pulaLinha('=')
        elif opc == 1:
            nome = str(input('Nome do produto: '))
            quantidade = int(input('Quantidade: '))
            preco = float(input('Valor do produto: '))
            print(f'Produto {nome} adcionado com sucesso!')
            adcionarProduto(cursor, nome, quantidade, preco)
            conn.commit()

        elif opc == 2:
            mostrarProdutos(cursor)
            pulaLinha('=')
            nome_deletado = input('Nome a ser deletado: ')
            excluirProduto(cursor, nome_deletado)
            print(f"Produto '{nome_deletado}' deletado com sucesso!")
            conn.commit()

        elif opc == 3:
            print(' Produtos Disponíveis '.center(50, '='))
            mostrarProdutos(cursor)
            pulaLinha('=')
            id_produto = int(input('ID: '))
            novo_nome = input('Novo Produto: ')
            nova_quantidade = int(input('Nova quantidade: '))
            novo_preco = float(input('Novo preço: R$'))
            modificarProduto(cursor, novo_nome, nova_quantidade,novo_preco, id_produto)
            print('Produto atualizado com sucesso!')
            conn.commit()

        elif opc == 4:
            cabeçalho(simbolo='=', titulo=' ESTOQUE DA LOJA ')
            mostrarProdutos(cursor)
            pulaLinha('=')

        elif opc == 0:
            cabeçalho(simbolo='=', titulo='>>>>>> FINALIZANDO <<<<<<'.center(50))
            sleep(2)
            conn.commit()
            conn.close()
            break