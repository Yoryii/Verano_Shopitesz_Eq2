# GDU
from datetime import timedelta

from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from flask_bootstrap import Bootstrap
from Modelo.Dao import db, Usuario, Pedido, DetallePedido, Tarjetas, Categoria, Producto

# GDU
from flask_login import login_required, login_user, logout_user, current_user, LoginManager

app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user_shopitesz_Eq2:Hola.123@localhost/BD_Shopitesz_Eq2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Cl4v3'

# GDU
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'mostrar_login'
login_manager.login_message = '¡ Tu sesión expiró !'
login_manager.login_message_category = "info"


# GDU
@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=10)


# Rutas del sistema - inicio
# Página principal
@app.route('/')
def inicio():
    return render_template('principal.html')


# Login
@app.route('/login')
def mostrar_login():
    if current_user.is_authenticated:
        return render_template('principal.html')
    else:
        return render_template('Usuarios/login.html')


# GDU
@login_manager.user_loader
def cargar_usuario(id):
    return Usuario.query.get(int(id))


# GDU
@app.route("/Usuarios/validarSesion", methods=['POST'])
def login():
    correo = request.form['email']
    password = request.form['pwd']
    usuario = Usuario()
    user = usuario.validar(correo, password)
    if user != None:
        login_user(user)
        return render_template('principal.html')
    else:
        # flash('Nombre de usuario o contraseña incorrectos')
        return render_template('Usuarios/login.html', mensaje="Nombre de usuario o contraseña incorrectos")


# GDU
@app.route('/Usuarios/cerrarSesion')
@login_required
def cerrarSesion():
    logout_user()
    return redirect(url_for('mostrar_login'))


# GDU
@app.route('/Usuarios/verPerfil')
@login_required
def consultaPerfil():
    return render_template('Usuarios/editar.html')


# Rutas del sistema - fin

# Rutas de Yoryi - inicio

# Usuarios - inicio

@app.route('/usuarios/new')
def nuevoUsuario():
    if current_user.is_authenticated and not current_user.is_admin():
        return render_template('principal.html')
    else:
        return render_template('Usuarios/registrar.html')


@app.route('/usuarios/agregar', methods=['post'])
def agregarUsuario():
    # try:
    u = Usuario()
    u.nombreCompleto = request.form['nombre']
    u.direccion = request.form['direccion']
    u.telefono = request.form['telefono']
    u.email = request.form['email']
    u.password = request.form['password']
    u.tipo = request.values.get("tipo", "Comprador")
    u.estatus = 'Activo'
    u.agregar()
    # except:
    # print(error)
    return redirect(url_for('consultaUsuarios'))


@app.route('/usuarios')
def consultaUsuarios():
    if current_user.is_authenticated and current_user.is_admin():
        u = Usuario()
        return render_template('Usuarios/consultaUsuarios.html', usuarios=u.consultaGeneral())
    else:
        return render_template('principal.html')


@app.route('/usuarios/edit', methods=['post'])
def editarUsuario():
    if current_user.is_authenticated:
        u = Usuario()
        u.idUsuario = request.form['idUsuario']
        u.nombreCompleto = request.form['nombre']
        u.direccion = request.form['direccion']
        u.telefono = request.form['telefono']
        if current_user.is_authenticated and current_user.is_admin():
            u.email = request.form['email']
        u.password = request.form['password']
        if current_user.is_authenticated and current_user.is_admin():
            u.tipo = request.values.get("tipo", u.tipo)
        # u.estatus = 'Activo'
        if current_user.is_authenticated and current_user.is_admin():
            u.editar()
        else:
            u.editarLite(request.form['idUsuario'], request.form['nombre'], request.form['direccion'],
                         request.form['telefono'], request.form['password'])
        return redirect(url_for('consultaUsuarios'))
    else:
        return render_template('principal.html')


@app.route('/usuarios/<int:id>')
def consultaUsuario(id):
    if current_user.is_authenticated and (current_user.idUsuario == id or current_user.is_admin()):
        u = Usuario()
        return render_template('usuarios/editarUsuario.html', usuario=u.consultaIndividual(id))
    else:
        return render_template('principal.html')


@app.route('/usuarios/delete/<int:id>')
def eliminarUsuario(id):
    u = Usuario()
    u.idUsuario = id
    u.eliminacionLogica()
    return render_template('principal.html')


# Usuarios fin
# Pedidos - Inicio

@app.route('/pedidos')
def consultaPedidos():
    p = Pedido()
    if current_user.is_authenticated and current_user.is_admin():
        return render_template('Pedidos/consultaPedidos.html', pedidos=p.consultaGeneral())
    if current_user.is_authenticated and current_user.is_vendedor():
        return render_template('Pedidos/consultaPedidos.html', pedidos=p.consultaVendedor(current_user.idUsuario))
    if current_user.is_authenticated and current_user.is_comprador():
        return render_template('Pedidos/consultaPedidos.html', pedidos=p.consultaComprador(current_user.idUsuario))


# Pedidos - Fin

# DetallePedidos - Inicio

@app.route('/detallePedido/<int:id>')
def consultaDetallePedidos(id):
    d = DetallePedido()
    return render_template('Pedidos/consultaDetallePedidos.html', detallePedidos=d.consultaGeneral(id), ID=id)


# DetallePedidos - Fin

# Manejo de errores - INICIO
@app.errorhandler(404)
def error_404(e):
    return render_template('Errores/error_404.html'), 404


