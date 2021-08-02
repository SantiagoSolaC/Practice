from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__, template_folder = "templates")

# Renderisando template
@app.route('/')
def index():
    return render_template('index.html')

# Usando parametros con "?"
@app.route('/ejemplo1')
def parametros():
    param = request.args.get('parametro1', 'vacio')
    param2 = request.args.get('parametro2', 'vacio')
    return f"El parametro es: {param, param2}"

# Usando parametros "/"
@app.route('/ejemplo2/') # Se crea para poder devolver un valor si no se ingresa un parametro y no haga un error
@app.route('/ejemplo2/<name>/') # Se crea el parametro 'name'
@app.route('/ejemplo2/<name>/<last_name>/')
@app.route('/ejemplo2/<name>/<last_name>/<int:edad>')
def parametros2(name = 'nombre', last_name = 'apellido', edad = 'edad'): # Se le da el valor por defecto por si no se ingresa ningun parametro
    return f"El parametro es: {name, last_name, edad}"

# Usando variables, ciclos y condicionales
@app.route('/ejemplo3/<name>')
def ejemplo3(name = 'santiago'):
    age = 27
    my_list = [3,13,23,33]
    return render_template('ejemplo3.html', nombre = name, edad = age, lista = my_list)

# Usando herencia
@app.route('/ejemplo4')
def ejemplo4():
    lista_nombres = ['Santiago', 'Leo', 'Sabrina']
    return render_template('ejemplo4.html', lista = lista_nombres)

if __name__ == '__main__':
    app.run(debug=True)
