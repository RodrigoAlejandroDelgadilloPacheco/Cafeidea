Azucar = 20
Agua = 200
Cafe = 1

def menu_principal():
    while True:
        if Azucar < 10 or Agua < 200 or Cafe < 1:
            print("¿Qué desea?")
            print("[1] Gestión")
            print("[3] Salir")
        else:
            print("¿Qué desea?")
            print("[1] Gestión")
            print("[2] Comprar")
            print("[3] Salir")

        opcion = obtener_opcion([1, 2, 3] if Azucar >= 10 and Agua >= 200 and Cafe >= 1 else [1, 3])

        if opcion == 1:
            gestion_menu()
        elif opcion == 2 and Azucar >= 10 and Agua >= 200 and Cafe >= 1:
            compra_menu()
        elif opcion == 3:
            print("Saliendo del programa...")
            break

def obtener_opcion(opciones_validas):
    while True:
        try:
            opcion = int(input("Introduce la opción: "))
            if opcion in opciones_validas:
                return opcion
            else:
                print("Opción no válida.")
        except ValueError:
            print("Número inválido")

def gestion_menu():
    global Azucar, Agua, Cafe

    while True:
        print("¿Qué vamos a añadir?")
        print("[1] Azúcar")
        print("[2] Agua")
        print("[3] Café")
        print("[4] Regresar")

        opcion = obtener_opcion([1, 2, 3, 4])

        if opcion == 4:
            break

        cantidad = obtener_cantidad("¿Cuánto deseas añadir?: ")
        if cantidad < 0:
            print("No se permite números negativos")
            continue

        if opcion == 1:
            Azucar += cantidad
            print(f"Añadido {cantidad}g de azúcar. Total: {Azucar}g")
        elif opcion == 2:
            Agua += cantidad
            print(f"Añadido {cantidad}ml de agua. Total: {Agua}ml")
        elif opcion == 3:
            Cafe += cantidad
            print(f"Añadido {cantidad} cartuchos de café. Total: {Cafe}")
        print("================================")

def obtener_cantidad(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Número inválido")

def compra_menu():
    global Azucar, Agua, Cafe

    print("¿Qué café deseas?")
    print("[1] Espresso (30ml)")
    print("[2] Capuchino (60ml)")
    print("[3] Mocaccino (60ml)")
    print("[4] Regresar")

    tipo_cafe = obtener_opcion([1, 2, 3, 4])

    if tipo_cafe == 4:
        return

    print("¿Cuánta azúcar deseas?")
    print("[1] Nada (0g)")
    print("[2] Poco (5g)")
    print("[3] Medio (10g)")
    print("[4] Mucho (15g)")
    print("[5] Muchísimo (20g)")

    azucar_opciones = {1: 0, 2: 5, 3: 10, 4: 15, 5: 20}
    opcion_azucar = obtener_opcion([1, 2, 3, 4, 5])
    cantidad_azucar = azucar_opciones[opcion_azucar]

    agua_necesaria = 30 if tipo_cafe == 1 else 60

    if Azucar >= cantidad_azucar and Agua >= agua_necesaria and Cafe >= 1:
        Azucar -= cantidad_azucar
        Agua -= agua_necesaria
        Cafe -= 1
        print("Café preparado. ¡Disfruta!")
    else:
        print("Recursos insuficientes para preparar el café.")

    print("================================")

menu_principal()
