function nombreCategoria(){

 var nombre = document.getElementById("nombre").value;

   if(nombre.length < 2){

   alert('!');
return 'El nombre debe tener mínimo dos caracteres<br>';
   
   }
   else{


   return '';
   }

}