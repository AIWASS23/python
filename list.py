# Lista de produtos
produtos = []

def cadastrar_produto():
    print("\nCadastro de Produto")
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")
    valor = float(input("Valor do produto: "))
    disponivel = input("Disponível para venda (sim/não): ").lower() == 'sim'
    
    produto = {
        'nome': nome,
        'descricao': descricao,
        'valor': valor,
        'disponivel': disponivel
    }
    
    produtos.append(produto)
    produtos.sort(key=lambda x: x['valor'])
    print("\nProduto cadastrado com sucesso!")

def listar_produtos():
    print("\nListagem de Produtos")
    print("Nome\t|\tValor")
    print("--------------------------")
    for produto in produtos:
        print(f"{produto['nome']}\t|\tR$ {produto['valor']:.2f}")

while True:
    print("\nEscolha uma opção:")
    print("1 - Cadastrar novo produto")
    print("2 - Listar produtos")
    print("3 - Sair")
    
    opcao = input("Opção: ")
    
    if opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        listar_produtos()
    elif opcao == '3':
        break
    else:
        print("Opção inválida. Tente novamente.")
