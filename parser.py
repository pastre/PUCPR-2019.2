from sly import Lexer,  Parser

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
