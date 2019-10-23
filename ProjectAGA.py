from random import randint
import random

# @AUTHOR : KAIQUE MOREIRA , MATEUS PEREIRA


# BEM VINDO AO PROJETO AGA (PROJETO DE ARMAZENAMENTO, GERAÇÃO E AVALIAÇÃO DE QUESTÕES)

# ARMAZENAREMOS TODAS AS INFORMAÇÕES DOS USUÁRIOS CADASTRADOS ATRAVÉS DE UM DICIONÁRIO CHAMADO DE "BANCO"
banco = {}

# "MATERIA E PROF" SÃO BANCOS DE ARMAZENAMENTO DO MENU COORDENADOR, QUE RECEBERAM AS MATÉRIAS E PROFESSORES CADASTRADOS.
materia = []
prof = []

# BANCOS DE ARMAZENAMENTO DO CADASTRO DE QUESTÕES E PROVAS.
cadastrar = []
cadastro = 0
prova = 0
provas = []


# git
def coordenador():
    print('#############################################')
    print('#               COORDENADOR                 #')
    print('#############################################')

    print('#############################################')
    print('#         Escolha a opção desejada          #')
    print('#                                           #')
    print('# 1 - Cadastrar Disciplinas e Professores   #')
    print('# 2 - Listar Questões                       #')
    print('# 3 - Listar Disciplinas                    #')
    print('# 4 - Retornar ao Cadastramento             #')
    print('# 5 - Sair                                  #')
    print('#############################################\n')
    escolha = int(input(">>>: "))
    if escolha == 1:
        cadastrar_disciplina()
    elif escolha == 2:
        listar_questoes()
    elif escolha == 3:
        listar_disciplinas()
    elif escolha == 4:

        main()
    elif escolha == 5:
        sair()
    else:
        print('-----------------------------------------------------------------------------')
        print('ERRO: Opção Invalida tente novamente.')
        print('-----------------------------------------------------------------------------')


# FUNÇÃO CADASTRO DE DISCIPLINA, FUNÇÃO RESPONSAVÉL PELO CADASTRO DE DISCIPLINAS E PROFESSORES INFORMADO PELO USUÁRIO.
def cadastrar_disciplina():
    cont = int(input('Quantas Disciplinas deseja cadastrar ?:'))
    for item in range(cont):
        item += 1
        materias = input(f'Digite o nome da {item} disciplina:')
        profs = input(f'Digite nome do {item} professor Referente à Materia:')
        materia.append(materias)
        prof.append(profs)
    return coordenador()


# FUNÇÃO LISTAR D., QUANDO CHAMADA MOSTRARÁ AO USUÁRIO TODAS AS DISCIPLINAS CADASTRADAS NO BANCO "MATERIA".
def listar_disciplinas():
    for i, j in enumerate(materia):
        i += 1
        print(i, "-", j)
    return coordenador()


# FUNÇÃO LISTAR Q., FUNÇÃO RESPONSÁVEL POR MOSTRAR AO USUÁRIO AS QUESTÕES ARMAZENADAS NO BANCO "" PELA ORDEM DE
# CADASTRAMENTO.
def listar_questoes():
    for i, j in enumerate(cadastrar):
        i += 1
        print(i, "-", j)
    return coordenador()


# FUNÇÃO LISTAR P., FUNÇÃO QUE MOSTRARÁ AO USUÁRIO TODOS OS PROFESSORES ARMAZENADOS NO BANCO "PROF" EM ORDEM DE
# CADASTRAMENTO.
def listar_professor():
    for i, j in enumerate(prof):
        i += 1
        print(i, "-", j, "materia", materia)
    return coordenador()


# FUNÇÃO SAIR, FINALIZA O CÓDIGO.
def sair():
    print("Saindo...")
    exit()


