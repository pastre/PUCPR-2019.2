from sly import Lexer,  Parser

class PortugolLexer(Lexer):
	tokens = { 
		ID, 
		STRING,
		NUMBER, 
		PLUS, 
		MINUS, 
		TIMES,
		DIVIDE, 
		ASSIGN, 
		LPAREN, 
		RPAREN, 
		EQ, 
		GREATER_THEN_EQ ,
		LESS_THEN_EQ ,
		NOT_EQ,
		GREATER_THEN,
		LESS_THEN,
		INTEIRO,
		IMPRIMA,
		LEIA,
		PARA,
		FIM_PARA,
		SE,
		ENTÃO,
		SENÃO,
		FIM_SE,
		TIPO,
		ATÉ,
		PASSO,
		EOL,
		INICIO,
		FIM
	}

	ignore = ' \t\n'
	ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
	STRING      = r'\".*\"'
	NUMBER  = r'\d+'

	ASSIGN  = r'<-'

	GREATER_THEN_EQ = '>='
	LESS_THEN_EQ = '<='
	NOT_EQ = '<>'

	EQ = '='
	PLUS	= r'\+'
	MINUS   = r'-'
	TIMES   = r'\*'
	DIVIDE  = r'/'

	GREATER_THEN = '>'
	LESS_THEN = '<'

	LPAREN  = r'\('
	RPAREN  = r'\)'
	
	TIPO  = r':'
	EOL = r';'

	ID['inteiro'] = INTEIRO

	ID['imprima'] = IMPRIMA
	ID['leia'] = LEIA

	ID['para'] = PARA
	ID['fim_para'] = FIM_PARA

	ID['se'] = SE
	ID['então'] = ENTÃO
	ID['senão'] = SENÃO
	ID['fim_se'] = FIM_SE

	ID['inicio'] = INICIO
	ID['fim'] = FIM
	
	ID['ate'] = ATÉ
	ID['passo'] = PASSO

lex = PortugolLexer()
text = open('./teste2.txt', 'r').read()

for tok  in lex.tokenize(text): print("tok", tok.type, tok.value)


