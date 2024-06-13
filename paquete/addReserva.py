
def addReserva(lista_reservas):
    while True:
        try:
            # Preguntamos al usuario por un ID de cliente
            clienteId = int(input('Introduce una ID de Cliente: '))
            # Si introduce un valor numérico válido, salimos del bucle infinito
            break
        except ValueError:
            # En caso de que introduzca un valor inválido, mostramos mensaje de error
            print('Debes introducir un ID de cliente válido!!')
    
    while True:
        try:
            # Preguntamos al usuario por un ID de cliente
            destinoId = int(input('Introduce una ID de Destino: '))
            # Si introduce un valor numérico válido, salimos del bucle infinito
            break
        except ValueError:
            # En caso de que introduzca un valor inválido, mostramos mensaje de error
            print('Debes introducir un ID de destino válido!!')

    # Una vez todo en orden, creamos un diccionario con la información del cliente  
    reserva = {
        'idCliente' : clienteId,
        'idDestino' : destinoId,
    }
    # Y añadimos esta info a la lista de clientes
    lista_reservas.append(reserva)