import os


print('Hello World')

def exibir_nome_do_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''') 
# aspas triplas quebra a linha

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' *(len(texto))
    print(linha)
    print (texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''docstring: Essa função é responsável por cadastrar um novo restaurante'''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    categoria_do_restaurante = input('Digite a categoria do restaurante que deseja cadastrar:')
    novo_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(novo_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')
    print(f"{'Nome do resturante: '.ljust(22)} | {'Categoria: '.ljust(20)} | Status: ")
    for restaurante in restaurantes:
        #operador ternário 
        ativo = 'Ativo' if restaurante['ativo'] else 'Desativado'
        print(f"- {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {ativo}")
    voltar_ao_menu_principal()

def ativar_restaurante():
    exibir_subtitulo('Alterando status restaurante')
    nome_restaurante_status = input('Digite o nome do restaurante que deseja cadastrar:')
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante_status:
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante_status} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante_status} foi desativado com sucesso'
            print(mensagem)
            return voltar_ao_menu_principal()
    print('Restaurante não encontrado.')
    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

# para verificar o tipo da variável
# print(opcao_escolhida == 1)
# print(type(opcao_escolhida))
# print(type(1))

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()


# Avisa ao "python" que assim que este programa ser executado, execute o método main
if __name__ == '__main__':
    main()







