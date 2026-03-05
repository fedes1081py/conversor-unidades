# 1 = 0.6213
# 1kg = 2.204 libras
# 0celsiu = 32 farenheit


def kilometros_millas(dato):
    return round(dato*0.62,2)

def kilogramos_libras(dato):
    return round(dato*2.204,2)

def celsius_fahrenheit(dato):
    return round((dato*(9/5)+32),2)

def validar_dato(mensaje,tipo):
    while True:
        print(mensaje)
        try:
            if tipo == 'float':
                opcion = float(input("Decime el dato: "))
            else:
                opcion = int(input("Decime la  opcion deseada: "))
                if not opcion >0 and not opcion <5:
                    raise ValueError
            return opcion
        except ValueError:
            print("Error en el dato ingresado")

def pedir_dato():
    pass


mensaje_opcion = "1) Kilometros -> Millas\n2) Kilogramos -> Libras\n3) Celsius -> Fahrenheit\n4) Salir"
mensaje_dato = "Ahora me vas a pasar la informacion"
def menu():
    opcion = validar_dato(mensaje_opcion,'int')
    dato = validar_dato(mensaje_dato,'float')
    diccionario = {
        1:kilometros_millas,
        2:kilogramos_libras,
        3:celsius_fahrenheit
    }
    dato_final = diccionario[opcion](dato)
    print(f"El resultado es {dato_final}")



menu()