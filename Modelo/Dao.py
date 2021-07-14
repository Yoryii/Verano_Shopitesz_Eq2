from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,BLOB,Date,Float

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
class Usuario(db.Model):
    __tablename__ = 'Usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombreCompleto = Column(String)
    direccion = Column(String)
    telefono = Column(String)
    email = Column(String, unique=True)
    contrasena = Column(String)
    tipo = Column(String)
    estatus = Column(String, nullable=False)

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
        db.session.delete(self)
        db.session.commit()
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

#Parte de Yoryi - Fin
