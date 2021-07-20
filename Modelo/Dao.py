from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,BLOB,Date,Float

#GDU
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

db=SQLAlchemy()

class Categoria(db.Model):
    __tablename__='Categorias'
    idCategoria=Column(Integer,primary_key=True)
    nombre=Column(String,unique=True)
    estatus=Column(String,nullable=False)
    imagen=Column(BLOB)

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self,id):
        return Categoria.query.get(id)

    def consultarImagen(self,id):
        return self.consultaIndividuall(id).imagen

    def agregar(self):
        db.session.add(self)
        db.session.commit()

    def editar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

#Parte de Yoryi - Inicio
#Usuarios - Inicio
class Usuario(UserMixin, db.Model):
    __tablename__ = 'Usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombreCompleto = Column(String)
    direccion = Column(String)
    telefono = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String(128))
    tipo = Column(String)
    estatus = Column(String, nullable=False)

    @property  # Implementa el metodo Get (para acceder a un valor)
    def password(self):
        raise AttributeError('El password no tiene acceso de lectura')

    @password.setter  # Definir el metodo set para el atributo password_hash
    def password(self, password):  # Se informa el password en formato plano para hacer el cifrado
        self.password_hash = generate_password_hash(password)

    def validarPassword(self,password):
        return check_password_hash(self.password_hash,password)

    #Definición de los métodos para el perfilamiento
    def is_authenticated(self):
        return True

    def is_active(self):
        if self.estatus=='Activo':
            return True
        else:
            return False
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.idUsuario

    def is_admin(self):
        if self.tipo=='Administrador':
            return True
        else:
            return False
    def is_vendedor(self):
        if self.tipo=='Vendedor':
            return True
        else:
            return False
    def is_comprador(self):
        if self.tipo=='Comprador':
            return True
        else:
            return False
    #Definir el método para la autenticacion
    def validar(self,email,password):
        usuario=Usuario.query.filter(Usuario.email==email).first()
        if usuario!=None and usuario.validarPassword(password) and usuario.is_active():
            return usuario
        else:
            return None

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self,id):
        return Usuario.query.get(id)

    def agregar(self):
        db.session.add(self)
        db.session.commit()

    def editar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        usuario = self.consultaIndividual(self.idUsuario)
        db.session.delete(usuario)
        db.session.commit()
    def editarLite(self, id, name, address, phone, pwd):
        u=self.consultaIndividual(id)
        u.nombreCompleto = name
        u.direccion = address
        u.telefono = phone
        u.password = pwd
        u.editar()
#Usuarios - Fin

#Pedidos - Inicio
class Pedido(db.Model):
    __tablename__ = 'Pedidos'
    idPedido = Column(Integer, primary_key=True)
    idComprador = Column(Integer)
    idVendedor = Column(Integer)
    idTarjeta = Column(Integer)
    fechaRegistro = Column(Date)
    fechaAtencion = Column(Date)
    fechaRecepcion = Column(Date)
    fechaCierre = Column(Date)
    total = Column(Float)
    estatus = Column(String, nullable=False)

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self,id):
        return Pedido.query.get(id)

    def agregar(self):
        db.session.add(self)
        db.session.commit()

    def editar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()
#Pedidos - Fin

#DetallePedidos - Inicio

class DetallePedido(db.Model):
    __tablename__ = 'DetallePedidos'
    idDetalle = Column(Integer, primary_key=True)
    idPedido = Column(Integer)
    idProducto = Column(Integer)
    precio = Column(Float)
    cantidadPedida = Column(Integer)
    cantidadEnviada = Column(Integer)
    cantidadAceptada = Column(Integer)
    cantidadRechazada = Column(Integer)
    subtotal = Column(Float)
    estatus = Column(String, nullable=False)
    comentario = Column(String)

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self,id):
        return DetallePedido.query.get(id)

    def agregar(self):
        db.session.add(self)
        db.session.commit()

    def editar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

#DetallePedidos - Fin

#Parte de Yoryi - Fin


#Parte de Francisco - Inicio

class Tarjetas(db.Model):
    __tablename__ = 'Tarjetas'
    idTarjeta = Column(Integer, primary_key=True)
    idUsuario = Column(Integer)
    noTarjeta = Column(Integer)
    saldo = Column(Float)
    banco = Column(String)
    estatus = Column(String, nullable=False)

    def consultaGeneral(self, id):
        return self.query.filter(Tarjetas.idUsuario==id).all()

    def consultaIndividual(self,id):
        return self.query.get(id)

    def agregar(self):
        db.session.add(self)
        db.session.commit()

    def editar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        usuario = self.consultaIndividual(self.idUsuario)
        db.session.delete(usuario)
        db.session.commit()




#Parte de Francisco - Fin


class Producto(db.Model):
    __tablename__='Producto'
    idProducto=Column(Integer,primary_key=True)
    idCategoria=Column(Integer)
    nombre=Column(String,unique=True)
    descripcion=Column(String,nullable=False)
    precioVenta=Column(Float, nullable=False)
    existencia=Column(Integer, nullable=False)
    foto=Column(BLOB)
    especificaciones=Column(BLOB)
    estatus=Column(String,nullable=False)


    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self,id):
        return Categoria.query.get(id)

    def consultarImagen(self,id):
        return self.consultaIndividuall(id).imagen

    def agregar(self):
        db.session.add(self)
        db.session.commit()

    def editar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()


