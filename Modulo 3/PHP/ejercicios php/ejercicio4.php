<?php
    $num = null;
    $intento = 1;
    $numsecreto = 21
    while ($num != $numsec)
    $numero = readline("ingrese un numero del 1 al 100: ")
    if ($num == $numsec){
        echo "haz adivinado el numero secreto"
        break;
    } else {
        echo "no es el numero, intentalo otra vez"
        echo "intentos restantes: " . $intento . "\n"
        $intento+=1
    }
    if ($intento==6){
        break;
    }
?>