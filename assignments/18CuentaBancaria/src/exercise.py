# coding=utf-8
def main():
    # escribe tu código abajo de esta línea
    pass
    saldo_mes_anterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    num_cheques = int(input("Dame el número de cheques: "))

    saldofinal = (saldo_mes_anterior + ingresos) - (egresos + (num_cheques * 13))
    interes_saldo = (saldofinal * 0.075)
    saldo_mostrar = saldofinal - interes_saldo
    saldo_mostrar_final = round(saldo_mostrar, 5)

    print("El saldo final de la cuenta es:", saldo_mostrar_final)


if __name__ == '__main__':
    main()
