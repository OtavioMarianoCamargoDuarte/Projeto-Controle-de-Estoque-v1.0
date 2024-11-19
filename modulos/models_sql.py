from modulos.models_text import *


def adcionarProduto(cursor, nome, quantidade, preco):
    cursor.execute('''
        INSERT INTO produtos (nome, quantidade, preço) VALUES(?, ?, ?)       
    ''', (nome, quantidade, preco))


def modificarProduto(cursor, novo_nome, nova_quantidade, novo_preco, id_produto):
    cursor.execute('''
        UPDATE produtos
        SET nome = ?, quantidade = ?, preço = ?
        WHERE id = ?
    ''', (novo_nome, nova_quantidade, novo_preco, id_produto))


def excluirProduto(cursor, nome_deletado):
    cursor.execute('''
        DELETE FROM produtos WHERE nome = ?
''', (nome_deletado,))


def mostrarProdutos(cursor):
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    print(f'| {'ID':^3} | {'NOME':^20} | {'QTD':^5} | {'PREÇO(R$)':>8} |')
    pulaLinha('=')
    for produto in produtos:
        print(f'| {produto[0]:^3} | {produto[1]:<20} | {produto[2]:^5} | R${produto[3]:>7.2f} |')
