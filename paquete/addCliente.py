def addCliente(lista_clientes):
    print('>>> Añadir Cliente')
    # Validamos que el ID del cliente sea válido
    while True:
        try:
            # Preguntamos al usuario el ID del cliente
            idCliente = int(input('Introduce el ID del cliente: '))

            # Validamos que el ID de cliente sea correcto
            if idCliente <= 0:
                print('Debes introducir un ID de Cliente válido!!')
            else:
                # Si es un valor numérico, salimos del bucle infinito
                break
        except ValueError:
            # Si el ID del cliente es inválido, mostramos mensaje de error
            print('Debes introducir un ID de cliente válido!!')
        
    # Validamos que el nombre del cliente sea válido
    while True:
        nomCliente = str(input('Introduce el nombre del cliente: '))
        if nomCliente == '':
            print('Debes introducir un nombre de cliente válido!!')
        else:
            # De lo contrario, salimos del bucle infinito
            break  

    # Una vez todo en orden, creamos un diccionario con la información del cliente  
    cliente = {
        'ID' : idCliente,
        'Nombre' : nomCliente,
    }

    # Y añadimos esta info a la lista de clientes
    lista_clientes.append(cliente)

    return lista_clientes