import socket
import mysql.connector
from datetime import datetime, timedelta
import unicodedata
import re


# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al puerto donde el servidor está escuchando
server_address = ('localhost', 5000)
print('Connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
print('Connected successfully')


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def remove_special_characters(input_str):
    # Keep only letters, numbers, spaces, and underscores
    return re.sub(r'[^a-zA-Z0-9\s_]', '', input_str)


# Cursor para ejecutar consultas SQL


try:
    # Send data
    message = b'00010sinitvisit'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = int(sock.recv(5))

    while amount_received < amount_expected:
        data = sock.recv(amount_expected - amount_received)
        amount_received += len(data)
        print('received {!r}'.format(data))

        while True:
            amount_received = 0
            amount_expected = int(sock.recv(5))

            while amount_received < amount_expected:
                data = sock.recv(amount_expected - amount_received)
                amount_received += len(data)
                print('received {!r}'.format(data))

            print("Processing ...")


            db_connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='hospital'
            )

            cursor = db_connection.cursor()
            cursor2 = db_connection.cursor() 

        
            recibido = format(data)
            print(recibido)
            if (recibido[7:9] == "RV"): #Registrar Visita
                recibido2 = recibido[9:len(recibido) - 1].split('/')
                print(recibido2)
                
                    # Solicitar el id_paciente al usuario
                rut_paciente = recibido2[0]
                hora_llegada = datetime.now()
                hora_salida = hora_llegada + timedelta(hours=2)
                hora_llegada = hora_llegada.strftime("%H:%M")
                hora_salida = hora_salida.strftime("%H:%M")
                nombre_visita = recibido2[1]
                rut_visita = recibido2[2]
                nombre_visita = remove_accents(nombre_visita)
                nombre_visita =  remove_special_characters(nombre_visita)

        
                fecha = datetime.now().date()
                
                query = "SELECT id_paciente FROM pacientes WHERE rut = %s;"
                cursor.execute(query, (rut_paciente,))
                respuesta = cursor.fetchall()

                if len(respuesta) == 0:

                    resp = "visit" + "NORUT"
                    respB = '{:05d}'.format (len(resp)) + resp
                    print(respB)

                    print("Send answer (if needed)")
                    print('sending {}'.format(resp))
                    sock.sendall(bytes(respB, 'utf-8'))


                id_paciente = respuesta[0][0]
                print(id_paciente)
                
                # Insertar información en la base de datos
                insert_query = """
                INSERT INTO control_visitas (id_paciente, hora_llegada, hora_salida, fecha, nombre_visita,rut_visita)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """

                cursor2.execute(insert_query, (id_paciente, hora_llegada, hora_salida, fecha, nombre_visita,rut_visita, ))
                
                db_connection.commit()

                resp = "visit" + "RV" + "OK" + hora_salida
                respB = '{:05d}'.format (len(resp)) + resp

                print(respB)

                print("Send answer (if needed)")
                print('sending {}'.format(resp))
                sock.sendall(bytes(respB, 'utf-8'))
                continue
            
            if (recibido[7:9] == "CV"): #Confirmar Visita
                
                recibido2 = recibido[9:len(recibido) - 2].split(',')
                
                print(recibido2)
                
                    # Solicitar el id_paciente al usuario

                
            
                select_query = """
                UPDATE control_visitas SET confirmado = 1 WHERE id_visita IN ({})
                """.format(','.join(['%s']*len(recibido2)))



                cursor2.execute(select_query, recibido2)
                db_connection.commit()
                # Cambio del valor del estado de la visita
                
                resp = "visit" + "CV" + "OK" + "Visita confirmada correctamente"
                respB = '{:05d}'.format (len(resp)) + resp

                print(respB)

                print("Send answer (if needed)")
                print('sending {}'.format(resp))
                sock.sendall(bytes(respB, 'utf-8'))
                continue
            
            if (recibido[7:9] == "AV"): #Actualizar Visita
                
                print("Processing ...")



                # Create a cursor to execute SQL queries

                # Query to get available doctors
                query = """
                   SELECT cp.id_visita, cp.hora_llegada, cp.hora_salida, cp.fecha, cp.nombre_visita, cp.rut_visita, cp.confirmado,
                        p.Nombre, p.apellidoPaterno, p.apellidoMaterno
                    FROM control_visitas cp
                    JOIN pacientes p ON cp.id_paciente = p.id_paciente;
                """

                # Execute the query with the current day and time
                cursor.execute(query)

                # Fetch the results
                resp1 = cursor.fetchall()

                print(resp1)

                respF = []

                for fila in resp1:
                    nombre = fila[7] + " " + fila[8] + " " + fila[9]
                    respF.append([fila[0], nombre, fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]])



                



                # Convert the list of values to a comma-separated string
                resp = 'visit'+'/'.join(map(str, respF))


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
    pass  # Manejar Ctrl+C

finally:
    # Cerrar conexiones
    print('Closing socket and database connection')
    sock.close()
    cursor.close()
    db_connection.close()