@app.errorhandler(500)
def error_500(e):
    return render_template('Errores/error_500.html'), 500


# Manejo de errores - FIN

# Rutas de Yoryi - fin


# Rutas de Pancho - inicio

@app.route('/pedidos/carrito')
def carrito():
    return render_template('pedidos/Carrito.html')


@app.route('/Tarjetas/new')
def nuevaTarjeta():
    return render_template('Tarjeta/registrarTarjeta.html')


@app.route('/usuarios/error')
def error():
    return render_template('Usuarios/error.html')


@app.route('/Tarjetas/editar', methods=['post'])
def editarTarjeta():
    Tar = Tarjetas()
    Tar.idTarjeta = request.form['idTarjeta']
    Tar.idUsuario = request.form['idUsuario']
    Tar.noTarjeta = request.form['noTarjeta']
    Tar.saldo = request.form['saldo']
    Tar.banco = request.form['banco']
    Tar.estatus = request.form['estatus']
    Tar.editar()
    return redirect(url_for('consultaTarjetas'))





@app.route('/Tarjetas/delete/<int:id>')
def eliminarTarjeta(id):
    Tar = Tarjetas()
    Tar.idTarjeta = id
    Tar.eliminar()
    return render_template('principal.html')

# CRUD Tarjetas

@app.route('/consultaTarjetas')
def consultaTarjetas():
    if current_user.is_authenticated and current_user.is_comprador():
        Tar = Tarjetas()
        return render_template('Tarjeta/consultaTarjetas.html', Tarjetas=Tar.consultaGeneral(current_user.idUsuario))
    else:
        return render_template('principal.html')


@app.route('/Tarjetas/agregar', methods=['post'])
def agregarTarjeta():
    if current_user.is_authenticated and current_user.is_comprador():
        Tar = Tarjetas()
        Tar.idUsuario = request.form['idUsuario']
        Tar.noTarjeta = request.form['noTarjeta']
        Tar.saldo = request.form['saldo']
        Tar.banco = request.form['banco']
        Tar.estatus = request.form['estatus']
        Tar.agregar()
        return redirect(url_for('consultaTarjetas'))
    else:
        return render_template('principal.html')


@app.route('/Tarjetas/<int:id>')
def consultaGeneral(id):
    if current_user.is_authenticated and current_user.is_comprador():
        Tar = Tarjetas()
        return render_template('Tarjetas/editarTarjeta.html', Tar=Tar.consultaIndividual(id))
    else:
        return render_template('principal.html')


# Rutas de Pancho - fin

# Rutas de JO - inicio

# Rutas CATEGORIAS------------------------------------------INICIO

@app.route('/categorias')
def categorias():
    c = Categoria()
    return render_template('Categorias/categorias.html', categorias=c.consultaGeneral())


@app.route('/categorias/new')
def nuevaCategoria():
    return render_template('Categorias/agregarCategoria.html')

@app.route('/categorias/agregar', methods=['post'])
def agregarCategoria():
    # try:
    c = Categoria()
    c.nombre = request.form['nombre']
    c.estatus = 'Activa'
    c.agregar()
    # except:
    # print(error)
    return redirect(url_for('categorias'))


@app.route('/categorias/edit', methods=['post'])
def editarCategoria():

        c = Categoria()
        c.idCategoria = request.form['idCategoria']
        c.nombre = request.form['nombre']

        c.editar()

        return redirect(url_for('categorias'))


@app.route('/categorias/<int:id>')
def consultaCategoria(id):

        c = Categoria()
        return render_template('categorias/editarCategoria.html', c=c.consultaIndividual(id))

@app.route('/categorias/delete/<int:id>')
def eliminarCategoria(id):
    c = Categoria()
    c.idCategoria = id
    c.eliminar()
    return render_template('principal.html')


# Rutas CATEGORIAS------------------------------------------FIN






#Rutas PRODUCTOS-------------------------------------------INICIO

@app.route('/productos')
def productos():
    p = Producto()
    return render_template('Productos/productos.html', productos=p.consultaGeneral())




@app.route('/productos/new')
def nuevoProducto():
    return render_template('Productos/agregarProducto.html')

@app.route('/productos/agregar', methods=['post'])
def agregarProducto():
    # try:
    p = Producto()
    p.idCategoria = request.form['idCategoria']
    p.nombre = request.form['nombre']
    p.descripcion = request.form['descripcion']
    p.precioVenta = request.form['precioVenta']
    p.existencia = request.form['existencia']
    p.estatus = 'Activo'
    p.agregar()
    # except:
    # print(error)
    return redirect(url_for('productos'))


@app.route('/productos/edit', methods=['post'])
def editarProducto():

        p = Producto()
        p.idProducto = request.form['idProducto']
        p.idCategorias = request.form['idCategoria']
        p.nombre = request.form['nombre']
        p.descripcion = request.form['descripcion']
        p.precioVenta = request.form['precioVenta']
        p.existencia = request.form['existencia']

        p.editar()

        return redirect(url_for('productos'))


@app.route('/productos/<int:id>')
def consultaProducto(id):

        p = Producto()
        return render_template('productos/editarProducto.html', p=p.consultaIndividual(id))

@app.route('/productos/delete/<int:id>')
def eliminarProducto(id):
    p = Producto()
    p.idProducto = id
    p.eliminar()
    return render_template('principal.html')

#Rutas PRODUCTOS--------------------------------------------FIN


# Rutas de JO - fin

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
