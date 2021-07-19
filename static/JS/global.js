function eliminarUsuario(id,nombre){
    if(confirm('¿Estás seguro de eliminar el usuario '+nombre+'?'))
        location.href='/usuarios/delete/'+id;
}