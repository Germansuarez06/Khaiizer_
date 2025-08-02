const numeroTabla = Number(prompt("Ingrese un numero del 1 al 10: " ));
console.log(`la tabla de mutiblicar ${numeroTabla} ---`);

for (let i = 1; i <= 10; i++) {
    // i es el contador, empieza en 1, se ejecuta mientras sea <= 10, y aumenta en 1 en cada iteración.
    const resultado = numeroTabla * i;
    console.log(`${numeroTabla} x ${i} = ${resultado}`);
}