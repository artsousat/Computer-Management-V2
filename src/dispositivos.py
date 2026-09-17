import os
import time
import json

from src.utils import cabeçalho

dispositivos = {
    "1": {"nome": "Chromebook", "estoque": 40, "quebrados": 1, "sumido": 1, "utilizaveis": 0},
    "2": {"nome": "Positivo", "estoque": 59, "quebrados": 0, "sumido": 0, "utilizaveis": 0},
    "3": {"nome": "Tablets", "estoque": 50, "quebrados": 0, "sumido": 0, "utilizaveis": 0},
    "4": {"nome": "Multilaser", "estoque": 10, "quebrados": 0, "sumido": 0, "utilizaveis": 0},
    "5": {"nome": "Positivo DS", "estoque": 15, "quebrados": 0, "sumido": 0, "utilizaveis": 0},
}

def carregar_dispositivos():
    try:
        with open("dados/dispositivos.json", "r") as arquivo:
            dados_dispositivos = json.load(arquivo)
            for item, dados_dispositivo in dados_dispositivos.items():
                utilizaveis = (dados_dispositivo["estoque"] - dados_dispositivo["quebrados"] - dados_dispositivo["sumido"])
                dados_dispositivo["utilizaveis"] = utilizaveis
        with open("dados/dispositivos.json", "w") as arquivo:
            json.dump(dados_dispositivos, arquivo, indent=4)
            return dados_dispositivos
    except FileNotFoundError:
        with open("dados/dispositivos.json", "w") as arquivo:
            json.dump(dispositivos, arquivo, indent=4)
            return dispositivos
dispositivos = carregar_dispositivos()

def cadastrar_dispositivo():
    while True:
        os.system("cls")
        cabeçalho("CADASTRO DISPOSITIVO")
        print("[0] Voltar ao menu\n")
        novo_dispositivo = input("Digite o dispositivo que gostaria de cadastrar: ")
        if novo_dispositivo == "0":
            return
        try:
            quantidade_dispositivo = int(input("Digite a quantidade que gostaria de cadastrar: "))
        except ValueError:
            print("Insira um número válido!")
            time.sleep(2)
            continue
        if quantidade_dispositivo == 0:
            return
        if quantidade_dispositivo < 0:
            print("Quantidade inválida, tente novamente!")
            time.sleep(2)
            continue
        maior_numero = 0
        for item in dispositivos:
            item_inteiro = int(item)
            if item_inteiro > maior_numero:
                maior_numero = item_inteiro
        numero = maior_numero + 1
        numero_str = str(numero)
        dispositivos[numero_str] = {"nome": novo_dispositivo,"estoque": quantidade_dispositivo,"quebrados": 0,"sumido": 0,"utilizaveis": quantidade_dispositivo}
        with open("dados/dispositivos.json", "w") as arquivo:
            json.dump(dispositivos, arquivo, indent=4)

            print("Dispositivo", novo_dispositivo, "cadastrado com sucesso!")
            time.sleep(2)

            return

def remover_dispositivo():
    while True:
        os.system("cls")
        cabeçalho("REMOVER DISPOSITIVO")
        for item, dados_dispositivo in dispositivos.items():
            print(f"ID: {item}\n"f"Dispositivo: {dados_dispositivo['nome']}\n"f"Estoque: {dados_dispositivo['estoque']}\n")
        print("[0] Voltar ao menu\n")
        selecionado = input("Digite o id do dispositivo que gostaria de remover: ")
        if selecionado == "0":
            return
        if selecionado not in dispositivos:
            print("Este dispositivo não existe!")
            time.sleep(2)
            continue
        del dispositivos[selecionado]
        with open("dados/dispositivos.json", "w") as arquivo:
            json.dump(dispositivos, arquivo, indent=4)
        print("Dispositivo removido com sucesso!")
        time.sleep(2)
        return

