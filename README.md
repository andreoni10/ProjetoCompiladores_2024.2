# ProjetoCompiladores_2024.22
Projeto da Disciplina Compiladores do período 2024.2

## Motivação
Utilizando os conhecimentos adquiridos na disciplina de Compiladores, colocálos em prática possibilitando o desenvolvimento de um Banco de Dados em exportar no formato de arquivo JSON.

## Descrição Informal da Linguagem
Com linguagem semelhante ao SQL, possui os seguintes comandos:

• Criar tabela:
```
CREATE [nome_tabela];
```

• Selecionar itens:
```
SELECT [col_1], [col_2] FROM [nome_tabela];
```

• Inserir na tabela:
```
INSERT INTO us[nome_tabela]ers ([col_1], [col_2]) VALUES ([val_1], [val_2]);
```

• Atualizar tabela:
```
UPDATE [nome_tabela] SET [col] = [val] WHERE [col] = [val];
```

• Deletar da tabela:
```
DELETE FROM [nome_tabela] WHERE [col] = [val];
```

• Deletar tabela por completo:
```
DELETE [nome_tabela];
```

• Limpar tabela:
```
CLEAR [nome_tabela];
```

• Mostar tabela no terminal:
```
SHOW [nome_tabela];
```

• Exportar tabela específica para arquivo JSON:
```
EXPORT [nome_tabela];
```

• Exportar tonas as tabela em um único arquivo JSON:
```
EXPORT ALL;
```

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
