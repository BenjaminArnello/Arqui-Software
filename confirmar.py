import mysql.connector
from datetime import datetime
import socket
import sys

# Establish a connection to the MySQL database

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # Send data
    message = b'00010sinitconfi'
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

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='citas'
        )


        cursor = conn.cursor()

        string = format(data) 

        c = string[7:len(string)-1]

        print (c)
       
        # Create a cursor to execute SQL queries

        # Query to get available doctors
        query = "UPDATE citas.horas SET Confirmado = 1 WHERE Id = %s"


        cursor.execute(query, (c,))

        conn.commit()

        resp = "confi" + c + "ok"


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

except KeyboardInterrupt:
    pass  # Handle Ctrl+C gracefully

finally:
    print('closing socket')
    sock.close()
    # Close cursor and connection

  