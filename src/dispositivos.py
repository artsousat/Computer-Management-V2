import os
import time

from src.utils import cabeçalho

def dispositivos_menu():
    while True:
        os.system("cls")
        cabeçalho("MENU DISPOSITIVOS")
        print("\n[1] Cadastrar Dispositivo")
        print("[2] Ver dispositivos cadastrados")
        print("[3] Remover Dispositivo")
        print("[4] Estoque de Dispositivos")
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
            pass
        elif opcao_dispositivo == 2:
            pass
        elif opcao_dispositivo == 4:
            pass
        elif opcao_dispositivo == 3:
            pass
        else:
            print("Digite uma opção Válida!")
            time.sleep(2)
            continue