
import mysql.connector
from datetime import datetime
import socket
import sys



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # Send data
    message = b'00010sinitrecet'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = int(sock.recv(5))
    while amount_received < amount_expected:
        data = sock.recv(amount_expected - amount_received)
        amount_received += len(data)
        print('received {!r}'.format(data))

    while True:
        print("Waiting for transaction")
        amount_received = 0
        amount_expected = int(sock.recv(5))

        while amount_received < amount_expected:
            data = sock.recv(amount_expected - amount_received)
            amount_received += len(data)
            print('received {!r}'.format(data))

        print("Processing ...")

        recibido = format(data)

        if (recibido[7:9] == "RP"): #Receta Paciente

            # Establish a connection to the MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='hospital'
            )

            rutPaciente = recibido[9:19]

            print(rutPaciente)



            cursor = conn.cursor()


            query = """
                SELECT recetas.fecha, recetas.texto
                FROM pacientes
                INNER JOIN recetas ON pacientes.id_paciente = recetas.id_paciente
                WHERE pacientes.rut = %s
                ORDER BY recetas.fecha DESC;

            """

            # Execute the query with the current day and time
            cursor.execute(query, (rutPaciente,))

            # Fetch the results
            resp1 = cursor.fetchall()

            print(resp1)



            # Convert the list of values to a comma-separated string
            resp = 'recet'+'/'.join(map(str, resp1))


            respB = '{:05d}'.format (len(resp)) + resp

            print(respB)

            print("Send answer (if needed)")
            print('sending {}'.format(resp))
            sock.sendall(bytes(respB, 'utf-8'))

            # Print the available doctors
        # if resp1:
            #   print("Available Doctors:")
            # for doctor in resp1:
            #      print(doctor)
        # else:
            #   print("No doctors available at the current time.")


            cursor.close()
            conn.close()
        
        elif (recibido[7:9] == "CR"): #CF = Crear Receta

            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='hospital'
            )


            print("CF")

            cursor = conn.cursor()

            string = format(data) 

            split = string[9:len(string) - 1].split('/')
            print(split)

            pacienteRut = split[0]
            texto = split[1]


            print(pacienteRut)
            print(texto)

        
            query = "SELECT id_paciente FROM hospital.pacientes where rut = %s"
            cursor.execute(query, (pacienteRut,))

            result = cursor.fetchall()
            print(result[0][0])

            idPaciente = result[0][0]

            # Query to get available doctors
            query2 = "INSERT INTO hospital.recetas (id_paciente, texto, fecha) VALUES (%s, %s, NOW()) "
            


            cursor.execute(query2, (idPaciente, texto,))

            print("insertado")

            conn.commit()

            resp = "recet" + "CR" +  "ok"

            


            # Fetch the results
    
            # Convert the list of values to a comma-separated string

            respB = '{:05d}'.format (len(resp)) + resp

            print(respB)

            print("Send answer (if needed)")
            print('sending {}'.format(resp))
            sock.sendall(bytes(respB, 'utf-8'))

            # Print the available doctors
        # if resp1:
            #   print("Available Doctors:")
            # for doctor in resp1:
            #      print(doctor)
        # else:
            #   print("No doctors available at the current time.")
            cursor.close()
            conn.close()
            
        
        else:
            
            resp = "camas" + "error"



finally:

    print('closing socket')

    sock.close()
    # Close cursor and connection
