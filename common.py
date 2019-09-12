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

	ignore = '\n\t '
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
	
	TIPO  = r'\:'
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


class PortugolParser(Parser):
	
	tokens = PortugolLexer.tokens

	# @_('INICIO comando FIM')
	# def comando(self, p):
	# 	return p.comando

	@_('comando')
	def statement(self, p):
		print("Inicio")

	@_('ID ASSIGN NUMBER EOL')
	@_('ID ASSIGN NUMBER EOL comando')
	def comando(self, p):
		print("ATRIBUI", p.ID, p.NUMBER)

	@_('INTEIRO TIPO ID EOL')
	@_('INTEIRO TIPO ID EOL comando')
	def comando(self, p):
		print("CRIEI", p.ID)

	# @_('ID ASSIGN NUMBER p.ID, p.NUMBER)




lex = PortugolLexer()
parser = PortugolParser()
file = open('./teste2.txt', 'r')
text = file.read()
file.close()

# for tok  in lex.tokenize(text): print("tok", tok.type, tok.value)

res = parser.parse(lex.tokenize(text))

print(res)

