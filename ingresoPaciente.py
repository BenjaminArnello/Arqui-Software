
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
    message = b'00010sinitregis'
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

        if (recibido[7:9] == "AP"): #Agregar Paciente

            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='hospital'
            )

            datos = recibido[9:].split("/")

            rutPaciente = datos[0]
            nombre = datos[1]
            apellidoPaterno = datos[2]
            apellidoMaterno = datos[3]
            sexo = datos[4]

            print(rutPaciente)



            cursor = conn.cursor()

            query0 = "SELECT * from pacientes where rut = %s"

            cursor.execute(query0, (rutPaciente,))

            resp1 = cursor.fetchall()

            if len(resp1) == 0:



                query = """
                        INSERT IGNORE INTO pacientes (rut,nombre, apellidoPaterno, apellidoMaterno, sexo) values (%s,%s,%s,%s,%s)
                """



                # Execute the query with the current day and time
                cursor.execute(query, (rutPaciente, nombre, apellidoPaterno, apellidoMaterno, sexo))

                print("Row inserted successfully!")
                resp = 'regis'+ 'SC'


                respB = '{:05d}'.format (len(resp)) + resp

                print(respB)

                print("Send answer (if needed)")
                print('sending {}'.format(resp))
                sock.sendall(bytes(respB, 'utf-8'))



                conn.commit()
                cursor.close()
                conn.close()

            else:
                print("Row was not inserted (probably already exists)")
                resp = 'regis'+ 'ER'


                respB = '{:05d}'.format (len(resp)) + resp

                print(respB)

                print("Send answer (if needed)")
                print('sending {}'.format(resp))
                sock.sendall(bytes(respB, 'utf-8'))


                conn.commit()
                cursor.close()
                conn.close()



finally:

    print('closing socket')

    sock.close()
    # Close cursor and connection
