import time
import subprocess
import threading

# Função para abrir uma instância do BlueStacks
def abrir_instancia(instancia_id):
    # Altere o caminho para o local onde o BlueStacks está instalado
    caminho_bluestacks = r"C:\Program Files\BlueStacks_nxt\HD-Player.exe"
    subprocess.Popen([caminho_bluestacks, "--instance", instancia_id])
    print(f"Abrindo instância {instancia_id}")

# Função para fechar uma instância do BlueStacks
def fechar_instancia(titulo, tempo_aberto):
    time.sleep(tempo_aberto * 1.5 )
    try:
        subprocess.call(["taskkill", "/F", "/IM", "HD-Player.exe", "/FI", f"WINDOWTITLE eq {titulo.strip()}"])
        print(f"Fechando {titulo}")
    except Exception as e:
        print(f"Erro ao fechar {titulo}: {e}")

# Função para alternar entre conjuntos de instâncias
def alternar_instancias(todas_instancias, tempo_aberto):
    for titulo, instancia_id in todas_instancias:
        abrir_instancia(instancia_id)
        time.sleep(tempo_aberto)

        t = threading.Thread(target=fechar_instancia, args=(titulo, tempo_aberto))
        t.start()

# Exemplo de uso
todas_instancias = [
    ("Conta 1", "Nougat32"),
    ("Conta 2", "Nougat32_2"),
    ("Conta 3", "Nougat32_3"),
    ("v1_conta_1", "Nougat32_9"),
    ("v1_conta_2", "Nougat32_10"),
    ("v1_conta_3", "Nougat32_11"),
    ("v1_conta_4", "Nougat32_12"),
    ("v1_conta_5", "Nougat32_13"),
    ("v1_conta_6", "Nougat32_14"),
    ("v1_conta_7", "Nougat32_15"),
    ("v1_conta_8", "Nougat32_16"),
    ("v2_conta_1", "Nougat32_17"),
    ("v2_conta_2", "Nougat32_18"),
    ("v2_conta_3", "Nougat32_19"),
    ("v2_conta_4", "Nougat32_20"),
    ("v2_conta_5", "Nougat32_21"),
    ("v2_conta_6", "Nougat32_22"),
    ("v2_conta_7", "Nougat32_23")
]

tempo_aberto = 100  # Tempo em segundos

while True:
    alternar_instancias(todas_instancias, tempo_aberto)
