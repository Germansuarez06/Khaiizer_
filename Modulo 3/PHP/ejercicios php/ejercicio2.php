<?php
$pares = 0;
$impares = 0;

for ($i = 1; $i <= 50; $i++) {
    if ($i % 2 == 0) {
    } else {
        $impares++;
    }
}

echo "La cantidad de números pares en el rango es: " . $pares . "\n";
echo "La cantidad de números impares en el rango es: " . $impares;
?>