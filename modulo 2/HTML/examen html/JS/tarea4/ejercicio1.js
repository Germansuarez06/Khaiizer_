const numeroTabla = Number(prompt("Ingrese un numero del 1 al 10: " ));
console.log(`la tabla de mutiblicar ${numeroTabla} ---`);

for (let i = 1; i <= 10; i++) {
    const resultado = numeroTabla * i;
    console.log(`${numeroTabla} x ${i} = ${resultado}`);
}