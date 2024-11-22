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
STRING: [A-Za-z]+;
OPERATOR: '<' | '>' | '=' | '>=' | '<=' | '==' | '!=';
ID: '$' [A-Za-z_][A-Za-z0-9_]* '$';
NUMBER: [0-9]+;
BRANCO: (' ' | '\n' | '\t') -> skip;

// Análise Sintática

PROG: PEDIDO+ EOF;

PEDIDO: COMANDO (PARAMETROS)? (CONDICAO)?;

COMANDO: ACTION;

PARAMETROS: (ID | STRING | NUMBER)+;

CONDICAO: ID OPERATOR (STRING | NUMBER) ('&&' | '||' CONDICAO)?;

ACTION: FILTER | LOAD | SAVE | SUM | AVG | COUNT | MIN | MAX | SORT | EXPORT | MERGE;