let pantalla = document.getElementById('pantalla');

function agregarCaracter(caracter) {
  const texto = pantalla.value;
  const posicionCursor = pantalla.selectionStart;
  const nuevoTexto = texto.slice(0, posicionCursor) + caracter + texto.slice(posicionCursor);
  pantalla.value = nuevoTexto;
  const nuevaPosicion = posicionCursor + caracter.length;
  pantalla.setSelectionRange(nuevaPosicion, nuevaPosicion);
  pantalla.focus();
}

function agregarFuncionConParentesis(funcion) {
  const texto = pantalla.value;
  const posicionCursor = pantalla.selectionStart;
  const nuevoTexto = texto.slice(0, posicionCursor) + funcion + '()' + texto.slice(posicionCursor);
  pantalla.value = nuevoTexto;
  const nuevaPosicion = posicionCursor + funcion.length + 1;
  pantalla.setSelectionRange(nuevaPosicion, nuevaPosicion);

  pantalla.focus();
}

function limpiarPantalla() {
  pantalla.value = '';
}

function borrarUltimo() {
  pantalla.value = pantalla.value.slice(0, -1);
}

function calcularResultado() {
  try {
    let expresion = pantalla.value;

   
    expresion = expresion.replace(/cos\(/g, "Math.cos(");
    expresion = expresion.replace(/sin\(/g, "Math.sin(");
    expresion = expresion.replace(/tan\(/g, "Math.tan(");
    expresion = expresion.replace(/sqrt\(/g, "Math.sqrt(");
    expresion = expresion.replace(/log\(/g, "Math.log10(");
    expresion = expresion.replace(/ln\(/g, "Math.log(");
    expresion = expresion.replace(/exp\(/g, "Math.exp(");
    expresion = expresion.replace(/pow\(/g, "Math.pow(");

  
    expresion = expresion.replace(/Math\.cos\(([^)]+)\)/g, "Math.cos(($1)*Math.PI/180)");
    expresion = expresion.replace(/Math\.sin\(([^)]+)\)/g, "Math.sin(($1)*Math.PI/180)");
    expresion = expresion.replace(/Math\.tan\(([^)]+)\)/g, "Math.tan(($1)*Math.PI/180)");

    console.log("Evaluando:", expresion);

    pantalla.value = eval(expresion);
  } catch (e) {
    pantalla.value = 'Error';
  }
}