let EdadUsuario = Number(prompt("ingrese su edad: "));
let TieneTicket = Boolean(prompt("Tiene ticket?: "));

true == "si"
false == "no"

if (EdadUsuario >= 18 && TieneTicket) {
    mensaje = "acceso concedido"
}
else {
    mensaje = "acceso denegado"
}
console.log(`${mensaje}`)