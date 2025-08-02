let numero1 = Number(prompt("Ingrese un numero: "));
let numero2 = Number(prompt("Ingrese otro numero: "));

if (numero1>numero2) {
    mensaje = `el ${numero1} es mayor al numero ${numero2}`
}
else if (numero1<numero2) {
    mensaje = `El numero ${numero2} es mayor al numero ${numero1}`
}
else {
    mensaje = `los numeros son iguales`
}
console.log(`${mensaje}`)