# FUNÇÃO PROFESSOR, FUNÇÃO RESPONSÁVEL POR GERAR O MENU DO PROFESSOR E CHAMAR AS FUNCIONALIDADES SELECIONADAS.
def professor():
    print("##############################################")
    print("#                 PROFESSOR                  #")
    print("##############################################\n")

    print("##############################################")
    print("#          Escolha a opção desejada          #")
    print("#                                            #")
    print("# 1 - Cadastrar Questão                      #")
    print("# 2 - Minhas Questões                        #")
    print("# 3 - Gerar Exercício ou Prova               #")
    print("# 4 - Acessar provas anteriores e gabaritos  #")
    print("# 5 - Sair                                   #")
    print("# 6 - Retornar Cadastramento                 #")
    print("##############################################\n")
    escolha = int(input(">>>: "))
    if escolha == 1:
        cadastrar()
    elif escolha == 2:
        minhas_questoes()
    elif escolha == 3:
        prova_ou_exerc()
    elif escolha == 4:
        acessar_prova_ou_exercicio()
    elif escolha == 5:
        sair()
    elif escolha == 6:
        main()
    else:
        print("-----------------------------------------------------------------------------")
        print("ERRO: Opção invalida. Tente novamente.")
        print("-----------------------------------------------------------------------------")
        return professor()


'''FUNÇÃO CADASTRAR, FUNÇÃO RESPONSÁVEL POR SALVAR AS QUESTÕES QUE OS PROFESSORES ELABORARÉM, ELAS SERÃO SALVAS NO
 BANCO "CADASTRAR".'''


def cadastrar():
    cadastro1 = str(input('Digite sua questão:'))
    cadastro1 = cadastro1.upper()
    cadastrar.append(cadastro1)
    if cadastro1 in cadastrar:
        print('Questão cadastrada!')
        return professor()
    else:
        cadastrar.append(cadastro1)
        print('Questão cadastrada!')
        return professor()


# FUNÇÃO MINHAS QUESTÕES, FUNÇÃO QUE MOSTRARÁ AO USUÁRIO AS QUESTÕES SALVAS NO BANCO "CADASTRAR".
def minhas_questoes():
    print(f'Minhas Questões: {cadastrar}')
    return professor()


# FUNÇÃO PROVA OU EXERCICIO, GERA UM ARQUIVO DE TEXTO NO FORMATO .TXT COM O NÚMERO DE QUESTÕES DEFIDO PELO USUÁRIO.
def prova_ou_exerc():
    arquivo = open("Prova.", "w")
    arquivo.write(str(cadastrar))
    arquivo.close()
    provas.append(cadastrar)
    print("Gerando prova...")
    print("Arquivo Prova de formato.txt criado na pasta downloads")
    return professor()


# FUNÇÃO ACESSAR, MOSTRARÁ AO USUÁRIO AS PROVAS E GABARITOS JÁ TRABALHADOS.
def acessar_prova_ou_exercicio():
    for i in range(len(provas)):
        print("Provas: ", provas)
        return professor()


