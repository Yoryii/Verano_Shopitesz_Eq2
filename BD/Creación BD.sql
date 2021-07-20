create database BD_Shopitesz_Eq2;
use BD_Shopitesz_Eq2;

/*drop database BD_Shopitesz_Eq2;
drop user 'user_shopitesz_Eq2';*/

/*Tablas*/
create table Usuarios
(
idUsuario int auto_increment not null,
nombreCompleto varchar(60) not null,
direccion varchar(200) not null,
telefono char(12) not null,
email varchar(100) not null,
password_hash varchar(128) not null,
tipo varchar(15) not null,
estatus varchar(10) not null,
constraint pk_usuarios primary key (idUsuario),
constraint uk_usuarios unique (email),
constraint chk_usuarios check (estatus in('Activo','Inactivo'))
);

create table Categorias(
	idCategoria int auto_increment not null,
    nombre varchar(60) not null,
    imagen mediumblob null,
    estatus varchar(10) not null,
    constraint pk_categorias primary key(idCategoria),
    constraint uk_nombre_categoria unique (nombre),
    constraint chk_categorias check (estatus in('Activa','Inactiva'))
);

create table Productos(
	idProducto int auto_increment not null,
    idCategoria int not null,
    nombre varchar(100) not null,
    descripcion varchar(200) not null,
    precioVenta float not null,
    existencia int not null,
    foto mediumblob null,
    especificaciones mediumblob null,
    estatus varchar(10) not null,
    constraint pk_productos primary key(idProducto),
    constraint uk_nombre_producto unique (nombre),
    constraint chk_productos check (estatus in('Activo','Inactivo'))
);

create table Carrito(
	idCarrito int auto_increment not null,
    idUsuario int not null,
    idProducto int not null,
    fecha date not null,
    cantidad int not null,
    estatus varchar(10) not null,
    constraint pk_carrito primary key(idCarrito),
    constraint chk_carrito check (estatus in('Activo','Inactivo'))
);

create table Tarjetas(
	idTarjeta int auto_increment not null,
    idUsuario int not null,
    noTarjeta varchar(16) not null,
    saldo float not null,
    banco varchar(50) not null,
    estatus varchar(10) not null,
    constraint pk_tarjetas primary key(idTarjeta),
    constraint uk_noTarjeta unique (noTarjeta),
    constraint chk_tarjetas check (estatus in('Activa','Inactiva'))
);

create table Pedidos(
	idPedido int auto_increment not null,
    idComprador int not null,
    idVendedor int not null,
    idTarjeta int not null,
    fechaRegistro date,
    fechaAtencion date,
    fechaRecepcion date,
    fechaCierre date,
    total float,
    estatus varchar(10) not null,
    constraint pk_pedidos primary key(idPedido)
);

create table DetallePedidos(
	idDetalle int auto_increment not null,
    idPedido int not null,
    idProducto int not null,
    precio float not null,
    cantidadPedida int not null,
    cantidadEnviada int,
    cantidadAceptada int,
    cantidadRechazada int,
    subtotal float,
    estatus varchar(10) not null,
    comentario varchar(200),
    constraint pk_detallepedidos primary key(idDetalle)
);

/*Claves foraneas*/

alter table DetallePedidos add constraint detallePedidos_pedidos_fk foreign key (idPedido) references Pedidos(idPedido);
alter table DetallePedidos add constraint detallePedidos_productos_fk foreign key (idProducto) references Productos(idProducto);
alter table Pedidos add constraint pedidos_usuarioComprador_fk foreign key (idComprador) references Usuarios(idUsuario);
alter table Pedidos add constraint pedidos_usuarioVendedor_fk foreign key (idVendedor) references Usuarios(idUsuario);
alter table Pedidos add constraint pedidos_tarjetas_fk foreign key (idTarjeta) references Tarjetas(idTarjeta);
alter table Tarjetas add constraint tarjetas_usuarios_fk foreign key (idUsuario) references Usuarios(idUsuario);
alter table Carrito add constraint carrito_usuarios_fk foreign key (idUsuario) references Usuarios(idUsuario);
alter table Carrito add constraint carrito_productos_fk foreign key (idProducto) references Productos(idProducto);
alter table Productos add constraint productos_categorias_fk foreign key (idCategoria) references Categorias(idCategoria);

/*Mostrar tablas*/
show tables;
select*from categorias
update usuarios set tipo='Administrador'
 where idUsuario=2;
 
 insert into Categorias (idCategoria, nombre, imagen, estatus) values(1, 'Electronicos', null, 'Activo')

/*Usuarios y permisos para conexión*/
create user user_shopitesz_Eq2 identified by 'Hola.123';
grant select,insert,update,delete on BD_Shopitesz_Eq2.Categorias to user_shopitesz_Eq2;
grant select,insert,update,delete on BD_Shopitesz_Eq2.Productos to user_shopitesz_Eq2;
grant select,insert,update,delete on BD_Shopitesz_Eq2.Carrito to user_shopitesz_Eq2;
grant select,insert,update,delete on BD_Shopitesz_Eq2.Usuarios to user_shopitesz_Eq2;
grant select,insert,update,delete on BD_Shopitesz_Eq2.Tarjetas to user_shopitesz_Eq2;
grant select,insert,update,delete on BD_Shopitesz_Eq2.Pedidos to user_shopitesz_Eq2;
grant select,insert,update,delete on BD_Shopitesz_Eq2.DetallePedidos to user_shopitesz_Eq2;