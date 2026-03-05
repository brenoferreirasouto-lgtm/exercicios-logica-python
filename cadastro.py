'''
■ Exercício 17 - Cadastro com Validação
Enunciado:
Faça um cadastro que valide:
- Nome: mínimo 3 caracteres
- Idade: entre 18 e 120 anos
- Email: deve conter "@"
'''
while True: 
    nome = str(input('Digite seu nome: ')).strip()
    if len(nome) >= 3 :
        break
    print('Nome muito curto! Mínimo 3 letras.')

while True: 
    try:
        idade = int(input('Digite sua idade: '))
        if idade >= 18 and idade <= 120 :
            break
        print('Idade deve estar entre 18 e 120')
    except: print('Digite apenas números')

while True:
    email = input('Email: ').strip()
    if '@' in email and len(email) >= 5: 
        break
    print('Email inválido! Deve conter @')

print('=== CADASTRO CONCLUÍDO ===')
print(f'Nome: {nome}')
print(f'Idade: {idade} anos')
print(f'Email: {email}')