def ver_dispositivo():
    os.system("cls")
    print("DISPOSITIVOS CADASTRADOS:\n")

    for item, dados_dispositivo in dispositivos.items():
        print(
            f"ID: {item}\n"
            f"Dispositivo: {dados_dispositivo['nome']}\n"
            f"Estoque: {dados_dispositivo['estoque']}\n"
        )

    input("\nAperte Enter para voltar ao menu principal...")

def estoque_dispositivo():
    os.system("cls")
    print("ESTOQUE DISPOSITIVO:\n")

    for item, dados_dispositivo in dispositivos.items():
        print(
            f"ID: {item}\n"
            f"Dispositivo: {dados_dispositivo['nome']}\n"
            f"Estoque: {dados_dispositivo['estoque']}\n"
            f"Disponíveis: {dados_dispositivo['utilizaveis']}\n"
            f"Quebrados: {dados_dispositivo['quebrados']}\n"
            f"Desaparecidos: {dados_dispositivo['sumido']}\n"
        )

    input("\nAperte Enter para voltar ao menu principal...")

def registrar_ocorrencia():
    while True:
        os.system("cls")
        cabeçalho("REGISTRAR OCORRÊNCIA")
        print("\n[1] Registrar dispositivo quebrado")
        print("[2] Registrar dispositivo desaparecido")
        print("[3] Registrar dispositivo consertado")
        print("[4] Registrar dispositivo encontrado")
        print("[0] Voltar ao menu")
        try:
            opcao_ocorrencia = int(input("\nSelecione a opção desejada: "))
        except ValueError:
            print("Digite um valor válido!!")
            time.sleep(2)
            continue
        if opcao_ocorrencia == 0:
            return
        elif opcao_ocorrencia == 1:
            os.system("cls")
            for item, dados_dispositivo in dispositivos.items():
                print(f"ID: {item}\n"f"Dispositivo: {dados_dispositivo['nome']}\n")
            selecao = input("Digite o ID do dispositivo que gostaria de registrar como quebrado: ")
            if selecao not in dispositivos:
                print("Este dispositivo não existe!")
                time.sleep(2)
                continue
            try:
                selecao_quebrado = int(input("Digite a quantidade que quebrou: "))
            except ValueError:
                print("Digite um valor válido!!")
                time.sleep(2)
                continue
            if selecao_quebrado <= 0:
                print("Quantidade inválida, tente novamente!")
                time.sleep(2)
                continue
            if dispositivos[selecao]["utilizaveis"] < selecao_quebrado:
                print("Quantidade inválida, tente novamente!")
                time.sleep(2)
                continue
            quebrado_novo = (dispositivos[selecao]["quebrados"] + selecao_quebrado)
            utilizavel_novo = (dispositivos[selecao]["utilizaveis"] - selecao_quebrado)
            dispositivos[selecao]["quebrados"] = quebrado_novo
            dispositivos[selecao]["utilizaveis"] = utilizavel_novo
            with open("dados/dispositivos.json", "w") as arquivo:
                json.dump(dispositivos, arquivo, indent=4)
                print("Ocorrência concluída!")
                time.sleep(2)
                return
        elif opcao_ocorrencia == 2:
            os.system("cls")
            for item, dados_dispositivo in dispositivos.items():
                print(f"ID: {item}\n"f"Dispositivo: {dados_dispositivo['nome']}\n")
            selecao = input("Digite o ID do dispositivo que gostaria de registrar como desaparecido: ")
            if selecao not in dispositivos:
                print("Este dispositivo não existe!")
                time.sleep(2)
                continue
            try:
                selecao_desaparecida = int(input("Digite a quantidade que desapareceu: "))
            except ValueError:
                print("Digite um valor válido!!")
                time.sleep(2)
                continue
            if selecao_desaparecida <= 0:
                print("Quantidade inválida, tente novamente!")
                time.sleep(2)
                continue
            if dispositivos[selecao]["utilizaveis"] < selecao_desaparecida:
                print("Quantidade inválida, tente novamente!")
                time.sleep(2)
                continue
            desaparecido_novo = (dispositivos[selecao]["sumido"] + selecao_desaparecida)
            utilizavel_novo = (dispositivos[selecao]["utilizaveis"] - selecao_desaparecida)
            dispositivos[selecao]["sumido"] = desaparecido_novo
            dispositivos[selecao]["utilizaveis"] = utilizavel_novo
            with open("dados/dispositivos.json", "w") as arquivo:
                json.dump(dispositivos, arquivo, indent=4)
                print("Ocorrência concluída!")
                time.sleep(2)
                return
        elif opcao_ocorrencia == 3:
            os.system("cls")
            for item, dados_dispositivo in dispositivos.items():
                print(f"ID: {item}\n"f"Dispositivo: {dados_dispositivo['nome']}\n")
            selecao = input("Digite o ID do dispositivo que gostaria de registrar como consertado: ")
            if selecao not in dispositivos:
                print("Este dispositivo não existe!")
                time.sleep(2)
                continue
            try:
                selecao_consertado = int(input("Digite a quantidade que consertou: "))
            except ValueError:
                print("Digite um valor válido!!")
                time.sleep(2)
                continue
            if selecao_consertado <= 0:
                print("Quantidade inválida, tente novamente!")
                time.sleep(2)
                continue
            if selecao_consertado > dispositivos[selecao]["quebrados"]:
                print("Quantidade inválida, tente novamente!")
                time.sleep(2)
                continue
            consertado_novo = (dispositivos[selecao]["quebrados"] - selecao_consertado)
            utilizavel_novo = (dispositivos[selecao]["utilizaveis"] + selecao_consertado)
            dispositivos[selecao]["quebrados"] = consertado_novo
            dispositivos[selecao]["utilizaveis"] = utilizavel_novo
            with open("dados/dispositivos.json", "w") as arquivo:
                json.dump(dispositivos, arquivo, indent=4)
                print("Ocorrência concluída!")
                time.sleep(2)
                return
        elif opcao_ocorrencia == 4:
            os.system("cls")
            for item, dados_dispositivo in dispositivos.items():
                print(f"ID: {item}\n"f"Dispositivo: {dados_dispositivo['nome']}\n")
            selecao = input("Digite o ID do dispositivo que gostaria de registrar como encontrado: ")
            if selecao not in dispositivos:
                print("Este dispositivo não existe!")
                time.sleep(2)
                continue
            try:
                selecao_encontrado = int(input("Digite a quantidade que encontrou: "))
            except ValueError:
                print("Digite um valor válido!!")
                time.sleep(2)
                continue
            if selecao_encontrado <= 0:
                print("Quantidade inválida, tente novamente!")
                time.sleep(2)
                continue
            if selecao_encontrado > dispositivos[selecao]["sumido"]:
                print("Quantidade inválida, tente novamente!")
                time.sleep(2)
                continue
            encontrado_novo = (dispositivos[selecao]["sumido"] - selecao_encontrado)
            utilizavel_novo = (dispositivos[selecao]["utilizaveis"] + selecao_encontrado)
            dispositivos[selecao]["sumido"] = encontrado_novo
            dispositivos[selecao]["utilizaveis"] = utilizavel_novo
            with open("dados/dispositivos.json", "w") as arquivo:
                json.dump(dispositivos, arquivo, indent=4)
                print("Ocorrência concluída!")
                time.sleep(2)
                return
        else:
            print("Digite uma opção Válida!")
            time.sleep(2)
            continue

