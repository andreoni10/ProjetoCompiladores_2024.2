# ProjetoCompiladores_2024.22
Projeto da Disciplina Compiladores do período 2024.2


## Equipe
• Bruno Roberto Lima Ramos Rangel </br>
• Lucas Hernandes Andreoni </br>
• Nathália Bacalhau </br>
• Silas Nascimento

## Motivação
Utilizando os conhecimentos adquiridos na disciplina de Compiladores, colocálos em prática possibilitando o desenvolvimento de um Banco de Dados em exportar no formato de arquivo JSON.

## Descrição Informal da Linguagem
Com linguagem semelhante ao SQL, possui os seguintes comandos:

• CREATE [nome_tabela]; </br>
• SELECT [col_1], [col_2] FROM [nome_tabela]; </br>
• INSERT INTO us[nome_tabela]ers ([col_1], [col_2]) VALUES ([val_1], [val_2]); </br>
• UPDATE [nome_tabela] SET [col] = [val] WHERE [col] = [val]; </br>
• DELETE FROM [nome_tabela] WHERE [col] = [val]; </br>
• DELETE [nome_tabela]; </br>
• CLEAR [nome_tabela]; </br>
• SHOW [nome_tabela]; </br>
• EXPORT [nome_tabela];
• EXPORT ALL;

## Guia de Como Executar o Compilador

1. No terminal, digite o comando:

```
java -jar antlr.jar -Dlanguage=Python3 Expressoes.g4
```

2. No arquivo ```main.py```, escreva o código como uma string em ```input_text``` e execute o código.

## Exemplos de programas

```
CREATE futebol;
INSERT INTO futebol (id, name) VALUES (1, 'Neymar');
INSERT INTO futebol (id, name) VALUES (2, 'Messi');
SELECT id, name FROM futebol;
SHOW futebol;

CREATE basquete;
INSERT INTO basquete (id, name) VALUES (1, 'Lebron');
INSERT INTO basquete (id, name) VALUES (2, 'Michael Jordan');
SELECT id, name FROM basquete;
SHOW basquete;

EXPORT futebol;
EXPORT basquete;
EXPORT ALL;
```