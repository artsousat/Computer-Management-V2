from datetime import datetime

def cabeçalho(titulo):
    agora = datetime.now()
    data_hora = agora.strftime("%d/%m/%y - %H:%M:%S")
    print("=" * 40)
    print("          ",titulo)
    print("          ",data_hora)
    print("=" * 40)
