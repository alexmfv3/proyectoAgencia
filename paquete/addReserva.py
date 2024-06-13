
def addReserva(lista_reservas, lista_clientes, lista_destinos):
    while True:
        try:
            # Preguntamos al usuario por un ID de cliente
            clienteId = int(input('Introduce una ID de Cliente: '))
            # Validamos que el ID de cliente no esté vacio
            if clienteId == '':
                print('Esto es un campo obligatorio!!')
            else:
                # Si introduce un valor numérico válido, salimos del bucle infinito
                break
        except ValueError:
            # En caso de que introduzca un valor inválido, mostramos mensaje de error
            print('Debes introducir un ID de cliente válido!!')
    
    while True:
        try:
            # Preguntamos al usuario por un ID de cliente
            destinoId = int(input('Introduce una ID de Destino: '))
            # Validamos que el ID de destino no esté vacio
            if destinoId == '':
                print('Esto es un campo obligatorio!!')
            else:
                # Si introduce un valor numérico válido, salimos del bucle infinito
                break
        except ValueError:
            # En caso de que introduzca un valor inválido, mostramos mensaje de error
            print('Debes introducir un ID de destino válido!!')
    
    # Validar que no se puedan añadir reservas sin cliente y destino
    contadorClientes = 0
    for indice, clientes in enumerate(lista_clientes):
        contadorClientes += 1

    contadorDestinos = 0
    for indice, destinos in enumerate(lista_destinos):
        contadorDestinos += 1
    
    if contadorClientes == 0 or contadorDestinos == 0:
        print('No se pudo añadir la reserva.')
    else:
        # Una vez todo en orden, creamos un diccionario con la información del cliente  
        reserva = {
            'idCliente' : clienteId,
            'idDestino' : destinoId,
        }
        # Y añadimos esta info a la lista de clientes
        lista_reservas.append(reserva)