opcion = input("""
        ──────────────────────────────────────────────
                   UNA NOCHE DE INVIERNO            
        ──────────────────────────────────────────────
      Es una fría noche de invierno.           
      Tú y tus tres amigos —Fernando, María y Humberto—
      han decidido emprender una aventura hacia un peculiar destino: el Hotel Brisas del Mar.
      Un lugar escondido en medio de la nada. Aunque su ubicación es cuestionable,
      las reseñas prometen una experiencia inolvidable.\n
      La carretera se extiende silenciosa y solitaria frente a ustedes,
      cuando de pronto... ¡un golpe seco sacude la camioneta!
      Algo ha impactado fuertemente el vehículo, y este comienza a fallar.
      El motor tose, las luces parpadean.
               
      Tienes que decidir rápido.
               
      ¿Qué harás?
      1° (REVISAR)
      2° (SEGUIR)

      - Escribe tu numero de la opcion   
      : """).strip().upper()

if opcion == "SEGUIR":
    print("""
            ──────────────────────────────────────────────
                   DECISIÓN: SEGUIR ADELANTE         
            ──────────────────────────────────────────────
    Deseando que todo haya sido solo un fallo momentáneo,
    decides continuar el camino con la esperanza de llegar a salvo al hotel.
                   
    Algo dentro de ti te dice que no es buena idea detenerse en ese lugar tan solitario,
    Pero no pasa mucho tiempo cuando la camioneta finalmente se rinde.
    El motor se apaga por completo, las luces se extinguen y el silencio de la noche se vuelve más pesado.
    Están varados, en medio de la nada, y lo peor... sin señal para pedir ayuda.
    Tus amigos entran en pánico. María revisa su teléfono una y otra vez sin éxito.
    Fernando maldice por lo bajo. Humberto mira alrededor con preocupación.
    A lo lejos, entre los árboles y la niebla, puedes distinguir las luces del hotel.
    No está tan lejos, pero el camino es oscuro y apartado.
                   
      ¿Qué decides hacer?""")
    choice = input("""
          🔧 1° (bajarte)
          🚶 2° (caminar)
                   
            - Escribe tu numero de la opcion
            : """).strip().lower()
    if choice == "1" or choice == "bajarte":
        print("""    
        ──────────────────────────────────────────────
                 CAMINATA DESESPERADA Y SOSPECHA     
        ──────────────────────────────────────────────
      Al bajarse e intentar arreglar la camioneta, se dan cuenta de algo terrible:
      el vehículo ha sido forzado hasta el punto de no tener salvación.
      El motor está muerto. Pero aún así, siguen intentando. Sabes que tu vida está en juego.
      En medio del esfuerzo, al mirar a lo lejos, divisas una pequeña estación de guardabosques.
      Apenas una cabaña de madera, lo justo para que viva una sola persona.
      Una oportunidad.
                                       
      Decides correr hacia ella, dejando a tus amigos cuidando la camioneta.
      El aire es frío, el bosque silencioso, y el miedo te corre por las venas.
      Llegas jadeando, con el corazón latiendo a mil por hora
      Golpeas la puerta desesperadamente, y entonces… se abre.
      Un hombre aparece. El guardabosques.
              
      Por un momento, una sensación de seguridad te invade. Estás a salvo… ¿o no?
      Al mirarlo a los ojos, algo no cuadra.
      Su expresión es fría. Su mirada vacía. Te transmite una inquietante sensación de desconfianza.
      Tu instinto te grita que algo no está bien.""")
        
        OpDentroDelChoice = (input("""
            ¿Qué harás?
                                    
       1° (Inventar)
       2° (Honestidad)
                                   
        - Escribe tu numero de la opcion
                                    
        """)).strip().upper()
        if OpDentroDelChoice == "inventar":
            print("""  
                Decides inventar una historia al guardabosques, sabiendo que es ilegal, pero la desconfianza te obliga a intentarlo. 
                Le dices que vienen del Hotel Brisas del Norte, no muy lejos de su estación, y que buscan ayuda para reportar un robo ocurrido en la instalación.
                El guardabosques se ríe y comenta con sorna:
                "Me sorprende que alguien venga de ahí. Ese edificio lleva años cerrado."
                Al notar que cometiste un error, intentas arreglar el malentendido, pero es demasiado tarde. De repente, el guardabosques te arrastra hacia su cabaña y te secuestra.
                El guardabosques sale en busca de los demás...
                
                  🔻 Fin del juego.
                  """)
        elif OpDentroDelChoice == "honestidad":
            print("""
        A pesar de la desconfianza, decides confiar y contarle la verdad al guardabosques.
        Él, con una sonrisa irónica y tono burlón, responde:
        "Oh, qué trágica historia..."
        El guardabosques se dirige hacia su garaje para buscar algo, mientras tú aprovechas el momento para escapar. Corres a toda prisa hacia donde están tus amigos, 
        queriendo asegurarte de que estén bien.
        Al contarles lo sucedido, todos deciden que la mejor opción es correr hacia el hotel, el único lugar cercano que podría ofrecer seguridad... 
        aunque sigue siendo toda una incógnita.
        Al llegar, un hombre algo extraño y excéntrico los recibe, dándoles la bienvenida al Hotel Brisas del Norte y los invita a pasar.
        """)
        else:
            print("Respuesta Incorrecta, Escriba la correcta")
        otrochoice = "juntos" or "separados"
        
        print("""
            Al cruzar la puerta, el aire cambia. El ambiente está cargado de una energía extraña.
            La decoración parece sacada de otra época: candelabros oxidados, alfombras raídas y cuadros cuyos ojos parecen seguirte.
            El recepcionista —el hombre excéntrico— los observa sin parpadear y dice en voz baja:
            "Aquí están... Los estábamos esperando."
            Tus amigos se miran entre sí, dudando, pero deciden seguirte hasta una habitación amplia con cuatro camas.
            La puerta se cierra sola con un crujido seco. Y ahí, el juego comienza...
                              
                                """)
        input("""
            ¿Qué deciden hacer?
                  1° juntos
                  2° separados

                - Escribe el nuero de la opcion
                  """).strip().lower()
        if otrochoice == "2" or otrochoice == "separados":
                 print("""
        María, algo inquieta, propone revisar el hotel para encontrar una salida alternativa.
        Fernando está de acuerdo, pero tú y Humberto prefieren quedarse juntos.
        La tensión entre ustedes se rompe y, en un impulso, deciden separarse para avanzar más rápido.

        Grave error.

        Apenas se dispersan, el hotel parece despertar. Las paredes susurran, las sombras se alargan.
        Una figura espectral empieza a seguirlos... uno por uno. Nadie puede verla al estar solo.
        Gritos. Puertas que se cierran. Pasillos que cambian de forma. El espíritu los atrapa,
        alimentándose de su miedo, atrapándolos para siempre entre los muros de Brisas del Norte.

El hotel vuelve al silencio... esperando a su próximo huésped.

 FIN DEL JUEGO  Final Malo
 Nunca debieron separarse.
                  """)
        elif otrochoice == "1" or otrochoice == "juntos":
                print("""
    Aunque el miedo los domina, los cuatro deciden quedarse juntos.
    Usan el mapa que aún tienen en el teléfono para explorar el hotel sin separarse ni un segundo.
    Cada rincón parece tener ojos, pero también pistas... una trampilla oculta en la cocina,
    una llave antigua detrás de un espejo, y finalmente: una salida secreta hacia el bosque.

    Justo cuando el espíritu del hotel intenta atraparlos en el salón principal,
    logran abrir la puerta oculta y escapar. Corren sin mirar atrás hasta encontrar una carretera,
    donde una patrulla forestal pasa casualmente y los rescata.

    Desde ese día, nadie ha podido localizar el Hotel Brisas del Norte.
    Solo queda su historia, contada por cuatro sobrevivientes que nunca se separaron.
                  """)
        else:
                print("Respuesta Incorrecta, Escriba la correcta")
    
            
    
            

                
    elif choice == "caminar":
         print("""
                ──────────────────────────────────────────────

                        ENTRE LOS CUATRO DECIDEN
               
                ──────────────────────────────────────────────

                Entre los cuatro, deciden dejar la camioneta atrás y partir a pie hacia el hotel.  
                La esperanza de encontrar ayuda y no quedarse varados en medio de la carretera  
                los impulsa a avanzar, aunque el camino frente a ellos sea oscuro y desconocido.
            """)
         dentrodeunchoice = input("""
            _____________________
            
            ENTRADA AL HOTEL                     
            _____________________
            
            Entraste al hotel y te diriges al receptor, ¿Habitaciones?...
            
            ¿Que le dices?
                                
            1° (una)
            2° (cuatro)
                                  
            - Escribe tu numero de la opcion
                                
            : """).strip().lower()
    else :print("Respuesta Incorrecta, Escriba la correcta")

    if dentrodeunchoice == "una":
             print("""
                Deciden tomar una habitación para todos, desconcertados por lo que podría pasarles si se separan.
                Cada uno traza un plan:
                Humberto vigilará los alrededores.
                Fernando y María buscarán la manera de pedir ayuda.
                Germán explorará el hotel en busca de una posible vía de escape.
                Justo antes de salir, recuerdan que en sus teléfonos tienen un mapa del hotel, resultado de una investigación previa.
                El plan está listo: reconocimiento, pedido de ayuda y la seguridad de poder salir en cualquier momento.
                Pero justo cuando todo parece bajo control, la electricidad falla abruptamente y la oscuridad envuelve cada rincón del hotel.
                Un frío glacial inunda el ambiente, y un silencio sepulcral se apodera del lugar.
                De entre las sombras, surge una presencia indescriptible: un espíritu antiguo y vengativo, cuyas formas son difusas y cambiantes, como si estuviera hecho de sombras y susurros.
                Este ente no es simplemente un espectro; es una entidad que se alimenta del miedo y la soledad, y ataca a cada uno por separado, buscando quebrar su unión y sembrar el caos.
                El espíritu se desliza por los pasillos con un sonido que parece un suspiro lejano, sus ojos brillan con un fuego espectral que hiela la sangre.
                Sin embargo, gracias a su pacto silencioso de nunca separarse, los cuatro logran esquivar sus ataques y mantenerse unidos, atravesando el laberinto oscuro del hotel.
                Finalmente, después de momentos que parecen eternos, consiguen salir al amanecer, encontrando ayuda y dejando atrás esa pesadilla.
                   
                   FINAL (SOBREVIVENCIA)
                   """)
    elif dentrodeunchoice == "cuatro":
             print("""
        Aunque el miedo los domina, los cuatro deciden quedarse juntos.
        Usan el mapa que aún tienen en el teléfono para explorar el hotel sin separarse ni un segundo.
        Cada rincón parece tener ojos, pero también pistas... una trampilla oculta en la cocina,
        una llave antigua detrás de un espejo, y finalmente: una salida secreta hacia el bosque.

        Justo cuando el espíritu del hotel intenta atraparlos en el salón principal,
        logran abrir la puerta oculta y escapar. Corren sin mirar atrás hasta encontrar una carretera,
        donde una patrulla forestal pasa casualmente y los rescata.

        Desde ese día, nadie ha podido localizar el Hotel Brisas del Norte.
        Solo queda su historia, contada por cuatro sobrevivientes que nunca se separaron.

        FIN DEL JUEGO  Final Bueno
        La unión los salvó.
""")
    else:
             print("Respuesta incorrecta, elige bien su respuesta")

         
         
        
