#Em python
#Crie um arquivo "config.txt" e coloque nele um valor para num. ex: "num = 3"
import sys

# Lê o arquivo de configuração
with open('config.txt', 'r') as f:
    config = f.read().strip()

# Extrai o valor de num
num = int(config.split('=')[1])

# Verifica se o número correto de parâmetros foi passado
if len(sys.argv) - 1 != num:
    print(f"Erro: Esperado {num} parâmetros, mas recebeu {len(sys.argv) - 1}.")
    sys.exit(1)

print(f"Parâmetros recebidos: {sys.argv[1:]}")
