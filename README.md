# Sistema de Controle de Estoque
Este é um sistema simples para controle de estoque desenvolvido em Python, utilizando o banco de dados SQLite. Ele permite a adição, remoção, modificação e visualização de produtos em um banco de dados local. O projeto foi criado com foco em simplicidade e funcionalidade, sendo ideal para iniciantes em programação e bancos de dados.

# Descrição
O sistema realiza as seguintes operações:
- Adicionar Produto: Insere novos produtos no banco de dados.
- Remover Produto: Exclui produtos do banco de dados.
- Atualizar Produto: Modifica dados de um produto já existente.
- Visualizar Produtos: Exibe a lista de todos os produtos no estoque.

# Tecnologias
- Python: Linguagem de programação principal.
- SQLite: Banco de dados local para armazenamento dos produtos.
- Modularização: O código está dividido em módulos para melhor organização e reutilização das funções.

# Estrutura de Diretórios
bash
Copiar código
├── Modulos
│   ├── models_app.py        # Funções para interações gerais do aplicativo
│   ├── models_sql.py        # Funções para operações no banco de dados
│   └── models_text.py       # Funções para interface com o usuário (exibição de menus, cabeçalhos, etc.)
├── app.py                   # Arquivo principal que executa o programa
└── banco_de_dados.db        # Banco de dados SQLite

# Instalação
- Clone o repositório:
git clone https://github.com/seu-usuario/seu-repositorio.git
- Navegue até o diretório do projeto:
cd seu-repositorio
- Instale as dependências necessárias (se houver):
pip install -r requirements.txt
- Execute o programa:
python app.py

# Funcionalidades
1. Adicionar Produto
- O usuário pode adicionar um novo produto informando o nome, quantidade e preço.
- O produto será armazenado no banco de dados SQLite.
2. Remover Produto
- O usuário pode remover um produto informando o nome do produto a ser excluído.
- O produto será deletado do banco de dados.
3. Atualizar Produto
- O usuário pode atualizar os dados de um produto existente.
- O usuário pode alterar o nome, a quantidade e o preço de um produto.
4. Visualizar Produtos
- O usuário pode visualizar todos os produtos cadastrados no estoque.

# Melhorias Futuras
- Tratamento de Dados: Adicionar validação e tratamento de erros para entrada de dados, como verificar se os campos estão vazios ou se os valores inseridos são válidos.
- Docstrings: Implementação de docstrings nas funções para uma melhor documentação e entendimento do código.
- Interface Gráfica (GUI): Desenvolvimento de uma interface gráfica para facilitar o uso do sistema, utilizando bibliotecas como Tkinter ou PyQt.
