
//VALIDACIONES JO---------------------------------------------------------------------------------


function validar(){
  var cad=nombreProducto(document.getElementById("nombre").value;);
 //  cad+=passwordRobusto(document.getElementById("password"),document.getElementById("password"));

    var div=document.getElementById("notificaciones");
    if(cad!=''){
        div.innerHTML='<p>'+cad+'</p>';

        return false;
    }
    else{

        return true;
    }
}


function nombreProducto(nombre){
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
}}