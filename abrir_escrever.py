#em python
# Função para escrever nome de arquivo e data em um arquivo
def escrever_no_arquivo(nome_arquivo, data):

# Abre o arquivo no modo de escrita
with open('saida.txt', 'w') as arquivo:

# Escreve o nome do arquivo na primeira linha
arquivo.write(f'Nome do arquivo: {nome_arquivo}\n')

# Escreve a data na segunda linha
arquivo.write(f'Data: {data}\n')

# Lê o nome do arquivo e a data do usuário
nome_arquivo = input("Digite o nome do arquivo: ")
data = input("Digite a data (formato: DD/MM/AAAA): ")

# Chama a função para escrever no arquivo
escrever_no_arquivo(nome_arquivo, data)
