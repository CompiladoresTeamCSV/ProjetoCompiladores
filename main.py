import sys
import pandas as pd
from antlr4 import *
from Gramatica_dadosLexer import Gramatica_dadosLexer
from Gramatica_dadosParser import Gramatica_dadosParser

# Dicionário global de tabelas (DataFrames)
tabelinhas = {}

# Tabela ativa
tabela_ativa = None

def resolve_variavel(nome):
    """
    Resolve o valor de uma variável no formato $variavel$, se necessário.
    """
    if nome.startswith("$") and nome.endswith("$"):
        raise Exception(f"Uso de variáveis no formato $variavel$ não implementado neste programa.")
    return nome

def carregar_documento(file):
    """
    Carrega um arquivo CSV e armazena em tabelinhas.
    """
    global tabelinhas, tabela_ativa
    tabelinha = pd.read_csv(file, sep=';')  # Usa cabeçalhos do CSV
    index = len(tabelinhas)
    tabelinhas[f'{index}'] = tabelinha
    tabela_ativa = tabelinha
    print(f"Arquivo '{file}' carregado com sucesso na tabela {index}.")

def avalie_condicao(condicao):
    """
    Avalia a condição lógica.
    """
    if condicao.getChildCount() == 3:
        coluna = condicao.getChild(0).getText().strip('"')  # Assume que o nome da coluna é uma string
        operador = condicao.getChild(1).getText()
        valor = resolve_variavel(condicao.getChild(2).getText())

        return coluna, operador, valor
    elif condicao.getChildCount() == 1:
        return avalie_condicao(condicao.getChild(0))
    else:
        raise Exception(f"Condição inválida: {condicao.toStringTree()}")

def execute_comando(condicao, comando, parametros, tabelinha=None):
    """
    Executa o comando com base na condição e parâmetros.
    """
    global tabela_ativa

    if comando == "carregue":
        if len(parametros) != 1:
            raise Exception("O comando 'carregue' requer um único parâmetro (nome do arquivo).")
        carregar_documento(parametros[0].strip('"'))
    elif comando == "filtre":
        if not condicao:
            raise Exception("O comando 'filtre' exige uma condição.")
        coluna, operador, valor = condicao
        if operador == ">":
            tabela_ativa = tabelinha[tabelinha[coluna] > float(valor)]
        elif operador == "<":
            tabela_ativa = tabelinha[tabelinha[coluna] < float(valor)]
        elif operador == "==":
            tabela_ativa = tabelinha[tabelinha[coluna] == float(valor)]
        else:
            raise Exception(f"Operador desconhecido: {operador}")
        print(f"Tabela filtrada com base na condição: {coluna} {operador} {valor}.")
    elif comando == "salve":
        if len(parametros) != 1:
            raise Exception("O comando 'salve' requer um único parâmetro (nome do arquivo).")
        nome_arquivo = parametros[0].strip('"')
        tabela_ativa.to_csv(nome_arquivo, index=False, sep=";")
        print(f"Tabela salva em '{nome_arquivo}'.")
    else:
        raise Exception(f"Comando desconhecido: {comando}")

def avalie_pedido(pedido, num):
    """
    Avalia cada pedido no programa, verificando comando, parâmetros e condições.
    """
    global tabela_ativa

    comando = pedido.comando().action().getText()
    parametros = []
    condicao = None

    if pedido.parametros():
        parametros = [resolve_variavel(param.getText()) for param in pedido.parametros().children if param.getText()]

    if pedido.condicao():
        condicao = avalie_condicao(pedido.condicao())

    execute_comando(condicao, comando, parametros, tabela_ativa)

def main():
    input_stream = """
        carregue "dados.csv";
        filtre "idade" > 50;
        salve "resultado.csv";
    """

    # Lexer e Parser
    lexer = Gramatica_dadosLexer(InputStream(input_stream))
    stream = CommonTokenStream(lexer)
    parser = Gramatica_dadosParser(stream)
    tree = parser.prog()

    # Percorre cada pedido no programa
    for line, pedido in enumerate(tree.pedido()):
        avalie_pedido(pedido, line)

if __name__ == "__main__":
    main()
