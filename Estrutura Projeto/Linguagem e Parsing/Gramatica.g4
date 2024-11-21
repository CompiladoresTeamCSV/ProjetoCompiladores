grammar Gramatica;

//Analise Lexica

//SUJEITOS
Time:'\*'[A-Za-z ]+'\*';
Nome: '\$'[A-Za-z ]+'\$';

//AÇÕES
Gol: 'gol';
Fez: 'fez'|'furou';
Receber: 'tomou'|'recebeu';
Entrada_Saida:'entra'|'sai';
Falta: 'falta';
Penalti: 'penalti';
Troca:'troca';
Machucado:'machucado'; 

//Pontuação
PotuacaoF: '.'| '!';
PontuacaoM: ',';

//TEMPO
Tempo: [0-1][0-9][0-9];
Minuto: 'minuto';

//Status
Cor: 'amarelo'|'vermelho';


Gravidade:'branda'|'grave';


BRANCO : (' ' | '\n' | '\t') -> skip ;

//Analise Sintatica

jogo: partida EOF;
partida: Frase + Minuto Tempo; 
Frase: Sujeito  (Action)? PotuacaoF; 
Sujeito: Time | Nome;
Action: (Fez | Receber | Entrada_Saida | Gol | Falta | Penalti | Troca | Machucado) (Status)?;
Status: Cor | Gravidade;



