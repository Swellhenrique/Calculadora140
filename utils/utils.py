import csv  # biblioteca para ler e escrever arquivos no formato CSV

def ler_csv(arquivo_csv):
    dados_csv = []                                         # cria uma lista em branco 
    try:                                                   # tentar / tratamento de erro
        with open(arquivo_csv, newline='')  as massa:      # com o arquivo ---> informa o nome e apelido massa
                                                           # newline seria o caracter de final de linha 
            tabela = csv.reader(massa, delimiter=',')      # com os dados do arquivo, menos o cabeçalho
                                                           # informando que o separador é a virgula
            next(tabela)                                   # serve aqui para pular a linha de cabeçalho 
            for linha in tabela:                           # para cada linha na tabela 
                dados_csv.append(linha)                    # guardando os dados separados para uso 
        return dados_csv                                   # devolver os dados para serem usados no teste
    except FileNotFoundError:                              # tratamento de erro para arquivo nao encontrado 
        print(f' Arquivo não encontrado: {arquivo_csv}')   # mensagem de erro de arquivo nao encontrado
    except Exception as fail:                              # qualquer erro nao previsto 
        print(f'Falha imprevista: {fail}')                 # mensagem de erro que voltara do sistema 