import math
import matplotlib.pyplot as plt

def bag_of_words(corpus):
    bag = []
    for phrase in corpus:
        frase = standartize(phrase)
        for word in frase:
            if word not in bag:
                bag.append(word)

    return bag

def frequency(keyword, phrase):
    freq = 0
    phrase = standartize(phrase)
    for word in phrase:
        if word == keyword:
            freq = freq + 1

    return freq

def term_frequency(keyword, phrase):
    freq = 0
    phrase = standartize(phrase)
    for word in phrase:
        if word == keyword:
            freq = freq + 1

    return freq / (len(phrase))


def qntDocumentos_contendoTermo(keyword, corpus):
    docsContendoTermo = 0
    for phrase in corpus:
        phrase = standartize(phrase)
        if (keyword in phrase):
            docsContendoTermo = docsContendoTermo + 1

    return docsContendoTermo


def idf(keyword):
    N = (len(corpus))
    dft = qntDocumentos_contendoTermo(keyword, corpus)
    try:
        inv_document_frequency = math.log((N / dft), 10)
        return inv_document_frequency
    except:
        return None


def tf_idf(keyword, phrase):
    tf = term_frequency(keyword, phrase)
    invdf = idf(keyword)
    try:
        result = tf * invdf
        return result
    except:
        return None


def freq(phrase):
    phrase = standartize(phrase)
    vetorFrequencia = []
    for cont in range(len(phrase)):
        frequencia = 0
        for cont2 in range(1, len(phrase) - 1):
            word = phrase[cont]
            if phrase[cont2] == word:
                frequencia = frequencia + 1
        vetorFrequencia.append(frequencia)

    return vetorFrequencia

def standartize(phrase):

    phrase = phrase.replace(".", "")
    phrase = phrase.replace(",", "")
    phrase = phrase.replace("'", "")
    phrase = phrase.lower()
    phrase = phrase.split()

    return phrase

def frequencyByTerm(text):
    textos = ""
    for texto in text:
        textos += texto + " "

    bag = bag_of_words(text)
    frequencia = []
    for word in bag:
        freq = frequency(word, textos)
        frequencia.append(freq)
    frequencia.sort(reverse=True)
    return frequencia

def zipfLaw(corpus):
    frequenciaTermos = frequencyByTerm(corpus)
    plt.plot(frequenciaTermos)
    plt.title("Zipf Law")
#    plt.show()

def persist_pedidos(pedidos):
    res = ''
    for i in pedidos:
        for _, v in i.items():
            # print(type(v))
            if type(v) == list:
                # print("--------------")
                for j in v: res += str(j).replace(' ', '-') + "/"
            else:
                res += str(v).replace(' ', '-') 
            res += ' '
            res = res.replace("/", ' ')

        res = res[:-1]
        res += '\n'
    with open("corpus.txt", 'w') as fopen:
        fopen.write(res[:-1])
        
def load_pedidos():
    with open("corpus.txt", 'r') as fopen:
        text = fopen.read()
        
        return text.split("\n")

    

corpus = [
    {'endereco': 'Iguacu, 1234', 'restaurante': 'Pizzaria', 'itens': ['quatro queijos', 'coca'], 'quantidades': 4},

    {'endereco': 'Iguacu, 1234', 'restaurante': 'Frutaria', 'itens': ['quatro queijos', 'coca'], 'quantidades': 1},

    {'endereco': 'Iguacu, 1234', 'restaurante': 'Pastelaria', 'itens': 'quatro queijos', 'quantidades': 3},

    {'endereco': 'Iguacu, 1234', 'restaurante': 'Maçonaria', 'itens': 'ilumi', 'quantidades': 1},

    {'endereco': 'Iguacu, 1234', 'restaurante': 'Massaria', 'itens': 'cheddar', 'quantidades': 2},

    {'endereco': 'Iguacu, 1234', 'restaurante': 'Hamburgueria', 'itens': ['quatro queijos', 'GUARA'], 'quantidades': 9},

    {'endereco': 'Iguacu, 1234', 'restaurante': 'Mercearia', 'itens': 'jeidra', 'quantidades': 6},

    {'endereco': 'Iguacu, 1234', 'restaurante': 'Peixaria', 'itens': 'peixe com queijos', 'quantidades': 8},

    {'endereco': 'Iguacu, 1234', 'restaurante': 'Fast Food', 'itens': 'prato feito', 'quantidades': 2},
] #documentos

# persist_pedidos(corpus)

# corpus  = load_pedidos()
# print("corpus", corpus)
# # Resposta questão 1:
# palavras = ["quatro-queijos"]
# bag = bag_of_words(corpus)

def filter_tf():
    ret = []
    for word in palavras:
        for cont in range(len(corpus)):
            if term_frequency(word, corpus[cont]) > 0:

                # print("Palavra:", word, "| tf:", term_frequency(word, corpus[cont]), "| idf:", idf(word), "| tf-idf:", tf_idf(word, corpus[cont]), "| Documento:", corpus[cont])
                ret.append(corpus[cont])
    return ret

def get_items(l):
    'Iguacu,-1234 Pizzaria quatro-queijos coca  4'
    items = [i for i in l.split(' ')[2:-1] if not i == '' ]
    return (items)
    
    #        if  corpus[cont] == " " or  corpus[cont] == "\n":  continue
#for word in palavras:
#
#    for cont in range(len(corpus)):
##        if  corpus[cont] == " " or  corpus[cont] == "\n":  continue
#        print("Palavra:", word, "| tf:", term_frequency(word, corpus[cont]), "| idf:", idf(word), "| tf-idf:",
#              tf_idf(word, corpus[cont]), "| Documento:", corpus[cont])
#
## Resposta questão 2:
# filtered = filter_tf()
# items = [get_items(i) for i in filtered]
# flatItems = [[i for i in item] for item in items][0]
# print("itens", items)
# d = { }

# for i in items:
#     for j in i:
#         if j in palavras: continue
#         try:
#             d[j] += 1
#         except KeyError:
#             d[j] = 1

# print("d is", d)

# s = list(reversed(sorted([(value,key) for (key,value) in d.items()])))[0][-1]

def getRecommendation(words, corpus):
    bag = bag_of_words(corpus)
    filtered = filter_tf()
    items = [get_items(i) for i in filtered]
    flatItems = [[i for i in item] for item in items][0]
    print("itens", items)
    d = { }
    for i in items:
        for j in i:
            if j in palavras: continue
            try:
                d[j] += 1
            except KeyError:
                d[j] = 1

    return list(reversed(sorted([(value,key) for (key,value) in d.items()])))[0][-1]


# print("s", s)
# # print(filtered)
# zipfLaw(corpus)

