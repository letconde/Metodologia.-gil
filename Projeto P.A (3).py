""" 
            #-----Trabalho de P.A - Metodologia Ágil-----#

Por: 
- Julia Bellini Sorrente (Scrum Master)
- Gabriel Cesar Rodrigues
- Ingrid Cavalli da Silva
- Letycia Conde da Cruz
- Riad Abbes Bernade

"O objetivo desta tarefa é o desenvolvimento de um projeto, 
em equipe, de implementação das operações de CRUD (Inserir, Exibir, Atualizar e Excluir) 
em Python utilizando apenas elementos nativos em modo console.

Cada equipe deverá implementar as operações utilizando listas ou matrizes, 
definindo um menu de ações para a execução."

                       #-----Projeto-----#
Nosso projeto consiste em uma programa de cadastro de animais que pode
ser utilizado em ONG's, veterinários e petshop's.
"""

                       #-------CÓDIGO-------#
cadastro = []

#-------Funções para Alterações de Dados-------#
def pede_nome():
    return input("Nome do animal: ")
def pede_especie():
    return input("Espécie (Gato, Cachorro...): ")
def pede_raca():
    return input("Qual a raça do animal?: ")
def pede_sexo():
    return input("Sexo do animal (M ou F): ")
def pede_peso():
    return int(input("Peso (em Kg): "))
def pede_idade():
    return int(input("Idade estimada (em anos): "))
def pede_vacina():
    return input("Já tomou alguma vacina? (S ou N): ")

#-------Função de Lista Médica do Animal-------#
def Lista():
    global cadastro
    nome = pede_nome()
    especie = pede_especie()
    raca = pede_raca()
    sexo = pede_sexo()
    peso = pede_peso()
    idade = pede_idade()
    vacina = pede_vacina()
    cadastro.append([nome, especie, raca, sexo, peso, idade, vacina])
    print ("\n----------")

#-------Enumerar os Cadastros-------#
    for posição, e in enumerate(cadastro):
        print(f"Posição:  {posição}", end="")
        mostra_dados(e[0], e[1], e[2], e[3], e[4], e[5], e[6])

#-------Função para Mostrar os Dados-------#
def mostra_dados(nome, especie, raca, sexo, peso, idade, vacina):
    print(f"\n Nome: {nome}, \n Espécie (Gato, Cachorro...): {especie}, \n Raça: {raca}, \n Sexo do animal (M ou F): {sexo}, \n Peso (em Kg): {peso}, \n Idade estimada (em anos): {idade}, \n Já tomou alguma vacina?: {vacina}")

#-------Função para verificação do Nome (Começar com letra Maiúscula ou não)-------#
def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(cadastro):
        if e[0].lower() == mnome:
            return p
    return None

#-------Função para Apagar um Dado-------#
def Apaga():
    global cadastro
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        del cadastro[p]
    else:
        print("Não encontrado.")

#-------Função para Alterar um Dado-------#
def Alterar():
    p = pesquisa(pede_nome())
    if p is not None:
        nome = cadastro[p][0]
        especie = cadastro[p][1]
        raca = cadastro[p][2]
        sexo = cadastro[p][3]
        peso = cadastro[p][4]
        idade = cadastro[p][5]
        vacina = cadastro[p][6]
        print("Cadastro Encontrado! \n")
        mostra_dados(nome, especie, raca, sexo, peso, idade, vacina)
        nome = pede_nome()
        especie = pede_especie()
        raca = pede_raca()
        sexo = pede_sexo()
        peso = pede_peso()
        idade = pede_idade()
        vacina = pede_vacina()
        cadastro[p] = [nome, especie, raca, sexo, peso, idade, vacina]
    else:
        print("Não Encontrado.")

#-------Função de Validação de Dados-------#
def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

#-------Função para Listar o Menu-------#
def Menu():
    print("""
    1 - Novo Cadastro
    2 - Alterar
    3 - Apagar
    4 - Lista

    0 - Sair
    """)
    print(f"\nLista de animais: {len(cadastro)}\n")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 5)

#-------Opções de Escolha do Usuário-------#
while True:
    sn1 = Menu()
    if sn1 == 0:
        print("Programa encerrado.")
        break
    elif sn1 == 1:
        Lista()
    elif sn1 == 2:
        Alterar()
    elif sn1 == 3:
        Apaga()
    elif sn1 == 4:
        mostra_dados()
    else:
        print("Opção inválida.")
