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
    message = b'00010sinithoras'
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
            database='citas'
        )


        cursor = conn.cursor()

        # Create a cursor to execute SQL queries

        # Query to get available doctors
        query = """
            SELECT * FROM citas.horas
            WHERE DATE(dia) = CURDATE();
        
        """
        # Execute the query with the current day
        cursor.execute(query)

        # Fetch the results
        resp1 = cursor.fetchall()

        array = []



        for fila in resp1:
            tempArr = []
            i = 0
            for dato in fila:
                if i == 3 :
                    tempFecha = str(dato)
                    print(tempFecha)
                    tempArr.append(tempFecha)
                elif i == 6 :
                    tempHora = str(dato)
                    print(tempHora)
                    tempArr.append(tempHora)   
                else: tempArr.append(dato)    
                i += 1
            print (tempArr)
            array.append(tempArr)        
        print(array)   

        # Convert the list of values to a comma-separated string
        resp = 'horas'+','.join(map(str, array))

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

finally:
    print('closing socket')
    sock.close()
    # Close cursor and connection

   