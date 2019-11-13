import ngramss
from parteII import getRecommendation as jonas
import random
import re

class Frame:
	def __init__(self, slots):
		self.slots = slots

	def getSlot(self, slotName, fromStdin = False):
		if not fromStdin:
			slot =  Slot(name, input("Digita o endereco: "))
		else : pass
		self.slots.append(slot)

class Slot:
	def __init__(self, name, valor):
		self.name = name
		self.valor = valor


isDebug = True
restaurantes = ["Pizzaria", "Frutaria", "Pastelaria", "Maçonaria","Massaria", "Hamburgueria","Mercearia", "Peixaria", "Fast Food"]

itens = {
	"Pizzaria" : ["quatro queijos","calabresa", "cheddar", "coca", "guara", "fanta", "sprite", "cini framboesa"],
	"Frutaria" : ["manga","melao", "teucu", "melancia", "banana""coca", "guara", "fanta", "sprite", "cini framboesa"],
	"Pastelaria" : ["quatro queijos","calabresa",  "cheddar", "coca", "guara", "fanta", "sprite", "cini framboesa"],
	"Maçonaria" : ["ilumi","nati", "iluminati", "lumi", "natibrothers""coca", "guara", "fanta", "sprite", "cini framboesa"],
	"Massaria" : ["quatro queijos","calabresa",  "cheddar", "coca", "guara", "fanta", "sprite", "cini framboesa"],
	"Hamburgueria" : ["duplo com queijo","bacon", "triplo", "quarteto fantastico", "jonasburguers""coca", "guara", "fanta", "sprite", "cini framboesa"],
	"Mercearia" : ["pao e queijos","presutno", "jonascommargarina", "pao de queijo", "jeidra""coca", "guara", "fanta", "sprite", "cini framboesa"],
	"Peixaria" : ["peixe com queijos","peixe com calabresa",  "peixe cheddar" "coca", "guara", "fanta", "sprite", "cini framboesa"],
	"Fast Food" : ["açai","jonascom mostarda", "prato feito", "marmitinha", "sorv""coca", "guara", "fanta", "sprite", "cini framboesa"],
}

class StateMachine:
	def __init__(self, frames = []):
		self.frames = frames
		self.currentState = 0
		self.frame = {
			"endereco": "",
			"restaurante": "",
			"itens": [],
			"quantidades": [],
		}


	def askQuestion(self, question):
		res = question()
		if res: self.currentState += 1
		return res

	def randomOrder(self):
		res = []
		numeroPedido = 0
		orderDict = {numeroPedido : 
			{ 
				"endereco": "Iguacu, 1234",
				"restaurante": "restaurante",
				"itens": res,
				"quantidades": random.randint(
				
				1,9)
			}, 
		}

		for restaurante in restaurantes:
			print(numeroPedido)
			orderDict[ numeroPedido] = {
				"endereco": "Iguacu, 1234",
				"restaurante": restaurante,
				"itens": res,
				"quantidades": random.randint(1,9)
			}

			listinha = itens[restaurante]
			orderDict[numeroPedido]["restaurante"] = restaurante
			pick = random.choice(listinha)
			res.append(pick)
			orderDict[numeroPedido]["itens"] = res[numeroPedido]
			numeroPedido += 1

		
		

		
		return orderDict

	def address(self):
		raw = input("Digite rua e numero: ")
		regex = re.compile("^((Rua|Avenida|Alameda) )?[A-z| ]*,( )?((numero|n) )?[0-9]*$")
		if regex.match(raw):
			self.frame["endereco"] = raw
			return True
		return False

	def restaurant(self):
		raw = input("Digite o restaurante: ")
		self.frame['restaurante'] = ngramss.verificaProx(raw, restaurantes[:])

		return True

	def item(self):
		raw = input("Digite o item: ")
		self.frame['itens'].append(ngramss.verificaProx(raw, itens[self.frame["restaurante"][:]]))
		return True

	def qtde(self):
		raw = input("Digite a quantidade: ")
		try: 
			value = int(raw)
			if value > 0:
				self.frame['quantidades'].append(value)
				return True
			return False
		except Exception as e:
			print(e)
			return False


	def querMais(self):
		ret =  input("Digite S para adicionar mais um item: ") == 'S'
		if ret:
			self.currentState = 2
			return False
		return True

	def sugstao(self):
		rec = jonas(self.frame["itens"][-1], itens[self.frame["restaurante"]])

	def updateState(self):
		questions = [
			self.address,
			self.restaurant,
			self.item,
			self.qtde,
			self.sugestao,
			self.querMais,
		]
		pedidos = self.randomOrder()
		for i in range(len(pedidos)):
			print(pedidos[i], "\n")
		
		# while not self.currentState > len (questions) - 1:
		# 	currentQuestion = questions[self.currentState]
			# self.askQuestion(currentQuestion)
			
			

		# return 


StateMachine().updateState()
