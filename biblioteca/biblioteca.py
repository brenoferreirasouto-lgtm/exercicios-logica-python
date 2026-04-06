biblioteca = [
    {'titulo': '1984', 'autor': 'George Orwell', 'ano': 1949, 'disponivel': True},
    {'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien', 'ano': 1954, 'disponivel': True},
    {'titulo': 'Dom Casmurro', 'autor': 'Machado de Assis', 'ano': 1899, 'disponivel': False},
    {'titulo': 'O Cortiço', 'autor': 'Aluísio Azevedo', 'ano': 1890, 'disponivel': True}
]

def livro_disponivel():
    disponiveis = 0
    for livro in biblioteca:
        if livro['disponivel']:
            disponiveis += 1 
    return disponiveis

def livros_emprestados(): 
    emprestados = 0
    for livro in biblioteca:
        if not livro['disponivel']:
            emprestados += 1
    return emprestados

while True:

    print('-' * 55)
    print('\n1 - Listar todos os livros e sua disponibilidade')
    print('2 - Emprestar um livro (muda disponivel para False)')
    print('3 - Devolver um livro (muda disponivel para True)')
    print('4 - Buscar livros por autor')
    print('5 - Mostrar estatisticas (total, disponiveis, emprestados)')
    print('6 - Sair')
    print('-' * 55)

    try:
        escolha = int(input('\nEscolha uma opção: '))
    except ValueError:
        print(' Digite um número!')
        continue 

    if escolha == 6:
        print('Você saiu!')
        break
    
    elif escolha == 1:
        for livro in biblioteca:
            status = ' Disponível' if livro['disponivel'] else ' Emprestado' 
            print(f"Título: {livro['titulo']} | {status}")

    elif escolha == 2:
        titulo_digitado = input('Digite o titulo do livro desejado: ').strip() 
        livro_existe = False  
        for livro in biblioteca:
            if livro['titulo'].lower() == titulo_digitado.lower(): 
                livro_existe = True
                if not livro['disponivel']: 
                    print(' Esse livro já está emprestado!')
                else:
                    livro['disponivel'] = False
                    print(' Livro emprestado!')
                break
        if not livro_existe:
            print(' Livro inexistente!!')
    
    elif escolha == 3:
        titulo_digitado = input('Digite o titulo do livro a devolver: ').strip()
        livro_existe = False 
        for livro in biblioteca:
            if livro['titulo'].lower() == titulo_digitado.lower():
                livro_existe = True
                if livro['disponivel']:  
                    print(' Esse livro já está na biblioteca!')
                else:
                    livro['disponivel'] = True
                    print(' Livro devolvido!')
                break
        if not livro_existe:
            print(' Livro inexistente!!')
    
    elif escolha == 4:
        autor_buscado = input('Autor: ').strip()
        autor_encontrado = False  
        for livro in biblioteca:
            if livro['autor'].lower() == autor_buscado.lower():
                autor_encontrado = True
                status = ' Disponível' if livro['disponivel'] else ' Emprestado'
                print(f"Título: {livro['titulo']} | Ano: {livro['ano']} | {status}")
        if not autor_encontrado:
            print(' Autor inexistente na biblioteca!!')

    elif escolha == 5:
        print(f' Total de livros      = {len(biblioteca)}')
        print(f' Livros disponíveis   = {livro_disponivel()}')
        print(f' Livros emprestados   = {livros_emprestados()}')

    else:
        print(' Opção inválida! Digite de 1 a 6.') 