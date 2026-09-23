import os
import time
import json
from datetime import datetime

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

def salvar_emprestimos():
    with open("dados/emprestimos.json", "w") as arquivo:
        json.dump(emprestimos, arquivo, indent=4)

def salvar_historico():
    with open("dados/historico.json", "w") as arquivo:
        json.dump(historico, arquivo, indent=4)

def salvar_dispositivos():
    with open("dados/dispositivos.json", "w") as arquivo:
        json.dump(dispositivos, arquivo, indent=4)

def emprestar_dispositivo():
    while True:
        os.system("cls")
        cabeçalho("EMPRESTAR DISPOSITIVOS")
        for numero, professor in professores.items():
            print(f"{numero} - {professor}")
        print("[0] Voltar ao menu\n")
        professor_selecionado = input("Selecione o ID do professor que vai utilizar o dispositivo: ")
        if professor_selecionado == "0":
            return
        if professor_selecionado not in professores:
            print("Este professor não existe!")
            time.sleep(2)
            continue
        os.system("cls")
        cabeçalho("EMPRESTAR DISPOSITIVOS")
        print("Você selecionou o(a) professor(a):", professores[professor_selecionado])
        print()
        for item, dados_dispositivo in dispositivos.items():
            print(f"ID: {item}\n"f"Dispositivo: {dados_dispositivo['nome']}\n"f"Disponíveis: {dados_dispositivo['utilizaveis']}\n")
        print("[0] Voltar ao menu\n")
        dispositivo_selecionado = input("Selecione o ID do dispositivo que será emprestado: ")
        if dispositivo_selecionado == "0":
            return
        if dispositivo_selecionado not in dispositivos:
            print("Este dispositivo não existe!")
            time.sleep(2)
            continue
        if dispositivos[dispositivo_selecionado]["utilizaveis"] == 0:
            print("Não existem dispositivos disponíveis para empréstimo!")
            time.sleep(2)
            continue
        try:
            quantidade_selecionada = int(input("Digite a quantidade que o professor vai utilizar: "))
        except ValueError:
            print("Digite um valor válido!!")
            time.sleep(2)
            continue
        if quantidade_selecionada == 0:
            return
        if quantidade_selecionada < 0:
            print("Quantidade inválida, tente novamente!")
            time.sleep(2)
            continue
        if quantidade_selecionada > dispositivos[dispositivo_selecionado]["utilizaveis"]:
            print("Quantidade inválida, tente novamente!")
            time.sleep(2)
            continue
        maior_numero = 0

        for emprestimo in emprestimos:
            if emprestimo["id"] > maior_numero:
                maior_numero = emprestimo["id"]

        for registro in historico:
            if registro["id_emprestimo"] > maior_numero:
                maior_numero = registro["id_emprestimo"]

        id_emprestimo = maior_numero + 1
        data_hora = datetime.now().strftime("%d/%m/%y - %H:%M:%S")
        novo_emprestimo = {
            "id": id_emprestimo,
            "professor_id": professor_selecionado,
            "professor": professores[professor_selecionado],
            "dispositivo_id": dispositivo_selecionado,
            "dispositivo": dispositivos[dispositivo_selecionado]["nome"],
            "quantidade": quantidade_selecionada,
            "data": data_hora
        }
        emprestimos.append(novo_emprestimo)
        dispositivos[dispositivo_selecionado]["utilizaveis"] -= quantidade_selecionada
        salvar_emprestimos()
        salvar_dispositivos()
        print("Empréstimo realizado com sucesso!")
        time.sleep(2)
        return

def ver_emprestimos():
    os.system("cls")
    cabeçalho("DISPOSITIVOS EM USO")
    if not emprestimos:
        print("\nNão existem dispositivos em uso.")
        input("\nAperte Enter para voltar ao menu...")
        return
    print()
    for emprestimo in emprestimos:
        print(
            f"ID do empréstimo: {emprestimo['id']}\n"
            f"Professor: {emprestimo['professor']}\n"
            f"Dispositivo: {emprestimo['dispositivo']}\n"
            f"Quantidade: {emprestimo['quantidade']}\n"
            f"Data: {emprestimo['data']}\n"
        )
    input("Aperte Enter para voltar ao menu...")