# CÓDIGO PRINCIPAL...
# O CÓDIGO PRINCIPAL TERÁ INICIO ATRAVÉS DO CADASTRAMENTO DOS USUÁRIOS PARA REALIZAÇÃO DO PRIMEIRO LOGIN.
def main():
    print("#############################################")
    print("#                                           #")
    print("#           WELCOME TO AGA PROJECT          #")
    print("#                                           #")
    print("#                 By: AGA                   #")
    print("#                                           #")
    print("#############################################\n")

    print("#############################################")
    print("#               CADASTRAMENTO               #")
    print("#############################################")

    # AS INFORMAÇÕES QUE PEDIREMOS SERAM OBRIGATÓRIAS NO CADASTRO, ESTAS INFORMAÇÕES SÃO: PRIMEIRO NOME, SOBRENOME,
    # NOME DO LOGIN DE ACESSO, QUE O MESMO SERÁ A CHAVE DE ACESSO AS SUAS INFORMAÇÕES.
    nome = str(input("Nome: "))
    while len(nome) < 4 or len(nome) > 15:
        print("-----------------------------------------------------------------------------")
        print("ERRO: O seu nome deve estar no intervado de 4 á 15 digitos.")
        print("-----------------------------------------------------------------------------")
        nome = str(input("Digite novamente o seu Nome: "))

    sobrenome = str(input("Sobrenome: "))
    while len(sobrenome) < 4 or len(sobrenome) > 15:
        print("-----------------------------------------------------------------------------")
        print("ERRO: O seu sobrenome deve estar no intervado de 4 á 15 digitos.")
        print("-----------------------------------------------------------------------------")
        sobrenome = str(input("Digite novamente o seu Sobrenome: "))

    login = input("nome do Usuário: ")
    while len(login) < 2 or len(login) > 30:
        print("-----------------------------------------------------------------------------")
        print("ERRO: O seu login deve estar no intervado de 2 á 30 digitos.")
        print("-----------------------------------------------------------------------------")
        login = input("Digite novamente o Nome de Usuário: ")
    print("#############################################")

    # EM SEGUIDA ASSIM QUE TODAS AS DEVIDAS INFORMAÇÕES FORÉM INFORMADAS O PROGRAMA IRÁ GERAR UMA SENHA PARA O USUÁRIO.
    senha = random.randint(10000000, 99999999)
    print("\nGerando senha...")
    print("A senha Gerada foi: ", senha)
    banco[login] = [nome, sobrenome, senha]
    print("\n#############################################")

    print("\nDados Cadastrados com Sucesso.\n")

    # ASSIM QUE A SENHA FOR GERADA APARECERÁ UMA MENSAGEM PERGUNTANDO SE O USUÁRIO DESEJA OU NÃO VER SUAS INFORMAÇÕES.
    alternativa = input("Deseja visualizar seus dados cadastrados? ('S' ou 'N'): ").upper()
    if alternativa == 'S':
        print('#############################################')
        print('#              Dados Cadastrados            #')
        print(f"nome: {nome}")
        print(f"sobrenome: {sobrenome}")
        print(f"nome de usuário: {login} ")
        print(f"Sua senha de login será: {senha} ")
        print("#############################################")
    elif alternativa == 'N':
        print('Obrigado por efetuar seu cadastramento. Aproveite nossa ferramenta de trabalho.')
    else:
        print('-----------------------------------------------------------------------------')
        print('ERRO: O Caractere informado é inválido.')
        print('-----------------------------------------------------------------------------')

    '''ASSIM QUE TODAS AS INFORMAÇÕES FORÉM CADASTRADAS, O ACESSO LOGIN SERÁ DISPONIBILIZADO, PARA EFETUARMOS 
    O PRIMEIRO ACESSO
    SERÁ SOLICITADO O LOGIN(NOME DE USUÁRIO) E A SENHA. EM SEGUIDA,
    O USUÁRIO DEVE INFORMAR O CARGO QUE ELE ATUA (PROFESSOR
    OU COORDENADOR) APARTIR DAI GERANDO CADA MENU E FUNCIONALIDADE ESPECIFICA DOS USUÁRIO.'''
    while True:
        Busca_Login = input("login: ")
        Busca_Senha = int(input("senha: "))
        if Busca_Login in banco.keys():
            if Busca_Senha in banco[Busca_Login]:
                alternativa = input("Informe o Cargo que você exerce? ('P' professor ou 'C' Coordenador)\n").upper()
                if alternativa == 'P':
                    professor()
                elif alternativa == 'C':
                    coordenador()
                else:
                    print('-----------------------------------------------------------------------------')
                    print('ERRO: Está opção não existe. Tente novamente')
                    print('-----------------------------------------------------------------------------')
            else:
                print('-----------------------------------------------------------------------------')
                print('ERRO: Usuário ou senha incorreto. Tente novamente')
                print('-----------------------------------------------------------------------------')
        else:
            print('-----------------------------------------------------------------------------')
            print('ERRO: Usuário ou senha incorreto. Tente novamente')
            print('-----------------------------------------------------------------------------')


main()
