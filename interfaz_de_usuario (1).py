from lógica_del_negocio import Aspirante

def comprobar_sí_es_número_entero(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

def solicitar_entero_en_rango(dato_solicitado, valor_inicial_rango, valor_final_rango):
    while True:
        entrada = input(f"Ingrese por favor {dato_solicitado}: ")
        if comprobar_sí_es_número_entero(entrada):
            representación_entera = int(entrada)
            if valor_inicial_rango <= representación_entera <= valor_final_rango:
                return representación_entera
            else:
                print(f"Recuerde que el valor debe estar entre {valor_inicial_rango} y {valor_final_rango}")
        else:
            print("Recuerde que debe ingresar un entero")

seguir_pidiendo_aspirantes = True
contador_de_aspirantes = 0

while seguir_pidiendo_aspirantes:
    print("******************************************************************")
    print("Bienvenido al programa club promesas bananeras para calcular la efectividad y la puntería")
    print("******************************************************************")
    print("************ Seleccione una de las siguientes opciones ************")
    print("1. Calcular métricas de efectividad y puntería a un nuevo aspirante")
    print("2. Salir del programa")
    print("********************************************")
    opción_seleccionada = input("Ingrese la acción que desea realizar (1 o 2): ")

    if opción_seleccionada in ("1", "2"):
        if opción_seleccionada == "1":
            print("---------------------------------------------") 
            print("Del aspirante", contador_de_aspirantes + 1, "por favor ingrese:")
            
            while True:
                nombre = input("Ingrese el nombre: ")
                if nombre.strip():
                    break
                else:
                    print("Recuerde que el nombre no puede estar vacío")
            
            while True:
                apellido = input("Ingrese el apellido: ")
                if apellido.strip():
                    break
                else:
                    print("Recuerde que el apellido no puede estar vacío")

            un_aspirante = Aspirante(nombre, apellido)

            solicitar_disparos_desviados = solicitar_entero_en_rango("disparos desviados", 0, 30)
            un_aspirante.establecer_disparos_desviados(solicitar_disparos_desviados)

            solicitar_disparos_atajados = solicitar_entero_en_rango("disparos atajados", 0, 30)
            un_aspirante.establecer_disparos_atajados(solicitar_disparos_atajados)

            solicitar_goles = solicitar_entero_en_rango("goles", 0, 10)
            un_aspirante.establecer_goles(solicitar_goles)

            print("---------------------------------------------") 
            print("Puntería =>", un_aspirante.calcular_puntería())
            print("Efectividad =>", un_aspirante.calcular_efectividad())
            print("Nivel de efectividad =>", un_aspirante.nivel_efectividad())
            print("Nivel de puntería =>", un_aspirante.nivel_punteria())
            print("Proyección de goles para el campeonato =>", un_aspirante.proyeccion_goles_campeonato())
            print("¿El aspirante pasó la prueba técnica?", un_aspirante.pasar_prueba_tecnica())
        
            contador_de_aspirantes += 1
        else:
            seguir_pidiendo_aspirantes = False
            print("***********************************************************")
            print("Gracias por usar el programa hasta una próxima ocasión")
            print("***********************************************************")
    else:
        print("***********************************************************")
        print("¡ERROR! Por favor ingrese una de las dos opciones indicadas")
print("La cantidad de aspirantes ingresados fue de", contador_de_aspirantes)
