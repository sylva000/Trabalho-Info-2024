def cadastrar_pessoa():
   
    cadastros = []

    while True:
     
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        email = input("Digite o email: ")
        cidade = input("Digite a cidade: ")

       
        pessoa = {
            'Nome': nome,
            'Idade': idade,
            'Email': email,
            'Cidade': cidade
        }

       
        cadastros.append(pessoa)

        
        continuar = input("Deseja cadastrar outra pessoa? (s/n): ")
        if continuar.lower() != 's':
            break

    return cadastros


cadastros = cadastrar_pessoa()
print("\nCadastros realizados:")
for pessoa in cadastros:
    print(pessoa)
