
import mysql.connector
from datetime import datetime
import socket
import sys

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='especialistas'
)



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # Send data
    message = b'00010sinitespec'
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

        cursor = conn.cursor()

        current_day = datetime.now().weekday() + 1  # 1 for Monday, 2 for Tuesday, etc.
        current_time = datetime.now().strftime('%I:%M %p')  # e.g., '03:45 PM'

        # Create a cursor to execute SQL queries

        # Query to get available doctors
        query = """
            SELECT e.*
            FROM especialistas AS e
            INNER JOIN horarios AS h
            ON e.especialista_id = h.especialista_id
            WHERE h.dia = %s
            AND STR_TO_DATE(h.inicio, ' %I:%i %p') <= STR_TO_DATE(%s, ' %I:%i %p')
            AND STR_TO_DATE(h.fin, ' %I:%i %p') >= STR_TO_DATE(%s, ' %I:%i %p')
        """

        # Execute the query with the current day and time
        cursor.execute(query, (current_day, current_time, current_time))

        # Fetch the results
        resp1 = cursor.fetchall()



        # Convert the list of values to a comma-separated string
        resp = 'espec'+','.join(map(str, resp1))


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



finally:
    print('closing socket')
    sock.close()
    # Close cursor and connection

    conn.close()
