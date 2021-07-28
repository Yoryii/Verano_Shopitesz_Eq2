

function validar(){
  var cad=nombreCategoria(document.getElementById("nombre").value);

    var div=document.getElementById("notificaciones");
    if(cad!=''){
        div.innerHTML='<p>'+cad+'</p>';
        return false;
    }
    else{

    alert('Registrado con exito!');
    return true;

    }


}

function nombre(nombre){



   if(nombre.length < 2){

    return 'El nombre debe tener mínimo dos caracteres<br>';

   }
   else{


   return '';
   }

}

function nombreCategoria(nombre){
var name = /^[A-Z]+$/i
   var codigo=nombre.charCodeAt(0);
    if(nombre.length < 3){
    return 'El nombre debe tener más de 2 letras!';
    }
    else{
    if(name.test(nombre)==true && ((codigo>=65 && codigo<=90) || codigo==165)){
    return '';
    }
    return 'El nombre no debe tener numeros y debe comenzar con Mayuscula';
    }
}