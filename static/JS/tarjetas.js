
function validar(){
  var cad=numeroTarjeta(document.getElementById("noTarjeta").value);

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


function numeroTarjeta(numero){

    if(numero.match(/^4\d{3}-?\d{3}-?\d{3}-?\d{3}$/)){
    return '';
    }
    else{
    return 'El numero debe cumplir el siguiente formato ####-###-###-###';
}

}
