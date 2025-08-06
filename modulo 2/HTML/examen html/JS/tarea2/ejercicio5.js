let montocompra = Number(prompt("Ingrese su monto: "))

if (montocompra >= 100)  {
    descuento_aplicado = 0.20
    mensaje = "Hemos aplicado el 20% de descuento"
} else if (montocompra > 50 && montocompra < 100) {
    descuento_aplicado = 0.10
    mensaje = "Hemos aplicado el descuento"
} else {
    mensaje = "Sin descuento"
    descuento_aplicado = 0
}

let precio_final = montocompra - (montocompra * descuento_aplicado)

console.log(mensaje)
console.log(precio_final)

