let mes = prompt("Inserta un Mes del año")
let estacion;

switch (mes.toLowerCase()) {
  case "diciembre":
  case "enero":
  case "febrero":
    estacion = "Invierno";
    break;

  case "marzo":
  case "abril":
  case "mayo":
    estacion = "Primavera";
    break;

  case "junio":
  case "julio":
  case "agosto":
    estacion = "Verano";
    break;

  case "septiembre":
  case "octubre":
  case "noviembre":
    estacion = "Otoño";
    break;

  default:
    estacion = "Mes no válido";
}

console.log(`El mes de ${mes} pertenece a la estación: ${estacion}`);