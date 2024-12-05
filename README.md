Compilador para Linguagem de Processamento de Dados
Equipe
Nome da Equipe: AILA
Integrantes:
Ayna Araújo
Igor Balbino
Lucas César
Motivação
Este projeto visa implementar um compilador para uma linguagem de processamento de dados, inspirada em comandos simples para manipulação de tabelas em formato CSV. A linguagem tem como objetivo fornecer uma interface simples para realizar operações de filtragem, carregamento e salvamento de dados, focando em simplificar tarefas comuns de manipulação de dados.
O objetivo principal do projeto é desenvolver habilidades no uso de ANTLR para gerar um compilador que possa ser utilizado como base para futuras implementações mais avançadas e como uma ferramenta útil para tarefas de processamento de dados.
Descrição Informal da Linguagem
A linguagem implementada no projeto é uma linguagem de processamento de dados que permite realizar as seguintes operações:
carregar: Carrega um arquivo CSV para ser manipulado.
filtre: Filtra os dados com base em uma condição específica.
salve: Salva os dados manipulados em um arquivo CSV.
A linguagem foi projetada para ser simples e intuitiva, utilizando uma sintaxe parecida com comandos em inglês. As variáveis podem ser definidas para armazenar valores que serão usados nas condições dos filtros.
Comandos Disponíveis
carregue "<nome_do_arquivo.csv>";: Carrega o arquivo CSV para ser processado.
filtre "<nome_da_coluna>" <operador> <valor>;: Filtra os dados com base na condição.
salve "<nome_do_arquivo.csv>";: Salva os dados filtrados ou manipulados em um novo arquivo CSV.
A sintaxe da linguagem permite o uso de variáveis para armazenar valores temporários e aplicá-los nas condições de filtragem.
Exemplos de Comandos
Carregar um arquivo CSV:

 carregue "dados.csv";


Filtrar os dados para obter linhas onde a idade seja maior que 40:

 filtre "idade" > 40;


Salvar o resultado filtrado em um novo arquivo CSV:

 salve "resultado.csv";


Definição de Variáveis
As variáveis podem ser definidas para armazenar valores temporários. Elas são usadas com o formato $variavel$ e podem ser usadas nas condições de filtragem.
Exemplo:
$idade_limite$ = 30;
filtre "idade" > $idade_limite$;

Como Executar o Compilador
Pré-requisitos
Python 3.x
Bibliotecas: antlr4, pandas, re
Passos para Execução
Instale as dependências necessárias: No terminal, execute o comando para instalar as bibliotecas necessárias:

 pip install antlr4-python3-runtime pandas


Compile a Gramática ANTLR: Antes de executar o compilador, é necessário gerar o código do lexer e do parser com a gramática definida. Para isso, execute o comando no terminal:

 antlr4 Gramatica_dados.g4 -Dlanguage=Python3
 Isso irá gerar os arquivos Gramatica_dadosLexer.py e Gramatica_dadosParser.py.


Execute o compilador: Após compilar a gramática, você pode executar o programa Python com o comando:

 python seu_arquivo.py
 Isso irá rodar o compilador, processando o código fornecido no input e gerando a saída conforme os comandos executados.


Exemplos de Programas
Exemplo 1: Carregar, Filtrar e Salvar Dados
carregue "dados.csv";
$idade_limite$ = 30;
filtre "idade" > $idade_limite$;
salve "resultado.csv";

Explicação:
O arquivo dados.csv é carregado.
A variável $idade_limite$ é definida com o valor 30.
O comando filtre é usado para selecionar os registros onde a idade é maior que 30.
O resultado é salvo no arquivo resultado.csv.
Exemplo 2: Filtragem Simples
carregue "dados.csv";
filtre "idade" > 40;
salve "maiores_que_40.csv";

Explicação:
O arquivo dados.csv é carregado.
O comando filtre é usado para selecionar os registros onde a idade é maior que 40.
O resultado é salvo no arquivo maiores_que_40.csv.
Exemplo 3: Comando Sem Variáveis
carregue "dados.csv";
filtre "sexo" == "F";
salve "resultado_feminino.csv";

Explicação:
O arquivo dados.csv é carregado.
O comando filtre é usado para selecionar os registros onde o sexo é feminino ("F").
O resultado é salvo no arquivo resultado_feminino.csv.
Conclusão
Este projeto fornece uma implementação simples de uma linguagem de processamento de dados, permitindo carregar, filtrar e salvar arquivos CSV com uma sintaxe intuitiva. Ele é baseado no uso de ANTLR para o parsing e execução de comandos definidos pelo usuário.

Instruções de Como Rodar:
abrir o terminal na pasta do projeto e rodar o comando "java -jar antlr.jar -Dlanguage=Python3 Gramatica_dados.g4" para gerar o código do lexer e do parser com a gramática definida. Isso irá gerar os arquivos Gramatica_dadosLexer.py e Gramatica_dadosParser.py.(nesse caso ele já estão criados)
posteriormente, rodar o arquivo main.py para executar o programa.
OBS: O código a ser interpretado deve estar no input_stream.(presente no main.py)