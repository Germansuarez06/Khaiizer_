let semaforo = prompt("Ingrese un color del semaforo: ")

if (semaforo == "verde") {
    mensaje = "Puedes pasar"
}
else if (semaforo == "amarillo") {
    mensaje = "Ten cuidado, pero puedes pasar"
}
else if (semaforo == "rojo") {
    mensaje = "Ten cuidado, esta en rojo, no puedes pasar"
}
else {
    mensaje = "color no invalido"
}
console.log(`${mensaje}`)
