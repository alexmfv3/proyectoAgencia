def mostrarDestinos(lista_destinos):
    contador = 0
    for indice, destino in enumerate(lista_destinos):
        print(f'---- Destino {indice+1} ----')
        for key, value in destino.items():
            contador += 1
            # Imprimimos clave, valor
            print (f'{key} : {value}')
    if contador == 0:
        print('No hay destinos registrados')
    
    return lista_destinos

def mostrarClientes(lista_clientes):
    contador = 0
    for indice, cliente in enumerate(lista_clientes):
        print(f'---- Cliente {indice+1} ----')
        for key, value in cliente.items():
            contador += 1
            # Imprimimos clave, valor
            print (f'{key} : {value}')
    if contador == 0:
        print('No hay clientes registrados')

    return lista_clientes   

def mostrarReservas(lista_reservas, lista_destinos, lista_clientes):
    contador = 0
    for indice, reserva in enumerate(lista_reservas):
        print(f'---- Reserva {indice+1} (ID Reserva: {reserva['idCliente']}) ----')
        for key, value in reserva.items():
            contador += 1
        for indiceCliente, cliente in enumerate(lista_clientes):
            for key, value in cliente.items():
                if cliente['ID'] == reserva['idCliente']:
                    print(f'Cliente: {cliente['Nombre']}')
                    break
        for indiceDestinos, destino in enumerate(lista_destinos):
            for key, value in destino.items():
                if destino['Codigo'] == reserva['idDestino']:
                    print(f'Destino: {destino['Nombre']}')
                    break
    if contador == 0:
        print('No hay reservas registradas')