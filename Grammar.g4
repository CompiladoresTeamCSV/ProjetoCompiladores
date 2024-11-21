grammar Grammar;

// Analise Lexica

DECLARE: 'declare';
USE: 'use';
VAR : [A-Za-z]+ ;
ACHAVE : '{';
FCHAVE : '}';
BRANCO : ( ' ' | '\n') -> skip ;

// Analise Sintatica
prog : com EOF ; 
com : DECLARE VAR com 
    | ACHAVE com* FCHAVE
    | USE VAR
    ; 
