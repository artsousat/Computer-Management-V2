import os
import time

from src.professores import professores_menu
from src.dispositivos import dispositivos_menu
from src.utils import cabeçalho
from src.emprestimos import emprestimos_menu

def main():
    while True:
        os.system("cls")
        cabeçalho("COMPUTER MANAGEMENT")
        print("\n[1] Professores")
        print("[2] Dispositivos")
        print("[3] Empréstimos")
        print("[0] Sair")
        try:
            opcao = int(input("\nDigite a opção desejada: "))
        except ValueError:
            print("Digite um valor válido!!")
            time.sleep(2)
            continue
        if opcao == 0:
            print("PROGRAMA ENCERRADO COM SUCESSO!")
            break
        elif opcao == 1:
            professores_menu()
        elif opcao == 2:
            dispositivos_menu()
        elif opcao == 3:
            emprestimos_menu()
        else:
            print("Digite uma opção válida!")
            time.sleep(2)
            continue

main()
