def addDestino(lista_destinos):
    print('>>> Añadir Destino')
    # Validamos que el codDestino sea válido
    while True:
        try:
            # Preguntamos al usuario por el código
            codDestino = int(input('Introduce el codigo del destino: '))

            # Validamos que el código de destino sea correcto
            if codDestino <= 0:
                print('Debes introducir un código válido!!')
            else:
                # Si es un valor numérico, salimos del bucle infinito
                break
        except ValueError:
            # Si el código es inválido, mostramos mensaje de error
            print('Debes introducir un código de destino válido!!')

    # Validamos que el nombre del destino sea válido
    while True:
        nomDestino = str(input('Introduce el nombre del destino: '))
        # Si este está vacío, mostramos mensaje de error
        if nomDestino == '':
            print('Debes introducir un nombre de destino válido!!')
        else:
            # De lo contrario, salimos del bucle infinito
            break

    # Validamos que el importe del destino sea válido
    while True:
        try:
            # Preguntamos al usuario por el importe
            prcDestino = float(input('Introduce el precio del destino: '))
            # Validación de que el precio sea positivo (¡AQUÍ NO REGALAMOS DINERO!)
            if prcDestino < 0:
                print('Debes introducir un precio válido!!')
            else:
                break
            # Si es un valor numérico, salimos del bucle infinito
        except ValueError:
            # Si el importe es inválido, mostramos mensaje de error
            print('Debes introducir un precio válido!!')

    # Una vez todo en orden, creamos un diccionario con la información del destino
    destino = {
        'Codigo' : codDestino,
        'Nombre' : nomDestino,
        'Precio' : prcDestino
    }
    
    # Y añadimos esta info a la lista de destinos
    lista_destinos.append(destino)

    return lista_destinos