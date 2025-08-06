let numeroSecreto = parseInt(prompt("Escribe un número del 1 al 10:"));

let intento = 0;
let intentosRealizados = 0;

while (intento !== numeroSecreto) {
  intento = Math.floor(Math.random() * 10) + 1;  
  intentosRealizados++;
  console.log("Intento " + intentosRealizados + ": " + intento);
}

console.log("¡Lo adiviné! Era el número " + numeroSecreto + " y me tomó " + intentosRealizados + " intentos.");

// Explicacion de este ejercicio es que utilizamos la formula matematica math.random que genera un numero entre 0 y 1
// despues lo multiplicamos por 10 para que genere un numero entre 0 y 9, despues lo sumamos con 1 para que ahi si quede entre 1 y 10
// el math.floor esta para redondear el numero pero este lo que hace es redondearlo hacia abajo 3.49 = 3; 9.99 = 9
// explicacion rapida porque tuve que investigar como hacer este ejercicio bien :D