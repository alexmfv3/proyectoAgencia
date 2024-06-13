from paquete.mostrar import mostrarClientes, mostrarDestinos

def delReserva(lista_reservas, lista_clientes):
    
    while True:
        # Mostramos menú de eliminación
        print('''
            Menu de eliminación
              1- eliminar por id de cliente
              2- eliminar por id de destino
              3- volver al menú principal
            ''')
        op = input('Introduce una opcion del menú: ')
        match op:
            case '1':
                mostrarClientes(lista_clientes)
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
                
                for indice, cliente in enumerate(lista_clientes):
                    for key, value in cliente.items():
                        if cliente['ID'] == clienteId:
                            del lista_clientes[indice]
                            print(f'Se ha eliminado con éxito a {cliente['Nombre']}')
                            break
                        else:
                            print('No se ha encontrado este cliente')
            case '2':
                mostrarDestinos(lista_reservas)
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
                
                for indice, reserva in enumerate(lista_reservas):
                    for key, value in reserva.items():
                        if reserva['idDestino'] == destinoId:
                            del lista_reservas[indice]
                            print(f'Se ha eliminado con éxito la reserva con ID de destino {reserva['idDestino']}')
                            break
                        else:
                            print('No se ha encontrado este destino')
                
            case '3':
                break
            case _: 
                print('Opción no contemplada')