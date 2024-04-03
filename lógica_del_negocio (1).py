class Aspirante:
    def __init__(self, nombres:str, apellidos:str):

        if len(nombres.strip()) == 0:
            raise ValueError("La cadena con los nombres del aspirante no puede estar vacía o ser solo espacios en blanco")
        
        if len(apellidos.strip()) == 0:
            raise ValueError("La cadena con los nombres del aspirante no puede estar vacía o ser solo espacios en blanco")

        self.nombres = nombres
        self.apellidos = apellidos
        self.disparos_desviados = None
        self.disparos_atajados = None
        self.goles = None


    def establecer_disparos_desviados(self, disparos_desviados:int):
        limite_inferior_disparos_desviados = 0
        limite_superior_disparos_desviados =  30
        if not limite_inferior_disparos_desviados <= disparos_desviados <= limite_superior_disparos_desviados:
            raise ValueError("El número de disparos desviados está por fuera del rango permitido")
        self.disparos_desviados = disparos_desviados

    
    def establecer_disparos_atajados(self, disparos_atajados:int):
        limite_inferior_disparos_atajados = 0
        limite_superior_disparos_atajados =  30
        if not limite_inferior_disparos_atajados <= disparos_atajados <= limite_superior_disparos_atajados:
            raise ValueError("El número de disparos atajados está por fuera del rango permitido")
        self.disparos_atajados = disparos_atajados


    def establecer_goles(self, goles:int):
        limite_inferior_goles = 0
        limite_superior_goles =  10
        if not limite_inferior_goles <= goles <= limite_superior_goles:
            raise ValueError("El número de goles está por fuera del rango permitido")
        self.goles = goles

    def calcular_total_disparos(self)-> int:
        total_disparos = self.disparos_desviados + self.disparos_atajados + self.goles
        return total_disparos

    def calcular_total_disparos_puerta(self)-> int:
        total_disparos_puerta = self.disparos_atajados + self.goles
        return total_disparos_puerta

    def calcular_puntería(self)-> float:
        total_disparos = self.calcular_total_disparos()
        total_disparos_puerta = self.calcular_total_disparos_puerta()
        puntería = (total_disparos_puerta / total_disparos) * 100
        return round(puntería,2)
        
    def calcular_efectividad(self)-> float:
        total_disparos = self.calcular_total_disparos()
        efectividad = (self.goles/total_disparos) * 100
        return round(efectividad,2)

    def nivel_punteria(self) -> str:
        punteria = self.calcular_puntería()
        if punteria >= 80:
            return "alta"
        elif punteria >= 50:
            return "media"
        else:
            return "baja"

    def nivel_efectividad(self) -> str:
        efectividad = self.calcular_efectividad()
        if efectividad > 50:
            return "muy alta"
        elif efectividad >= 20:
            return "alta"
        else:
            return "baja"
    
    def pasar_prueba_tecnica(self) -> str:
        nivel_punteria = self.nivel_punteria()
        nivel_efectividad = self.nivel_efectividad()
        if nivel_efectividad == "muy alta" or (nivel_efectividad == "alta" and nivel_punteria == "media"):
            return "sí pasó la prueba"
        else:
            return "no pasó la prueba"
        
    def proyeccion_goles_campeonato(self) -> int:
        goles_prueba = self.goles * 4
        goles_mes1 = goles_prueba
        goles_mes2 = (90 * goles_mes1 + goles_prueba * 4) / 2
        goles_mes3 = (90 * goles_mes2 + goles_prueba * 4) / 2
        goles_mes4 = (90 * goles_mes3 + goles_prueba * 4) / 2
        goles_mes5 = (90 * goles_mes4 + goles_prueba * 4) / 2
        goles_totales = goles_mes1 + goles_mes2 + goles_mes3 + goles_mes4 + goles_mes5
        return goles_totales

