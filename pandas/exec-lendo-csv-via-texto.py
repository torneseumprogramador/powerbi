# Extract = pegamos o dado do CSV
with open("dados.csv", "r") as arquivo:
    # Transform = transformar os dados
    cabecalho = arquivo.readline().strip().split(";")
    print("{:<20} {:<20} {:<20}".format(*cabecalho))
    print("-" * 60)
    for linha in arquivo:
        valores = linha.strip().split(";")
        print("{:<20} {:<20} {:<20}".format(*valores))
        # Mostrou dados transformados na tela