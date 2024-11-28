grammar Expressoes;

// Lexer rules
CREATE: 'CREATE';
SELECT : 'SELECT';
INSERT : 'INSERT';
UPDATE : 'UPDATE';
DELETE : 'DELETE';
CLEAR : 'CLEAR';
SHOW : 'SHOW';
FROM : 'FROM';
WHERE : 'WHERE';
SET : 'SET';
INTO : 'INTO';
VALUES : 'VALUES';
AND : 'AND';
OR : 'OR';
EQ : '=';
NEQ : '!=';
GT : '>';
LT : '<';
COMMA : ',';
PV : ';';
LPAR : '(';
RPAR : ')';
ID : [a-zA-Z_][a-zA-Z_0-9]*;
NUM : [0-9]+;
STRING : '\'' .*? '\''; // Adiciona suporte para strings entre aspas simples
WS : [ \t\r\n]+ -> skip;

// Parser rules
prog : stmt+ ;
stmt : createStmt | selectStmt | insertStmt | updateStmt | deleteItemStmt | deleteTableStmt | clearStmt | showStmt;

createStmt : CREATE table PV ;
selectStmt : SELECT columns FROM table (WHERE condition)? PV ;
insertStmt : INSERT INTO table LPAR columns RPAR VALUES LPAR values RPAR PV ;
updateStmt : UPDATE table SET assignments (WHERE condition)? PV ;
deleteItemStmt : DELETE FROM table (WHERE condition)? PV ;
deleteTableStmt : DELETE table PV ;
clearStmt : CLEAR table PV ;
showStmt : SHOW table PV ;

columns : ID (COMMA ID)* ;
values : value (COMMA value)* ;
assignments : assignment (COMMA assignment)* ;
assignment : ID EQ value ;
condition : ID (EQ | NEQ | GT | LT) value (AND condition | OR condition)? ;
value : NUM | ID | STRING ; // Adiciona suporte para strings entre aspas simples
table : ID ;