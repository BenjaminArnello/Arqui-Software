import mysql.connector
from datetime import datetime
import socket
import sys
from datetime import datetime

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # Send data
    message = b'00010sinitcitas'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = int(sock.recv(5))
    while amount_received < amount_expected:
        data = sock.recv(amount_expected - amount_received)
        amount_received += len(data)
        print('received {!r}'.format(data))

    

    while True:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='hospital'
        )

        conn2 = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='citas'
        )

        print ("Esperando Mensaje")
        amount_received = 0
        amount_expected = int(sock.recv (5))

        while amount_received < amount_expected:
                data = sock.recv (amount_expected - amount_received)
                amount_received += len (data)
                print('received {!r}'.format(data))

        print ("Procesando...")

        recibido = format(data)

        if (recibido[7:9]) == "AH": #AH = Agendar Hora:


            recibidoPros = recibido[9:len(recibido)-1]

            arreglo = recibidoPros.split(',')

            print(arreglo)

            da = arreglo[0]
            ti = arreglo[1]
            esp = arreglo[2]



            indi = datetime.strptime(da, '%Y-%m-%d')
            dia = indi.weekday()
            dia = dia+1


            cursor = conn.cursor()
            query = """
                        SELECT hospital.horarios.* FROM hospital.horarios
                        INNER JOIN hospital.doctores ON horarios.doctor_id = doctores.doctor_id
                        WHERE horarios.dia = %s
                        AND doctores.especialidad = %s
                    """

            cursor.execute(query, (dia,esp,))

            resp1 = cursor.fetchall()

            print(resp1[0])

            id_uso = []

            for i in range(len(resp1)):
                arr = resp1[i]
                inic = arr[3]
                fin = arr[4]
                inic_hora = int(inic[0:2])
                fin_hora = int(fin[0:2])

                if inic[6] == 'P':

                    inic_hora = inic_hora + 12

                if fin[6] == 'P':

                    fin_hora = fin_hora + 12

                if inic_hora <= int(ti[0:2]) < fin_hora:

                    id_uso.append(arr[1])

            print(id_uso)
                    
            cursor2 = conn2.cursor()

            query2 = """
                SELECT * FROM citas.horas
                WHERE Dia = %s
                AND Hora = %s
            """

            cursor2.execute(query2, (da,ti,))
            resp2 = cursor2.fetchall()

            for x in range(len(resp2)):
                if resp2[x][4] in id_uso:
                    id_uso.remove(resp2[x][4])

                    
            enviar = []

            query3 = """
                SELECT doctor_id, nombre FROM  hospital.doctores
                WHERE doctor_id IN ({})
                """.format(','.join(['%s']*len(id_uso)))
                    

                    
            if len(id_uso) > 0 :

                cursor.execute(query3, id_uso)

                enviar = cursor.fetchall()

            else: enviar += [{"0", "Vacio"}]

                    

            print(enviar)

            resp = 'citas'+'/'.join(map(str, enviar))


            respB = '{:05d}'.format (len(resp)) + resp

            print(respB)

            print("Send answer (if needed)")
            print('sending {}'.format(resp))

            sock.sendall(bytes(respB, 'utf-8'))

            cursor2.close()

            cursor.close()

        #CONFIRMAR CITAS

        elif (recibido[7:9]) == "CH":
                 
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='citas'
            )


            cursor = conn.cursor()

            string = format(data) 

            c = string[9:len(string)-1]

            print (c)

            if (c != ""):
        
                # Create a cursor to execute SQL queries

                # Query to get available doctors
                ids = c.split(",")  # Replace this with your actual list of IDs

                print(ids)



                # Create placeholders for the SQL query
                placeholders = ', '.join(['%s'] * len(ids))

                # Modify the query
                query = """UPDATE citas.horas SET Confirmado = 1 WHERE Id IN ({})
                """.format(','.join(['%s']*len(ids)))

                cursor.execute(query, ids)

                conn.commit()

                resp = "citas" + "OK"


                # Fetch the results
        
                # Convert the list of values to a comma-separated string

                respB = '{:05d}'.format (len(resp)) + resp

                print(respB)


                print('sending {}'.format(resp))
                sock.sendall(bytes(respB, 'utf-8'))


                conn.close()
            
            else:
                resp = "citas" + "nk"

                respB = '{:05d}'.format (len(resp)) + resp

                print(respB)


                print('sending {}'.format(resp))
                sock.sendall(bytes(respB, 'utf-8'))


                conn.close()
        
        elif (recibido[7:9]) == "AG":

            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='hospital'
            )


            cursor = conn.cursor()

            recibidos = recibido[9:len(recibido)-1].split("/")
            print(recibidos)

            query = "SELECT nombre, apellidoPaterno, apellidoMaterno FROM pacientes where rut = %s"

            cursor.execute(query,(recibidos[0],))
      

            resp1 = cursor.fetchall()
            print(resp1)

            if (len(resp1) == 0):
                resp = "citas" + "NE"
                respB = '{:05d}'.format (len(resp)) + resp

                print(respB)


                print('sending {}'.format(resp))
                sock.sendall(bytes(respB, 'utf-8'))


                conn.close()
                conn2.commit()
                conn2.close()

    

            else:

                partes = resp1[0]
                nombre1 = partes[0]
                print(nombre1)
                nombre = partes[0] + " " + partes[1] + " " + partes[2] 
                print(nombre)

                
                conn2 = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='1234',
                    database='citas'
                )

                cursor2 = conn2.cursor()

                
                query2 = "INSERT INTO horas (nombrePaciente, Rut, Dia, id_doctor, hora) values (%s,%s,%s,%s,%s)"

                Dia = recibidos[3]
                print(Dia)
                id_doctor = recibidos[1]
                hora = recibidos[2]
        

                cursor2.execute(query2,(nombre, recibidos[0], Dia, id_doctor, hora,))

            
                resp = "citas" + "OK"

                respB = '{:05d}'.format (len(resp)) + resp

                print(respB)


                print('sending {}'.format(resp))
                sock.sendall(bytes(respB, 'utf-8'))


                conn.close()
                conn2.commit()
                conn2.close()
                


                        

except KeyboardInterrupt:
    pass  # Handle Ctrl+C gracefully


finally:

    resp = "confi" + "error"

    respB = '{:05d}'.format (len(resp)) + resp

    print(respB)


    print('sending {}'.format(resp))
    sock.sendall(bytes(respB, 'utf-8'))

    print ('closing socket')
    sock.close ()        