from paquete.addCliente import addCliente
from paquete.addDestino import addDestino
from paquete.delDestino import delReserva
from paquete.addReserva import addReserva
from paquete.mostrar import mostrarClientes, mostrarDestinos, mostrarReservas


import os
def clear_screen():
     os.system ("cls")

def pause_screen ():
    print ("Pulse Enter para continuar...")
    input ()


def principal():

    lista_destinos = []
    lista_clientes = []
    lista_reservas = []
    while True:
        print('''
        Menu de opciones:
          1- Añadir un nuevo destino
          2- Añadir un nuevo cliente
          3- Realizar una reserva
          4- Cancelar una reserva
          5- Mostrar todos los destinos
          6- Mostrar todos los clientes
          7- Mostrar todas las reservas
          8- Salir
        ''')
        # Preguntamos al usuario por la opción (cadena string)
        opcion = input('Introduce una opcion del menu: ')
        
        match opcion:
            case '1':              
                addDestino(lista_destinos)
                pause_screen()
                clear_screen()
            case '2':
                addCliente(lista_clientes)
                pause_screen()
                clear_screen()
            case '3':
                addReserva(lista_reservas, lista_clientes, lista_destinos)
                pause_screen()
                clear_screen()
            case '4':              
                delReserva(lista_reservas, lista_clientes, lista_destinos)
                pause_screen()
                clear_screen()
            case '5':              
                mostrarDestinos(lista_destinos)
                pause_screen()
                clear_screen()
            case '6':              
                mostrarClientes(lista_clientes)
                pause_screen()
                clear_screen()
            case '7':              
                mostrarReservas(lista_reservas, lista_destinos, lista_clientes)
                pause_screen()
                clear_screen()
            case '8':              
                break
            case _:
                print('Opcion no contemplada')
                

           
principal()
print('Fin de programa')