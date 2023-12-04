
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
    message = b'00010sinitcamas'
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

        if (recibido[7:9] == "DC"): #Disponibilidad camas

            # Establish a connection to the MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='hospital'
            )



            cursor = conn.cursor()


            query = """
                SELECT s.id_sala, s.tipo, COUNT(c.id_cama) AS camas_totales,
                SUM(c.ocupada) AS camas_ocupadas,
                COUNT(c.id_cama) - SUM(c.ocupada) AS camas_disponibles
                FROM Salas s
                LEFT JOIN Camas c ON s.id_sala = c.id_salas
                GROUP BY s.id_sala
                ORDER BY camas_ocupadas DESC;

            """

            # Execute the query with the current day and time
            cursor.execute(query)

            # Fetch the results
            resp1 = cursor.fetchall()

            print(resp1)



            # Convert the list of values to a comma-separated string
            resp = 'camas'+'/'.join(map(str, resp1))
            print(resp)


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
        
        elif (recibido[7:9] == "SC"): #SC = Seleccionar Cama

            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='hospital'
            )


            print("SC")

            cursor = conn.cursor()

            string = format(data) 

            split = string[9:len(string) - 1].split('/')
            print(split)

            coId = split[2]
            sId = split[1]
            rut = split[0]

            print (sId)
            print (rut)

        
            # Create a cursor to execute SQL queries

            # Query to get available doctors
            quer = "SELECT id_cama FROM hospital.camas WHERE id_salas = %s AND ocupada = 0 LIMIT 1"
            query = "UPDATE hospital.camas SET ocupada = 1 WHERE id_salas = %s AND id_cama = %s"
            query2 = "UPDATE hospital.pacientes SET id_cama = %s WHERE rut = %s"
            desocuparCama = "UPDATE hospital.camas SET ocupada = 0 where id_cama = %s"

            cursor.execute(quer, (sId,))
            cIdaux = cursor.fetchall()
            cId = cIdaux[0][0]
            print(cId)
            cursor.execute(query, (sId, cId))
            cursor.execute(query2,(cId, rut,))
            cursor.execute(desocuparCama,(coId,))

            conn.commit()

            resp = "camas" + "/" + str(cId) 


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
