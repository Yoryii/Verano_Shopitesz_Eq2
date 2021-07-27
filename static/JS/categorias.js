

function validar(){
  var cad=nombreCategoria(document.getElementById("nombre").value);

    var div=document.getElementById("notificaciones");
    if(cad!=''){
        div.innerHTML='<p>'+cad+'</p>';
        return false;
    }
    else{

    alert('Si se pudo');
    return true;

    }


}

function nombreCategoria(nombre){



   if(nombre.length < 2){

    return 'El nombre debe tener mínimo dos caracteres<br>';

   }
   else{


   return '';
   }

}