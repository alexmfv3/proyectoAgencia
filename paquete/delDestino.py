from paquete.mostrar import mostrarClientes, mostrarDestinos, mostrarReservas

def delReserva(lista_reservas, lista_clientes, lista_destinos):
    mostrarReservas(lista_reservas, lista_destinos, lista_clientes)
    # Validamos que el usuario introduzca una ID de cliente válido
    while True:
        try:
            # Preguntamos al usuario por un ID de cliente
            clienteId = int(input('Dame un ID de cliente: '))
            # Si introduce un valor numérico válido, salimos del bucle infinito
            break
        except ValueError:
            # En caso de que introduzca un valor inválido, mostramos mensaje de error
            print('Debes introducir un ID de cliente válido!!')
                
                
    # Validamos que el usuario introduzca una ID de cliente válido
    while True:
        try:
            # Preguntamos al usuario por un ID de cliente
            destinoId = int(input('Dame un ID de destino: '))
            # Si introduce un valor numérico válido, salimos del bucle infinito
            break
        except ValueError:
            # En caso de que introduzca un valor inválido, mostramos mensaje de error
            print('Debes introducir un ID de destino válido!!')

    contador = 0        
    for indice, reserva in enumerate(lista_reservas):
        for key, value in reserva.items():
            if reserva['idDestino'] == destinoId and reserva['idCliente'] == clienteId:
                contador += 1
                del lista_reservas[indice]
                print('Se ha eliminado la reserva con éxito')
                break
    if contador == 0:
        print('No se ha encontrado esta reserva')

           

