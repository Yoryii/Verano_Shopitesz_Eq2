from flask import Flask, render_template, request,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from Modelo.Dao import db, Usuario, Pedido, DetallePedido
app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://user_shopitesz_Eq2:Hola.123@localhost/BD_Shopitesz_Eq2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='Cl4v3'
#Rutas del sistema - inicio
#Página principal
@app.route('/')
def inicio():
    return render_template('principal.html')

#Login
@app.route('/login')
def login():
    return render_template('Usuarios/login.html')

#Rutas del sistema - fin

#Rutas de Yoryi - inicio

#Usuarios - inicio

@app.route('/usuarios/new')
def nuevoUsuario():
    return render_template('Usuarios/registrar.html')

@app.route('/usuarios/agregar',methods=['post'])
def agregarUsuario():
    #try:
    u = Usuario()
    u.nombreCompleto=request.form['nombre']
    u.direccion = request.form['direccion']
    u.telefono = request.form['telefono']
    u.email = request.form['email']
    u.contrasena = request.form['password']
    u.tipo = 'Comprador'
    u.estatus='Activo'
    u.agregar()
    #except:
    print(error)
    return redirect(url_for('consultaUsuarios'))

@app.route('/usuarios')
def consultaUsuarios():
    u = Usuario()
    return render_template('Usuarios/consultaUsuarios.html', usuarios=u.consultaGeneral())

@app.route('/usuarios/edit')
def editarUsuario():
    return render_template('Usuarios/editarUsuario.html')

#Usuarios fin
#Pedidos - Inicio

@app.route('/pedidos')
def consultaPedidos():
    p = Pedido()
    return render_template('Pedidos/consultaPedidos.html', pedidos=p.consultaGeneral())

#Pedidos - Fin

#DetallePedidos - Inicio

@app.route('/detallePedidos')
def consultaDetallePedidos():
    d = DetallePedido()
    return render_template('Pedidos/consultaDetallePedidos.html', detallePedidos=d.consultaGeneral())

#DetallePedidos - Fin

#Rutas de Yoryi - fin

#Rutas de Pancho - inicio

@app.route('/pedidos/carrito')
def carrito():
    return render_template('pedidos/Carrito.html')

@app.route('/Tarjetas')
def tarjetas():
    return render_template('Tarjeta/Tarjetas.html')

@app.route('/Tarjetas/new')
def nuevaTarjeta():
    return render_template('Tarjeta/registrarTarjeta.html')

@app.route('/usuarios/error')
def error():
    return render_template('Usuarios/error.html')

#Rutas de Pancho - fin

#Rutas de JO - inicio

#Rutas CATEGORIAS------------------------------------------INICIO

@app.route('/categorias')
def categorias():
    return render_template('Categorias/categorias.html')

@app.route('categorias/new')
def nuevaCategoria():
    return render_template('Categorias/agregarCategoria.html')


#Rutas CATEGORIAS------------------------------------------FIN


@app.route('/productos')
def productos():
    return render_template('Productos/productos.html')
#Rutas de JO - fin

if __name__=='__main__':
    db.init_app(app)
    app.run(debug=True)