def main():
    #escribe tu código abajo de esta línea
    edad = int(input("Ingresa tu edad: "))
    # Escribe el código adecuado para completar el programa
    # Para pedir el dato de la idetificación oficial emplea este mensaje:
    # "¿Tienes identificación oficial? (s/n): "
    if edad>0 and edad<18:
        print("No cumples requisitos")
    elif edad>=18:
        identificacion = str(input("¿Tienes identificación oficial? (s/n): "))
        if identificacion=="n":
            print("No cumples requisitos")
        elif identificacion=="s":
            print("Trámite de licencia concedido")
        else:
            print("Respuesta incorrecta")
    else:
        print ("Respuesta incorrecta")


if __name__=='__main__':
    main()

