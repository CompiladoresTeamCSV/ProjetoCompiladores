grammar Gramatica_dados;

// Análise Léxica

// PALAVRAS RESERVADAS
FILTER: 'filtre';
LOAD: 'carregue';
SAVE: 'salve';
SUM: 'some';
AVG: 'media';
COUNT: 'conta';
MIN: 'min';
MAX: 'max';
SORT: 'ordene';
EXPORT: 'exporte';
MERGE: 'mescla';

// TOKENS
STRING: '"' (~["\r\n])* '"'; // Texto entre aspas, sem novas linhas
FILE: '"' (~["\r\n])* '\\.' [a-zA-Z]+ '"'; // Arquivos como "dados.csv"
ID: '$' [A-Za-z_][A-Za-z0-9_]* '$'; // Identificadores delimitados por '$'
NUMBER: [0-9]+ ('.' [0-9]+)?; // Números inteiros ou decimais
OPERATOR: '<' | '>' | '=' | '>=' | '<=' | '==' | '!='; // Operadores relacionais
LOGICAL_OPERATOR: '&&' | '||'; // Operadores lógicos
BRANCO: (' ' | '\n' | '\t') -> skip; // Ignorar espaços e quebras de linha

// Análise Sintática

prog: pedido+ EOF; // Ponto de entrada

pedido: comando (parametros)? (condicao)?;

comando: action;

parametros: (ID | STRING | FILE | NUMBER)+;

condicao: ID OPERATOR (STRING | NUMBER)
          (LOGICAL_OPERATOR condicao)?; // Condições compostas

action: FILTER | LOAD | SAVE | SUM | AVG | COUNT | MIN | MAX | SORT | EXPORT | MERGE;
