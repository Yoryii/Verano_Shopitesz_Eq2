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
def carrito():
    return render_template('Tarjeta/Tarjetas.html')

@app.route('/Tarjetas/new')
def carrito():
    return render_template('Tarjeta/registrarTarjeta.html')

if __name__=='__main__':
    app.run(debug=True)