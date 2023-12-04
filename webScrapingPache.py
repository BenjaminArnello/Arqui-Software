import requests
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime, timedelta

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
    message = b'00010sinitmedic'
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

        # Assuming 'data' is a variable with some content
        string = format(data)

        if len(data) <= 5:
            resp = "medic" +  "NK" + "No ingresar campos vacíos"
            respB = '{:05d}'.format (len(resp)) + resp

            print(respB)

            print("Send answer (if needed)")
            print('sending {}'.format(resp))
            sock.sendall(bytes(respB, 'utf-8'))
            continue

        # Assuming 'data' is in a format that needs some sort of parsing
        remedios = string[7:len(string) - 1].split('-')
        print(remedios)
        print(remedios[0])
        

        # Establish a database connection
        cursor = conn.cursor()
        
        query = """
        SELECT * FROM hospital.remedios WHERE nombre IN ({})
        """.format(','.join(['%s'] * len(remedios)))

        print(query)

        cursor.execute(query, remedios)
        results = cursor.fetchall()

        if len(results) < 1:
                resp = "medic" +  "NK" + "Medicamento no recetable"
                respB = '{:05d}'.format (len(resp)) + resp

                print(respB)

                print("Send answer (if needed)")
                print('sending {}'.format(resp))
                sock.sendall(bytes(respB, 'utf-8'))
                continue

        resultsList = []

        for result in results:
            resultsList.append(list(result))

        
        print(resultsList)



        print(resultsList)
        
        disponibles = []
        noDisponibles = []
        idBuscar = []

        for valores in resultsList:
            if valores[2] != 0:
                disponibles.append([valores[1], valores[2] ])

            else: 
                idBuscar.append(valores[0])
                noDisponibles.append([valores[1], "0"])
        
        if len(idBuscar) != 0:
            query2 = """
            SELECT * FROM busqueda_remedios WHERE id_remedio IN ({})
            """.format(','.join(['%s'] * len(idBuscar)))

            print(query2)

            
            cursor.execute(query2, idBuscar)

            results2 = cursor.fetchall()

            if len(results2) < 1:
                    resp = "medic" +  "NK" + "Medicamento no disponible en farmacias cercanas"
                    respB = '{:05d}'.format (len(resp)) + resp

                    print(respB)

                    print("Send answer (if needed)")
                    print('sending {}'.format(resp))
                    sock.sendall(bytes(respB, 'utf-8'))
                    continue

            results2List = []

            for result in results2:
                results2List.append(list(result))

            for x in range(len(results2)):
                # Assuming your date is in the format YYYY-MM-DD HH:MM:SS
                fecha = results2List[x][2]

                print(fecha)

                given_datetime = datetime.combine(fecha, datetime.min.time())

                print(datetime.now())

                # Calculate the difference between the current time and the given date
                delta = datetime.now() - given_datetime

                print (fecha, delta)

                # Check if the time difference is greater than 48 hours
                if delta > timedelta(hours=48):

                    url = results2List[x][1]
                    print(url)

                    response = requests.get(url)

                    # Check if the request was successful (status code 200)
                    if response.status_code == 200:
                        # Parse the HTML content of the page using BeautifulSoup
                        soup = BeautifulSoup(response.content, 'html.parser')

                        # Find elements by their HTML tags, class, id, etc., and extract specific values
                        # Replace 'tag', 'class_', 'id_', etc., with the specific attributes of the elements you want to scrape
                        web = soup.find(class_='vtex-product-price-1-x-currencyInteger')  # Example

                        # Extract specific text or attributes from the found elements
                        if web:
                            # Extract the text content of the element
                            valueWeb = web.text.strip()
                            print(f"Scraped value: {valueWeb}")
                            noDisponibles[x][1] = valueWeb
                        else:
                            print("No data found.")

                            noDisponibles[x][1] = "0"

                    else:
                            print("Failed to retrieve the webpage.")
                            noDisponibles[x][1] = "0"


                else:


                    print("The date is not yet 48 hours old.")
                    temp = results2List[x][3]
                    noDisponibles[x][1]  = temp


        # Convert the list of values to a comma-separated string
        resp = 'medic'+ ','.join(map(str, disponibles)) + "-" + ",".join(map(str, noDisponibles))


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


except KeyboardInterrupt:
    pass  # Handle Ctrl+C gracefully



finally:
    print('closing socket')
    sock.close()
    # Close cursor and connection

    conn.close()
