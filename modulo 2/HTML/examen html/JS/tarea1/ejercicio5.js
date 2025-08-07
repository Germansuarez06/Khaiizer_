let edad = prompt("¿Cuál es tu edad?: ");
edad = Number(edad);
let Rango = edad >= 18 && edad <= 64;
console.log(Rango);

if (Rango) {
    console.log("Estas en el rango");
} else {
    console.log("No estas en el rango");
}

//este es un ejercicio que estoy haciendo despues
//por eso estoy aplicando el if y else