elif opcion == "REVISAR":
        print("""
      ──────────────────────────────────────────────
          
                  ESCENA FINAL - CAMINO FATAL 
                
      ──────────────────────────────────────────────
          
      Decides detenerte. No hay marcha atrás.
      Aunque el miedo se siente en el ambiente como una sombra invisible,
      sabes que ya estás en esto. Solo queda arreglar la camioneta lo más rápido posible.
      Los cuatro se bajan. Humberto y tú (Germán) se quedan revisando el motor.
      intentando encontrar el problema bajo la tenue luz de una linterna.
      Mientras tanto, María y Fernando se alejan un poco, buscando señal para pedir ayuda.
      Todo parece en calma... pero algo no está bien. El aire se siente más frío. Más denso.
      De pronto, un golpe. Otro. Gritos.
      Antes de que puedas reaccionar, tú y Humberto son emboscados.
      No ves de dónde vienen, solo sombras que se mueven con precisión mortal.
      Intentas correr, pero es inútil. Te derriban. No puedes moverte. No puedes gritar.
      Logras mirar hacia la camioneta… y el horror te invade.
      Fernando y María han sido asesinados. Degollados brutalmente.
      La escena es tan grotesca como irreal.
      Y entonces lo comprendes...
      No fue una simple falla mecánica. Fue una trampa.
      El lugar estaba preparado. Los responsables: un culto oculto en la oscuridad,
      cazadores de almas para sus rituales.
      Han estado esperando. Y ustedes… cayeron directo en su juego.
      🔻 FIN DEL JUEGO
      🎭 Sacrificio completado...
    """)

else:
    print("Respuesta Incorrecta, Escriba la correcta")