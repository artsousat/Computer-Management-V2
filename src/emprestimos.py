import os
import time
import json

from src.professores import professores
from src.utils import cabeçalho
from src.dispositivos import dispositivos

emprestimos = []
historico = []

def carregar_emprestimos():
    try:
        with open("dados/emprestimos.json", "r") as arquivo:
            dados_emprestimos = json.load(arquivo)
            return dados_emprestimos
    except FileNotFoundError:
        with open("dados/emprestimos.json", "w") as arquivo:
            json.dump(emprestimos, arquivo, indent=4)
            return emprestimos
emprestimos = carregar_emprestimos()

def carregar_historico():
    try:
        with open("dados/historico.json", "r") as arquivo:
            dados_historico = json.load(arquivo)
            return dados_historico
    except FileNotFoundError:
        with open("dados/historico.json", "w") as arquivo:
            json.dump(historico, arquivo, indent=4)
            return historico
historico = carregar_historico()

def emprestar_dispositivo():
    while True:
        os.system("cls")
        cabeçalho("EMPRESTAR DISPOSITIVOS")
        for numero, professor in professores.items():
            print(f"{numero} - {professor}")
        print("[0] Voltar ao menu\n")
        professor_selecionado = input("Selecione o ID do professor que gostaria de emprestar o dispositivo: ")
        if professor_selecionado == "0":
            return
        if professor_selecionado not in professores:
            print("Este professor não existe!")
            time.sleep(2)
            continue
        os.system("cls")
        print("Você selecionou o(a) professor(a):",professores[professor_selecionado])
        for item, dados_dispositivo in dispositivos.items():
            print(f"ID: {item}\n"f"Dispositivo: {dados_dispositivo['nome']}\n")
        dispositivo_selecionado = input("Selecione o ID do dispositivo que gostaria de emprestar o dispositivo: ")
        if dispositivo_selecionado == "0":
            return
        if dispositivo_selecionado not in dispositivos:
            print("Este dispositivo não existe!")
            time.sleep(2)
            continue
        try:
            quantidade_selecionado = int(input("Digite a quantidade que o professor vai utilizar: "))
        except ValueError:
            print("Digite um valor válido!!")
            time.sleep(2)
            continue
        if quantidade_selecionado == 0:
            return
        if quantidade_selecionado > dispositivos[dispositivo_selecionado]["utilizaveis"]:
            print("Quantidade inválida, tente novamente!")
            time.sleep(2)
            continue
        if emprestimos:
            id_emprestimos = len(max(emprestimos))+1
        else:
            id_emprestimos = 1  
        novo_emprestimo = {
            "professor": professores[professor_selecionado],
            "dispositivo": dispositivos[dispositivo_selecionado]["nome"],
            "quantidade": quantidade_selecionado
        }

        

def emprestimos_menu():
    while True:
        os.system("cls")
        cabeçalho("MENU EMPRÉSTIMOS")
        print("\n[1] Emprestar Dispositivo")
        print("[2] Ver dispositivos em uso")
        print("[3] Devolução de Dispositivo")
        print("[4] Histórico de Empréstimos")
        print("[5] Limpar histórico do dia")
        print("[0] Voltar ao menu")
        try:
            opcao_emprestimo = int(input("\nDigite a opção desejada: "))
        except ValueError:
            print("Digite um valor válido!!")
            time.sleep(2)
            continue
        if opcao_emprestimo == 0:
            return
        elif opcao_emprestimo == 1:
            emprestar_dispositivo()
        elif opcao_emprestimo == 2:
            pass
        elif opcao_emprestimo == 3:
            pass
        elif opcao_emprestimo == 4:
            pass
        elif opcao_emprestimo == 5:
            pass
        else:
            print("Digite uma opção Válida!")
            time.sleep(2)
            continue