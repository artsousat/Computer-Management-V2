import os
import time

from src.utils import cabeçalho

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
            pass
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