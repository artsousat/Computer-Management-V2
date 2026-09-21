import os
import time
import json

from src.utils import cabeçalho

professores = {
    "1": "Leni",
    "2": "Flavia",
    "3": "Carol",
    "4": "Karine",
    "5": "Josi",
    "6": "Jussara",
    "7": "Michele",
    "8": "Dalva",
    "9": "Tatiana",
    "10": "Patricia",
    "11": "Jucelia",
    "12": "Andressa",
    "13": "Angela",
    "14": "Magali",
    "15": "Vida"
    }

def carregar_professores():
    try:
        with open("dados/professores.json", "r") as arquivo:
            dados_professores = json.load(arquivo)
            return dados_professores
    except FileNotFoundError:
        with open("dados/professores.json", "w") as arquivo:
            json.dump(professores, arquivo, indent=4)
            return professores
professores = carregar_professores()

def cadastro_professor():
    os.system("cls")
    cabeçalho("CADASTRO DE PROFESSORES")
    print("[0] Voltar ao menu\n")
    novo_professor = input("\nDigite o nome do professor que deseja cadastrar: ")
    if novo_professor == "0":
        return
    if novo_professor == "":
        print("Digite um nome válido!")
        time.sleep(2)
        return
    maior_numero = 0
    for item in professores:
        item_inteiro = int(item)
        if item_inteiro > maior_numero:
            maior_numero = item_inteiro
    numero = maior_numero + 1
    numero_str = str(numero)
    professores[numero_str] = novo_professor
    with open("dados/professores.json", "w") as arquivo:
        json.dump(professores, arquivo, indent=4)
        print("Professor", novo_professor, "cadastrado com sucesso!")
        time.sleep(2)
        return

def ver_professor():
    os.system("cls")
    cabeçalho("PROFESSORES CADASTRADOS")
    print()
    for numero, professor in professores.items():
        print(f"{numero} - {professor}")
    input("\nAperte Enter para voltar ao menu principal...")
    return

def remover_professor():
    while True:
        os.system("cls")
        cabeçalho("REMOVER PROFESSOR")
        for numero, professor in professores.items():
            print(f"{numero} - {professor}")
        print("[0] Voltar ao menu\n")
        selecionado = input("Digite o número do professor que gostaria de remover: ")
        if selecionado == "0":
            return
        if selecionado not in professores:
            print("Este professor não existe!")
            time.sleep(2)
            continue
        del professores[selecionado]
        with open("dados/professores.json", "w") as arquivo:
            json.dump(professores, arquivo, indent=4)
        print("Professor removido com sucesso!")
        time.sleep(2)
        return

def professores_menu():
    while True:
        os.system("cls")
        cabeçalho("MENU PROFESSORES")
        print("\n[1] Cadastrar Professor")
        print("[2] Ver professores cadastrados")
        print("[3] Remover professor")
        print("[0] Voltar ao menu")
        try:
            opcao_professor = int(input("\nDigite a opção desejada: "))
        except ValueError:
            print("Digite um valor válido!!")
            time.sleep(2)
            continue
        if opcao_professor == 0:
            return
        elif opcao_professor == 1:
            cadastro_professor()
        elif opcao_professor == 2:
            ver_professor()
        elif opcao_professor == 3:
            remover_professor()
        else:
            print("Digite uma opção válida!")
            time.sleep(2)
            continue
