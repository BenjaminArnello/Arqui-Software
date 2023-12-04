import mysql.connector
from datetime import datetime
import socket
import sys
import hashlib


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # Send data
    message = b'00010sinitlogin'
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

        # Establish a connection to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='hospital'
        )

        cursor = conn.cursor()

        recibido = format(data)
        print(data)
        if len(data) <= 5:
            resp = "login" +  "NK" + "No ingresar campos vacíos"
            respB = '{:05d}'.format (len(resp)) + resp

            print(respB)

            print("Send answer (if needed)")
            print('sending {}'.format(resp))
            sock.sendall(bytes(respB, 'utf-8'))
            continue

        split = recibido[7:len(recibido) - 1].split('/')
        rutLogin = split[0]
        passLogin = split[1]
        my_hash = hashlib.sha256(passLogin.encode('utf-8')).hexdigest()

        query = """
            SELECT *
            FROM login
            WHERE login.rut = %s AND
            login.pass = %s;
        """

        cursor = conn.cursor()

        cursor.execute(query, (rutLogin,my_hash,))

        resp1 = cursor.fetchall()

        if len(resp1) < 1:
            resp = "login" +  "NK" + "Rut y/o contraseña inválidos"
            respB = '{:05d}'.format (len(resp)) + resp

            print(respB)

            print("Send answer (if needed)")
            print('sending {}'.format(resp))
            sock.sendall(bytes(respB, 'utf-8'))
            continue

        resp = "login"+"OK"

        respB = '{:05d}'.format (len(resp)) + resp

        print(respB)

        print("Send answer (if needed)")
        print('sending {}'.format(resp))
        sock.sendall(bytes(respB, 'utf-8'))
        
        cursor.close()
        conn.close()

finally:
    print('closing socket')
    sock.close()
    # Close cursor and connection
