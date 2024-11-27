import sys
import pandas as pd
from antlr4 import *
from Gramatica_dadosLexer import Gramatica_dadosLexer
from Gramatica_dadosParser import Gramatica_dadosParser
from utils import *

tabelinhas = {}

def mostrar(no, indentacao):
    if no.getChildCount() == 0:
        print(indentacao + no.getText())
    else:
        print(indentacao + no.getText())
        for i in range(no.getChildCount()):
            mostrar(no.getChild(i), indentacao + "  ")

def carregar_documento(file):
    tabelinha = pd.read_csv(file, sep=';', header=None)
    tabelinhas[f'{get_num_tabelinhas()}'] = tabelinha

def verificar_programa(programa):
    return programa.split(';')

def avalie_pedido(pedido, num):
    
    if num == 0:
        if pedido.comando().action().getText() != "carregue":
            raise Exception("O primeiro pedido dever ser carregar um csv") 
        else:
        
            carregar_documento(pedido.parametros().getText().replace('"',''))
            return
    if pedido.comando() and num!=0:  # Processa o comando principal
        print(tabelinhas)
        comando = pedido.comando().action().getText()

        parametros = []
        condicao = None
        carrega = False
        tabelinha = tabelinhas['0']

        # Verifica os parâmetros
        if pedido.parametros():
            parametros = [param.getText() for param in pedido.parametros().children if param.getText()]

        # Verifica a condição, se existir
        if pedido.condicao():
            condicao = avalie_condicao(pedido.condicao())


        # Executa o comando correspondente
        print(num)
        return execute_comando(condicao,comando, parametros,tabelinha)   

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


def execute_comando(condicao,comando, parametros, tabelinha = None):
    print(parametros)

    

    for param in parametros:
        if "$" in param:
            coluna = param.replace('$', '')
            break


    if comando == "filtre":
        print((tabelinha[coluna] > 25).sum())
    
    elif comando == "carregue":
        if tabelinha_exists():
            print("Tabela já existe")
        else:
            carregar_documento(parametros[0],parametros[1])

    elif comando == "salve":

        pd.to_csv('dados/{parametro.csv}',tabelinha)

    elif comando == "some":
        soma = tabelinha[parametros].sum()
        print(soma)
    
    elif comando == "media":
        media = tabelinha[parametros].mean()
        print(media)
    
    elif comando == "conte":
        count = tabelinha[parametros].value_counts()
        print(count)

    elif comando == "min":
        min = tabelinha[parametros].min()
        print(min)

    elif comando == "max":
        max = tabelinha[parametros].max()   
        print(max)

    elif comando == "ordene":
        tabelinha = tabelinha.sort_values(by = parametros)

    elif comando == "exporte":
       pd.to_csv(parametros,tabelinha)

    else:
        raise Exception(f"Comando desconhecido: {comando}")


# Inicializa um dicionário de variáveis (para armazenar valores de variáveis declaradas)
vars = {"$idade$": 20}  # Definindo a variável $idade$ com o valor 20

def main():
    # Input direto no código
    input_stream = InputStream(
        """
        carregue "dados.csv";      
        filtre $idade$ > 18;
        salve "resultado.csv";
        """
    )

    # Lexer e Parser
    lexer = Gramatica_dadosLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Gramatica_dadosParser(stream)
    tree = parser.prog()  # Ponto de entrada

    # Percorre cada pedido no programa
    
    for line, pedido in enumerate(tree.pedido()):
        
        avalie_pedido(pedido,line)


if __name__ == "__main__":
    main()
