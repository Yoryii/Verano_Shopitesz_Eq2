function imprimirMsg(){
    alert('Se hizo click');
}




function prueba(){

   var nombre = document.getElementById("nombre").value;

   if(nombre == ''){

   alert('No se ingreso ningun nombre!');

   return false;
   }

}


//Metodo de pruba de validacion de usuarios


function validarPrueba(){

    var cad=validarPassword(document.getElementById("password").value);
    cad+=passwordRobusto(document.getElementById("password").value,document.getElementById("password").value);
  // cad+=validarPasswords(form.password.value,form.passwordConfirmacion.value)
    cad+=validarTelefono(document.getElementById("telefono").value);
    cad+=nombreApellido(document.getElementById("nombre").value);
    var div=document.getElementById("notificaciones");
    if(cad!=''){
        div.innerHTML='<p>'+cad+'</p>';

        return false;
    }
    else{
        alert("Usuario registrado con exito!!");
        return true;
    }

}


function validar(form){

    var cad=validarPassword(form.password.value);
    cad+=passwordRobusto(form.password.value,form.password.value);
  // cad+=validarPasswords(form.password.value,form.passwordConfirmacion.value)
    cad+=validarTelefono(form.telefono.value);
    var div=document.getElementById("notificaciones");
    if(cad!=''){
        div.innerHTML='<p>'+cad+'</p>';
        alert("false");
        return false;
    }
    else{
        alert("true");
        return true;
    }

}
function validarPassword(pwd){
    if(pwd.length<8){
        return 'El password debe ser de al menos 8 caracteres<br>';
    }
    else{
        return '';
    }
}

function validarPasswords(pwd1,pwd2){
    if(pwd1!=pwd2){
        return 'Los password no coinciden<br>';
    }
    else{
        return '';
    }
}
function verPasswords(){
    var check=document.getElementById("verPassword");
    if(check.checked){
        document.getElementById("password").setAttribute('type','text')
        document.getElementById("passwordConfirmacion").setAttribute('type','text')
    }
    else{
        document.getElementById("password").setAttribute('type','password')
        document.getElementById("passwordConfirmacion").setAttribute('type','password')
    }
}
function passwordRobusto(pwd){
    var banNumero=false,banMin=false,banMay=false,banCarEs=false;
    banNumero=tieneNumero(pwd);
    banMin=tieneLetraMinuscula(pwd);
    banMay=tieneLetraMayuscula(pwd);
    banCarEs=tieneCaracterEspecial(pwd);
    if(banNumero && banMin && banMay && banCarEs)
        return '';
    else
        return 'El password debe tener al menos un digito,<br> una mayuscula, una minuscula y al menos un caracter especial.<br>'
}
function tieneNumero(cadena){
    var bandera=false;
    for(i=0;i<cadena.length;i++){
        var codigo=cadena.charCodeAt(i);
        if(codigo>=48 && codigo<=57){
            bandera=true;
            break;
        }
    }
    return bandera;
}
function tieneLetraMinuscula(cadena){
    var bandera=false;
    for(i=0;i<cadena.length;i++){
        var codigo=cadena.charCodeAt(i);
        if((codigo>=97 && codigo<=122) || codigo==164){
            bandera=true;
            break;
        }
    }
    return bandera;
}
function tieneLetraMayuscula(cadena){
    var bandera=false;
    for(i=0;i<cadena.length;i++){
        var codigo=cadena.charCodeAt(i);
        if((codigo>=65 && codigo<=90)|| codigo==165){
            bandera=true;
            break;
        }
    }
    return bandera;
}
function tieneCaracterEspecial(cadena){
    var bandera=false;
    for(i=0;i<cadena.length;i++){
        var codigo=cadena.charCodeAt(i);
        if((codigo>=32 && codigo<=47)||(codigo>=58 &&codigo<=64)||(codigo>=91 && codigo<=96)||(codigo>=123 &&codigo<=126)|| codigo==173 || codigo==168){
            bandera=true;
            break;
        }
    }
    return bandera;
}
function validarTelefono(cadena){
    var patron=/\d{3}-\d{3}-\d{4}/;
    if(patron.test(cadena)==true){
        return '';
    }
    else{
        return 'El numero telefonico debe tener el siguiente formato ###-###-####,<br> donde el # representa un numero del 0-9<br>';
    }
}



//Metodos Jose Angel
function nombreApellido(nombre){
var name = /^[A-Z]+$/i
   var codigo=nombre.charCodeAt(0);
    if(nombre.length < 2){
    return 'Tu nombre debe tener m??s de 1 letra';
    }
    else{
    if(name.test(nombre)==true && ((codigo>=65 && codigo<=90) || codigo==165)){
    return '';
    }
    return 'Tu nombre no debe tener numeros y debe comenzar con Mayuscula';
    }
}