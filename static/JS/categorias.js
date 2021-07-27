function nombreCategoria(){

 var nombre = document.getElementById("nombre").value;

   if(nombre == ''){

   alert('No se ingreso ningun nombre!');

   return false;
   }
   else{

   alert('El nombre es: '+nombre);
   return true;
   }

}