import mysql.connector
from datetime import datetime
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print ('connecting to {} port {}'.format (*server_address))
sock.connect (server_address)

try:
    # Send data
    message = b'00010sinitextra'
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
        
        # Establish a connection to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='hospital'
        )
        nombre_remedio = []
        cantidad_total = []
        numerito = recibido[7:len(recibido)-1].split('-')
        for x in range(len(numerito)-1):
            aux = numerito[x].split(',')
            print(aux)
            nombre_remedio.append(aux[0])
            cantidad_total.append(aux[1])
        print(nombre_remedio)

        cursor = conn.cursor()


        query = """
            UPDATE remedios
            SET cantidad = %s
            WHERE nombre = %s;

        """

        for x in range(len(cantidad_total)):
            cursor.execute(query, (cantidad_total[x], nombre_remedio[x],))

        conn.commit()
        conn.close()

        resp = "extra" + "OK"

        respB = '{:05d}'.format (len(resp)) + resp

        print(respB)

        print("Send answer (if needed)")
        print('sending {}'.format(resp))
        sock.sendall(bytes(respB, 'utf-8'))
        
        cursor.close()
        conn.close()

        # Execute the query with the current day and time

        # Fetch the results







finally:
    print('closing socket')
    sock.close()
    # Close cursor and connection
