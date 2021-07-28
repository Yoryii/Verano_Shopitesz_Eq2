function eliminarUsuario(id,nombre){
    if(confirm('¿Estás seguro de eliminar el usuario '+nombre+'?'))
        location.href='/usuarios/delete/'+id;
}

function eliminarDetalle(id){
    if(confirm('¿Estás seguro de eliminar el detalle '+id+'?'))
        location.href='/detallePedidos/delete/'+id;
}

function eliminarPedido(id){
    if(confirm('¿Estás seguro de eliminar el pedido '+id+'?'))
        location.href='/pedidos/delete/'+id;
}

function eliminarCesta(id){
    if(confirm('¿Estás seguro de eliminar la cesta?'))
        location.href='/cesta/delete/'+id;
}

function eliminarTarjeta(id){
    if(confirm('¿Estás seguro de eliminar la tarjeta ' +id+ '?'))
        location.href='/Tarjetas/delete/'+id;
}