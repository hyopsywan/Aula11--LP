# Lê os nomes dos arquivos a partir de config.txt
with open('config.txt', 'r') as config_file:
    arquivos = config_file.read().splitlines()

# Cria ou abre o arquivo resultado.txt para escrita
with open('resultado.txt', 'w') as resultado_file:
    for arquivo in arquivos:
        try:
            # Lê o conteúdo de cada arquivo e escreve no resultado.txt
            with open(arquivo, 'r') as file:
                conteudo = file.read()
                resultado_file.write(conteudo + '\n')  # Adiciona uma nova linha entre os conteúdos
print("Conteúdo combinado foi salvo em resultado.txt.")
