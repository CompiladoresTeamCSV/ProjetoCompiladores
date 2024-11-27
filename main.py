import sys
import pandas as pd
from antlr4 import *
from Gramatica_dadosLexer import Gramatica_dadosLexer
from Gramatica_dadosParser import Gramatica_dadosParser

def mostrar(no, indentacao):
    if no.getChildCount() == 0:
        print(indentacao + no.getText())
    else:
        print(indentacao + no.getText())
        for i in range(no.getChildCount()):
            mostrar(no.getChild(i), indentacao + "  ")

def carregar_documento(file):
    tabelinha = pd.read_csv(file, sep=';', header=None)
    return tabelinha

def avalie_pedido(pedido):
    if pedido.comando():  # Processa o comando principal
        comando = pedido.comando().action().getText()
        parametros = []
        condicao = None

        # Verifica os parâmetros
        if pedido.parametros():
            parametros = [param.getText() for param in pedido.parametros().children if param.getText()]

        # Verifica a condição, se existir
        if pedido.condicao():
            condicao = avalie_condicao(pedido.condicao())

        # Executa o comando correspondente
        return execute_comando(comando, parametros, condicao)

    else:
        raise Exception(f"Pedido inválido: {pedido.toStringTree()}")


def avalie_condicao(condicao):
    if condicao.ID() and condicao.OPERATOR():
        variavel = condicao.ID().getText()
        operador = condicao.OPERATOR().getText()
        valor = int(condicao.getChild(2).getText())

        # Avalia a condição simples
        if variavel in vars.keys():
            variavel_valor = vars[variavel]
            if operador == "==":
                return variavel_valor == valor
            elif operador == "!=":
                return variavel_valor != valor
            elif operador == ">":
                return variavel_valor > valor
            elif operador == "<":
                return variavel_valor < valor
            elif operador == ">=":
                return variavel_valor >= valor
            elif operador == "<=":
                return variavel_valor <= valor
            else:
                raise Exception(f"Operador desconhecido: {operador}")
        else:
            raise Exception(f"Variável {variavel} não declarada")
    elif condicao.getChild(0) and condicao.getChild(2):  # Avalia condições compostas
        cond1 = avalie_condicao(condicao.getChild(0))
        operador_logico = condicao.getChild(1).getText()
        cond2 = avalie_condicao(condicao.getChild(2))

        if operador_logico == "&&":
            return cond1 and cond2
        elif operador_logico == "||":
            return cond1 or cond2
        else:
            raise Exception(f"Operador lógico desconhecido: {operador_logico}")
    else:
        raise Exception(f"Condição inválida: {condicao.toStringTree()}")

def execute_comando(comando, parametros, condicao):
    # Implemente o comportamento de cada comando específico
    if comando == "filtre":
        print(f"Filtrando com os parâmetros: {parametros} e condição: {condicao}")
    elif comando == "carregue":
        print(f"Carregando arquivo: {parametros[0]}")
    elif comando == "salve":
        print(f"Salvando em: {parametros[0]}")
    elif comando == "some":
        print(f"Somando com parâmetros: {parametros}")
    elif comando == "media":
        print(f"Calculando média com parâmetros: {parametros}")
    elif comando == "conta":
        print(f"Contando elementos com parâmetros: {parametros}")
    elif comando == "min":
        print(f"Calculando mínimo com parâmetros: {parametros}")
    elif comando == "max":
        print(f"Calculando máximo com parâmetros: {parametros}")
    elif comando == "ordene":
        print(f"Ordenando com parâmetros: {parametros}")
    elif comando == "exporte":
        print(f"Exportando para: {parametros[0]}")
    elif comando == "mescla":
        print(f"Mesclando arquivos: {parametros}")
    else:
        raise Exception(f"Comando desconhecido: {comando}")


# Inicializa um dicionário de variáveis (para armazenar valores de variáveis declaradas)
vars = {"$idade$": 20}  # Definindo a variável $idade$ com o valor 20

def main():
    # Input direto no código
    input_stream = InputStream(
        """
        carregue "dados.csv"
        filtre $idade$ > 18
        salve "resultado.csv"
        """
    )

    # Lexer e Parser
    lexer = Gramatica_dadosLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Gramatica_dadosParser(stream)
    tree = parser.prog()  # Ponto de entrada

    # Percorre cada pedido no programa
    for pedido in tree.pedido():
        avalie_pedido(pedido)


if __name__ == "__main__":
    main()
