# coding=utf-8
def main():
    # escribe tu código abajo de esta línea

    gramosharina = float(input("Dame la harina en gramos: "))
    calculo = (gramosharina) * (0.050)
    calculo = round(calculo,1)
    print("Necesitas estos gramos de levadura:", calculo)


if __name__ == '__main__':
    main()
