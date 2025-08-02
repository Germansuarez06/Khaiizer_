let num = Number(prompt("Ingrese su edad: "))

if (num >= 18) {
  mensaje = "Perfecto, eres mayor de edad";
} else {
  mensaje = "Lo siento, no eres mayor de edad";
}

console.log(`${mensaje}`);