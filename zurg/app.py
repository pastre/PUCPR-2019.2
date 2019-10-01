#### API

from flask import Flask, request

ip, porta = input("Entre com o IP"), int(input("Entre com a porta"))

app = Flask(";lkjhgfds")

transformadores = {

}

def build_line(param):
	return f'tId: {param["tId"]}, serie: {param["serie"]}, tensaoRef: {param["tensaoRef"]}, errorRef: {param["errorRef"]}, error: {param["error"]},\
	 status: {param["status"]}, media: {param["media"]}\n'

def add_medida(param):
	global transformadores

	tId = param["tId"]
	if not tId in transformadores.keys():
		transformadores[tId] = []
	transformadores[tId].append(param)


def build_response():
	ret = ""

	for _, transformador in transformadores.items():

		for leitura in transformador:
			ret += build_line(leitura) + "<br />"

	return ret


@app.route('/vpp', methods = ['GET', 'POST'])
def vpp():
	if request.method == 'POST':
		payload = dict(request.form)
		print("request", payload)
		add_medida(payload)
		return payload

		{
            "tId" : self.tId ,
            "serie" : self.serie ,
            "tensaoRef" : self.tensaoRef ,
            "errorRef" : self.error ,
            "error": error,
            "status": status,
            "media": media
        }
	return build_response()


app.run(ip, porta)
