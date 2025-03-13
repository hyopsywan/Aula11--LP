//Em C 

int main() {
    char nome_arquivo[100];
    char data[11]; 

// Solicita o nome do arquivo
    printf("Digite o nome do arquivo: ");
    scanf("%s", nome_arquivo);

// Solicita a data
    printf("Digite a data (DD/MM/AAAA): ");
    scanf("%s", data);

// Abre o arquivo para escrita
    FILE *arquivo = fopen(nome_arquivo, "w");

// Escreve o nome do arquivo e a data no arquivo
    fprintf(arquivo, "%s\n", nome_arquivo);
    fprintf(arquivo, "%s\n", data);

// Não esqueca de fechar o arquivo
    fclose(arquivo);
