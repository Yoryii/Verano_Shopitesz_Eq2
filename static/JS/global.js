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