def devolver_dispositivo():
    while True:
        os.system("cls")
        cabeçalho("DEVOLUÇÃO DE DISPOSITIVO")
        if not emprestimos:
            print("\nNão existem dispositivos em uso.")
            time.sleep(2)
            return
        for emprestimo in emprestimos:
            print(
                f"ID: {emprestimo['id']}\n"
                f"Professor: {emprestimo['professor']}\n"
                f"Dispositivo: {emprestimo['dispositivo']}\n"
                f"Quantidade: {emprestimo['quantidade']}\n"
            )
        print("[0] Voltar ao menu\n")
        try:
            id_selecionado = int(input("Digite o ID do empréstimo que deseja devolver: "))
        except ValueError:
            print("Digite um valor válido!!")
            time.sleep(2)
            continue
        if id_selecionado == 0:
            return
        emprestimo_selecionado = None
        for emprestimo in emprestimos:
            if emprestimo["id"] == id_selecionado:
                emprestimo_selecionado = emprestimo
                break
        if emprestimo_selecionado is None:
            print("Este empréstimo não existe!")
            time.sleep(2)
            continue
        try:
            quantidade_devolvida = int(input("Digite a quantidade que será devolvida: "))
        except ValueError:
            print("Digite um valor válido!!")
            time.sleep(2)
            continue
        if quantidade_devolvida <= 0:
            print("Quantidade inválida, tente novamente!")
            time.sleep(2)
            continue
        if quantidade_devolvida > emprestimo_selecionado["quantidade"]:
            print("A quantidade devolvida é maior que a quantidade emprestada!")
            time.sleep(2)
            continue
        dispositivos[emprestimo_selecionado["dispositivo_id"]]["utilizaveis"] += quantidade_devolvida
        data_hora = datetime.now().strftime("%d/%m/%y - %H:%M:%S")
        registro_historico = {
            "id_emprestimo": emprestimo_selecionado["id"],
            "professor_id": emprestimo_selecionado["professor_id"],
            "professor": emprestimo_selecionado["professor"],
            "dispositivo_id": emprestimo_selecionado["dispositivo_id"],
            "dispositivo": emprestimo_selecionado["dispositivo"],
            "quantidade": quantidade_devolvida,
            "data_emprestimo": emprestimo_selecionado["data"],
            "data_devolucao": data_hora
        }
        historico.append(registro_historico)
        emprestimo_selecionado["quantidade"] -= quantidade_devolvida
        if emprestimo_selecionado["quantidade"] == 0:
            emprestimos.remove(emprestimo_selecionado)
        salvar_emprestimos()
        salvar_historico()
        salvar_dispositivos()
        print("Devolução realizada com sucesso!")
        time.sleep(2)
        return

def ver_historico():
    os.system("cls")
    cabeçalho("HISTÓRICO DE EMPRÉSTIMOS")
    if not historico:
        print("\nO histórico está vazio.")
        input("\nAperte Enter para voltar ao menu...")
        return
    print()
    for registro in historico:
        print(
            f"ID do empréstimo: {registro['id_emprestimo']}\n"
            f"Professor: {registro['professor']}\n"
            f"Dispositivo: {registro['dispositivo']}\n"
            f"Quantidade devolvida: {registro['quantidade']}\n"
            f"Data do empréstimo: {registro['data_emprestimo']}\n"
            f"Data da devolução: {registro['data_devolucao']}\n"
        )
    input("Aperte Enter para voltar ao menu...")

def limpar_historico():
    os.system("cls")
    cabeçalho("LIMPAR HISTÓRICO")
    if not historico:
        print("\nO histórico já está vazio.")
        time.sleep(2)
        return
    confirmacao = input("\nTem certeza que deseja limpar o histórico? [S/N]: ")
    if confirmacao.lower() != "s":
        return
    historico.clear()
    salvar_historico()
    print("Histórico limpo com sucesso!")
    time.sleep(2)

def emprestimos_menu():
    while True:
        os.system("cls")
        cabeçalho("MENU EMPRÉSTIMOS")
        print("\n[1] Emprestar dispositivo")
        print("[2] Ver dispositivos em uso")
        print("[3] Devolução de dispositivo")
        print("[4] Histórico de empréstimos")
        print("[5] Limpar histórico")
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
            ver_emprestimos()
        elif opcao_emprestimo == 3:
            devolver_dispositivo()
        elif opcao_emprestimo == 4:
            ver_historico()
        elif opcao_emprestimo == 5:
            limpar_historico()
        else:
            print("Digite uma opção válida!")
            time.sleep(2)
            continue
