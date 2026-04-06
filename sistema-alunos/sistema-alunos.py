
alunos = []

while True:
    print('\n-----SELECIONE UMA OPÇÃO-----')
    print(' 1 - Cadastrar novo aluno')
    print(' 2 - Listar todos os alunos com média e situação')
    print(' 3 - Buscar aluno pelo nome')
    print(' 4 - Sair')

    try:
        opcao = int(input('Opção: '))
    except ValueError:
        print('Digite um número válido.')
        continue

    if opcao == 4:
        print('Você saiu!')
        break

    elif opcao == 1:
        nome = input('Nome: ').strip()

        try:
            idade = int(input('Idade: '))
        except ValueError:
            print('Idade inválida! Cadastro cancelado.')
            continue

        notas = []
        valido = True
        for i in range(1, 4):
            try:
                n = float(input(f'Nota {i}: '))
                if n < 0 or n > 10:
                    print('Nota inválida! Digite um valor entre 0 e 10.')
                    valido = False
                    break
                notas.append(n)
            except ValueError:
                print('Nota inválida! Digite um número.')
                valido = False
                break

        if valido:
            aluno = {'nome': nome, 'idade': idade, 'notas': notas}
            alunos.append(aluno)
            print(f'{nome} cadastrado com sucesso!')

    elif opcao == 2:
        if len(alunos) == 0:
            print('Nenhum aluno cadastrado!')
        else:
            print('\n--- LISTA DE ALUNOS ---')
            for aluno in alunos:
                media = sum(aluno['notas']) / len(aluno['notas'])
                situacao = 'APROVADO ✓' if media >= 7.0 else 'REPROVADO ✗'
                print(f'{aluno["nome"]} | Idade: {aluno["idade"]} | Média: {media:.2f} | {situacao}')

    elif opcao == 3:
        busca = input('Digite o nome do aluno: ').strip().lower()
        encontrado = False
        for aluno in alunos:
            if busca in aluno['nome'].lower():
                media = sum(aluno['notas']) / len(aluno['notas'])
                situacao = 'APROVADO ✓' if media >= 7.0 else 'REPROVADO ✗'
                print(f'\nAluno encontrado!')
                print(f'Nome: {aluno["nome"]}')
                print(f'Idade: {aluno["idade"]}')
                print(f'Notas: {aluno["notas"]}')
                print(f'Média: {media:.2f} | {situacao}')
                encontrado = True
                break
        if not encontrado:
            print('Aluno não encontrado!')

    else:
        print('Opção inválida! Escolha entre 1 e 4.')
    

