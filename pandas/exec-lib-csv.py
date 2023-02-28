import csv

# Abrindo o arquivo em modo de leitura (r)
with open("dados.csv", "r") as arquivo:
    # Criando um leitor CSV
    leitor = csv.reader(arquivo)
    # Lendo a primeira linha do arquivo como cabeçalho
    cabecalho = next(leitor)
    cabecalho = cabecalho[0].split(";")
    print("{:<20} {:<20} {:<20}".format(*cabecalho))
    print("-" * 60)
    for valores in leitor:
        valores = valores[0].split(";")
        print("{:<20} {:<20} {:<20}".format(*valores))