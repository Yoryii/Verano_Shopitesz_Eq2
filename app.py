from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

@app.route('/login')
def login():
    return render_template('Usuarios/login.html')

@app.route('/usuarios/new')
def registrarUsuario():
    return render_template('Usuarios/registrar.html')

@app.route('/pedidos/pedidos')
def consultarPedidos():
    return render_template('Pedidos/pedidos.html')

@app.route('/pedidos/verPedido')
def verPedido():
    return render_template('Pedidos/verPedido.html')

@app.route('/pedidos/carrito')
def carrito():
    return render_template('Pedidos/Carrito.html')

@app.route('/Tarjetas')
def tarjetas():
    return render_template('Tarjeta/Tarjetas.html')

@app.route('/Tarjetas/new')
def nuevaTarjeta():
    return render_template('Tarjeta/registrarTarjeta.html')

<<<<<<< HEAD
@app.route('/usuarios/error')
def error():
    return render_template('Usuarios/error.html')
=======
@app.route('/Error')
def carrito():
    return render_template('Usuarios/Error.html')
>>>>>>> a5951f41d4b815979e7f76f08c650ff7bbc97f2d

if __name__=='__main__':
    app.run(debug=True)