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
    message = b'00010sinitdocto'
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

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='hospital'
        )

        print("Processing ...")

        

        cursor = conn.cursor()
        cursor2 = conn.cursor()

        # Create a cursor to execute SQL queries
        
        # Query to get available doctors
        query = """
            SELECT * FROM hospital.doctores
        """
        cursor.execute(query)
        resp = cursor.fetchall()

        mat = []

        query2 = """
                SELECT * 
                FROM horarios as h
                WHERE doctor_id = %s
            """

        # Execute the query with the current day and time
        for i in range(5):
            id = resp[i][0]
            print(id)
            cursor2.execute(query2, (id,))

            # Fetch the results
            resp1 = cursor2.fetchall()
            temp = []
            temp.append(resp[i][1])
            for x in range(7):
                aux = resp1[x][3] + "-" + resp1[x][4]
                temp.append(aux)
            mat.append(temp)

            
        
        print(mat)

        # Convert the list of values to a comma-separated string
        resp = 'docto'+'/'.join(map(str, mat))

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
        cursor2.close()



finally:
    print('closing socket')
    sock.close()
    # Close cursor and connection

    conn.close()
