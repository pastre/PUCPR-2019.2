import sys

def diagramas(string):
	lista = []
	for i in range(len(string)):
		if i <= len(string ) -2:
			lista.append(string[i]+ string[i+1])
	return(lista)

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

def nivelProximidade(string1, string2):
	# print(string1, string2)
	if len(string1) < 5 and len(string2) < 5: return
	doc1 = diagramas(string1)
	doc2 = diagramas(string2)
	doc1Contador = []
	doc2Contador = []

	for i in doc1:
		if doc1.count(i) == 1:

			doc1Contador.append(i)

	for i in doc2: 
		if doc2.count(i) ==  1:
			doc2Contador.append(i)
	a = len(doc1Contador)
	b = len(doc2Contador)
	if a or b != 0:
		c = len(intersection(doc1Contador, doc2Contador))
		conta = 2*c / (a+b)
		return(conta)


def verificaProx(string, palavras):
	currMajor = 0
	array = []

	for palavra in palavras:

		nProx = nivelProximidade(string, palavra)
		array.append([nProx, palavra])
		if nProx > currMajor:
			currMajor = nProx

	array.sort()
	array.reverse()
	lista = []

	# for i in array:
	# 	lista[array.index(i)] = (i[1], i[0]*100)
	
	result = [(i[1], i[0]*100) for i in array]

	if result[0][1] >= 70:
		return result[0][0]
	elif result[0][1] == 0:
		str = input("insira novamente onde comer: ")
		verificaProx(str, palavras)
	else:
		if input("Voce quis dizer {0} ?".format(result[0][0])) == "sim":
			return result[0][0]
		else:
			str = input("Insira onde quer comer: ")
			verificaProx(str, result)


