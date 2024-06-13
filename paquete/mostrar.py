def mostrarDestinos(lista_destinos):
    # Creamos un contador
    contador = 0
    # Recorremos la lista de destinos
    for indice, destino in enumerate(lista_destinos):
        # Mostramos el número de destino
        print(f'---- Destino {indice+1} ----')
        # Recorremos el diccionario de destino
        for key, value in destino.items():
            # Incrementamos el contador
            contador += 1
            # Imprimimos clave, valor
            print (f'{key} : {value}')
    # Si el contador es 0, mostramos mensaje de no hay registros
    if contador == 0:
        print('No hay destinos registrados')
    
    return lista_destinos

def mostrarClientes(lista_clientes):
    # Creamos un contador
    contador = 0
    # Recorremos la lista de clientes
    for indice, cliente in enumerate(lista_clientes):
        # Mostramos el número de cliente
        print(f'---- Cliente {indice+1} ----')
        # Recorremos el diccionario de cliente
        for key, value in cliente.items():
            # Incrementamos el contador
            contador += 1
            # Imprimimos clave, valor
            print (f'{key} : {value}')
    # Si el contador es 0, mostramos mensaje de no hay registros
    if contador == 0:
        print('No hay clientes registrados')

    return lista_clientes   

def mostrarReservas(lista_reservas, lista_destinos, lista_clientes):
    # Creamos un contador
    contador = 0
    # Recorremos la lista de reservas
    for indice, reserva in enumerate(lista_reservas):
        # Mostramos el número de reserva
        print(f'---- Reserva {indice+1} (ID Cliente: {reserva['idCliente']} || ID Destino: {reserva['idDestino']}) ----')
        # Recorremos el diccionario de reserva
        for key, value in reserva.items():
            # Incrementamos el contador
            contador += 1
        # Recorremos la lista de clientes
        for indiceCliente, cliente in enumerate(lista_clientes):
            # Recorremos el diccionario de cliente
            for key, value in cliente.items():
                # Si el ID del cliente coincide con el ID Cliente de la reserva
                if cliente['ID'] == reserva['idCliente']:
                    # Imprimimos el nombre del cliente
                    print(f'Cliente: {cliente['Nombre']}')
                    # Salimos del bucle
                    break
        # Recorremos la lista de destinos
        for indiceDestinos, destino in enumerate(lista_destinos):
            # Recorremos el diccionario de destino
            for key, value in destino.items():
                # Si el codigo de destino coincide con el ID Destino de la reserva
                if destino['Codigo'] == reserva['idDestino']:
                    # Mostramos el nombre del destino
                    print(f'Destino: {destino['Nombre']}')
                    print(f'Precio: {destino['Precio']} €')
                    # Salimos del bucle
                    break
    # Si no existen reservas hechas, mostramos mensaje
    if contador == 0:
        print('No hay reservas registradas')