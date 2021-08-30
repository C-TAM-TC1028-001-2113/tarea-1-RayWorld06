# coding=utf-8
def main():
    # escribe tu código abajo de esta línea

    mensajes = int(input("Dame el numero de mensajes: "))
    megas = float(input("Dame el numero de megas: "))
    minutos = int(input("Dame el numero de minutos: "))
    costo = (mensajes + megas + minutos) * 0.8
    print("El costo mensual es:",costo)

if __name__ == '__main__':
    main()
