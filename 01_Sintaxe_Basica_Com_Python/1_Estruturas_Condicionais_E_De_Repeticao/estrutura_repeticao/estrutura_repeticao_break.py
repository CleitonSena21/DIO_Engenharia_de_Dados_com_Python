while True: 
    numero = int(input("Informe em nùmero: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)