def adicionar_estoque():
    while True:
        os.system("cls")
        cabeçalho("CONTROLE DO ESTOQUE")
        print("\n[1] Adicionar Dispositivo ao estoque")
        print("[2] Remover Dispositivo do estoque")
        print("[0] Voltar ao menu")
        try:
            opcao_estoque = int(input("\nDigite a opção desejada: "))
        except ValueError:
            print("Digite um valor válido!!")
            time.sleep(2)
            continue
        if opcao_estoque == 0:
            return
        elif opcao_estoque == 1:
            for item, dados_dispositivo in dispositivos.items():
                print(f"ID: {item}\n"f"Dispositivo: {dados_dispositivo['nome']}\n")
            adicao_opcao = input("Digite o ID do dispositivo que gostaria de adicionar mais ao estoque: ")
            if adicao_opcao not in dispositivos:
                print("Este dispositivo não existe!")
                time.sleep(2)
                continue
            try:
                quantidade_adicao = int(input("Digite a quantidade que gostaria de adicionar: "))
            except ValueError:
                print("Digite um valor válido!!")
                time.sleep(2)
                continue
            if quantidade_adicao <= 0:
                print("Quantidade inválida, tente novamente!")
                time.sleep(2)
                continue
            estoque_novo = (dispositivos[adicao_opcao]["estoque"] + quantidade_adicao)
            utilizavel_novo = (dispositivos[adicao_opcao]["utilizaveis"] + quantidade_adicao)
            dispositivos[adicao_opcao]["utilizaveis"] = utilizavel_novo
            dispositivos[adicao_opcao]["estoque"] = estoque_novo
            with open("dados/dispositivos.json", "w") as arquivo:
                json.dump(dispositivos, arquivo, indent=4)
                print("Quantidade adicionada!")
                time.sleep(2)
                return
        elif opcao_estoque == 2:
            for item, dados_dispositivo in dispositivos.items():
                print(f"ID: {item}\n"f"Dispositivo: {dados_dispositivo['nome']}\n")
            remover_opcao = input("Digite o ID do dispositivo que gostaria de remover do estoque: ")
            if remover_opcao not in dispositivos:
                print("Este dispositivo não existe!")
                time.sleep(2)
                continue
            try:
                quantidade_remover = int(input("Digite a quantidade que gostaria de remover: "))
            except ValueError:
                print("Digite um valor válido!!")
                time.sleep(2)
                continue
            if quantidade_remover <= 0:
                print("Quantidade inválida, tente novamente!")
                time.sleep(2)
                continue
            if quantidade_remover > dispositivos[remover_opcao]["utilizaveis"]:
                print("Quantidade maior que a disponível!")
                time.sleep(2)
                continue
            estoque_novo = (dispositivos[remover_opcao]["estoque"] - quantidade_remover)
            utilizavel_novo = (dispositivos[remover_opcao]["utilizaveis"] - quantidade_remover)
            dispositivos[remover_opcao]["estoque"] = estoque_novo
            dispositivos[remover_opcao]["utilizaveis"] = utilizavel_novo
            with open("dados/dispositivos.json", "w") as arquivo:
                json.dump(dispositivos, arquivo, indent=4)
                print("Quantidade removida!")
                time.sleep(2)
                return

def dispositivos_menu():
    while True:
        os.system("cls")
        cabeçalho("MENU DISPOSITIVOS")
        print("\n[1] Cadastrar Dispositivo")
        print("[2] Ver dispositivos cadastrados")
        print("[3] Remover Dispositivo")
        print("[4] Estoque de Dispositivos")
        print("[5] Registrar Ocorrência")
        print("[6] Adicionar/Remover dispositivo ao estoque")
        print("[0] Voltar ao menu")
        try:
            opcao_dispositivo = int(input("\nDigite a opção desejada: "))
        except ValueError:
            print("Digite um valor válido!!")
            time.sleep(2)
            continue
        if opcao_dispositivo == 0:
            return
        elif opcao_dispositivo == 1:
            cadastrar_dispositivo()
        elif opcao_dispositivo == 2:
            ver_dispositivo()
        elif opcao_dispositivo == 3:
            remover_dispositivo()
        elif opcao_dispositivo == 4:
            estoque_dispositivo()
        elif opcao_dispositivo == 5:
            registrar_ocorrencia()
        elif opcao_dispositivo == 6:
            adicionar_estoque()
        else:
            print("Digite uma opção Válida!")
            time.sleep(2)
            continue