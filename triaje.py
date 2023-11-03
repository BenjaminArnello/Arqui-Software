import socket
import sys

# Create a TCP/IP socket
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print ('connecting to {} port {}'.format (*server_address))
sock.connect (server_address)


def tablatriaje(entrada):
    nivel = 0
    sintomas = ["Dificultad respiratoria severa, 1",
                "Coloracion azul en piel, 1",
                "Frialdad generalizada, 1",
                "Traumatismo severos multiples, 1",
                "Quemaduras en todo el cuerpo, 1",
                "Perdida de miembro u organo, 1",
                "Hemorragia masiva, 1",
                "Trabajo de parte expulsivo, 1",
                "Abuso sexual, 1",
                "Alteracion aguda de signos vitales, 2",
                "Estado convulsivo, 2",
                "Deficiencia respiratoria moderada, 2",
                "Crisis hipertensiva, 2",
                "Diabetes descompesada, 2",
                "Dolor toracico, 2",
                "Trauma severo, 2",
                "Quemadura de tercer grado, 2",
                "Riesgo de perdida de miembro u organo, 2",
                "Fractura, 2",
                "Hemorragia digestiva, 2",
                "Sangrado vaginal en embarazadas, 2",
                "Trabajo de parto, 2",
                "Abuso sexual antiguo, 2",
                "Agitacion psicomotora, 2",
                "Ingestion de sustancias toxicas o envenenamiento, 2",
                "Dolor agudo, 2",
                "Fiebre mayor a 38.5, 3",
                "Vertigo severo, 3",
                "Dificultad respiratoria leve, 3",
                "Vomito y diarrea con deshidratación, 3",
                "Sintomas asociados o dialisis, 3",
                "Dolor moderado de menos de 24 horas, 3",
                "Trauma moderado, 3",
                "Quemadura segundo o primer grado, 3",
                "Sangrado moderado, 3",
                "Reaccion alergica con brote generalizado, 3",
                "Fiebre menor a 38.5, 4",
                "Tos y congestion, 4",
                "Faringitis, 4",
                "Amigdalitis, 4",
                "Vomito, 4",
                "Diarrea sin deshidratacion, 4",
                "Dolor leve, 4",
                "Dolor moderado de mas de 24 horas, 4",
                "Trauma leve, 4",
                "Signos de infeccion local, 4",
                "Ardor al orinar, 4",
                "Enfermedad venerea aguda, 4",
                "Ansiedad y depresion, 4",
                "Colico menstrual, 4",
                "Dolor de cabeza cronico, 5",
                "Tos cronica,5",
                "Inapetencia,5",
                "Dolor abdominal cronico, 5",
                "Dolor postraumatico leve, 5",
                "Dermatitis, 5",
                "Estres emocional, 5",
                "Enfermedades cronicas, 5",
                "Formulacion de medicamentos, 5",
                "Lectura de examenes, 5",
                "Diarrea cronica, 5",
                "Estreñimiento, 5"]

    
    for sintoma in sintomas:
        partes = sintoma.split(', ')
        if len(partes) == 2:
            nombre, valor = partes
            if entrada == nombre:
                nivel = int(valor)
                break

    if nivel == 0:
        nivel = 5 

    return nivel


def triaje(sintomas):
    nivel=5
    for i in sintomas:
        triaje = tablatriaje(i)
        if triaje < nivel:
            nivel = triaje
        else:
            nivel=nivel
    return nivel    

try:
    # Send data
    message = b'00010sinittriaj'
    print ('sending {!r}'.format (message))
    sock.sendall (message)

    amount_received = 0
    amount_expected = int(sock.recv (5))
    while amount_received < amount_expected:
        data = sock.recv (amount_expected - amount_received)
        amount_received += len (data)
        print('received {!r}'.format(data))

    while True:
      print ("Esperando Triaje")
      amount_received = 0
      amount_expected = int(sock.recv (5))

      while amount_received < amount_expected:
          data = sock.recv (amount_expected - amount_received)
          amount_received += len (data)
          print('received {!r}'.format(data))

          
       
      print ("Processing ...")

      recibido = format(data)

      recibidoPros = recibido[7:len(recibido)-1]

      arreglo = recibidoPros.split('-')

      print(arreglo)

      resTriaje = "triaj" + str(triaje(arreglo))

      print(resTriaje)
          

      resp = '{:05d}'.format(len(resTriaje)) + resTriaje
      print ("Send answer (if needed)")
      print ('sending {}'.format (resp))



      sock.sendall (bytes(resp, 'utf-8'))


finally:
    print ('closing socket')
    sock.close ()        




