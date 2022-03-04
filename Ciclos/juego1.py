import random
victorias = 0; derrotas = 0; empates = 0

menu = 1
while menu != 0:
    print('<1> Jugar')
    print('<2> Resultados')
    print('<0> Salir')

    menu = int(input('ingrese opcion: '))
    if menu == 1:
        nump = 1
        num = 0
        
        while nump != 0:
         
         num = random.randint(1, 3)
         
         print('<1> Piedra')
         print('<2> Papel')
         print('<3> Tijera')
         print('<0> Salir')

         nump = int(input('ingrese su elección: '))
         if nump == 1:
            if num == 2:
                print('Perdió: piedra vs papel')
                derrotas += 1
            elif num == 3:
                print('Gano: piedra vs tijera')
                victorias += 1
            elif num == 1:
                print('Empate: piedra vs piedra')
                empates += 1
         elif nump == 2:
            if num == 3:
                print('Perdió: papel vs tijera')
                derrotas += 1
            elif num == 1:
                print('Gano: papel vs piedra')
                victorias += 1
            elif num == 2:
                print('Empate: papel vs papel')
                empates += 1
         elif nump == 3:
            if num == 2:
                print('Perdió: tijera vs piedra')
                derrotas += 1
            elif num == 1:
                print('Gano: tijera vs papel')
                victorias += 1
            elif num ==3:
                print('Empate: tijera vs tijera')
                empates += 1
         elif nump == 0:
            print('gracias por jugar')
         else:
            print('ingreso no valido')
    elif menu == 2:
        print('Victoria:', victorias)
        print('Derrotas:', derrotas)
        print('Empates:', empates)
    elif menu == 0:
        print('Hasta la próxima')
    else:
        print('Ingreso no valido')
        print('Inténtelo nuevamente')
