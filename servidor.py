from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/calculo/", methods=['POST'])
def calculadora():

    numero1 = request.form['numero1']
    numero2 = request.form['numero2']
    operacao = request.form['operacao']
    resultado = 0

    numero1 = float(numero1)
    numero2 = float(numero2)
    operacao = str(operacao)

    if (operacao == "*"):
        resultado = numero1 * numero2
    elif (operacao == "/"):
        resultado = numero1 / numero2
    elif (operacao == "+"):
        resultado = numero1 + numero2
    elif (operacao == "-"):
        resultado = numero1 - numero2

    return str(resultado)

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)