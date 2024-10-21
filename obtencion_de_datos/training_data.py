import socket
import csv
import os 
#from record_lineas.record_line import datos
# Crea un objeto de socket
##sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincula el socket a una dirección y puerto
##server_address = []


##server_address = ('localhost', 1234)


#print(server_address)
##sock.bind(server_address)

# Escucha conexiones entrantes
##sock.listen(1)

print("Esperando conexión...")

# Acepta una conexión entrante
#connection, client_address = sock.accept()
print("Conexión establecida.")
datos = []
data = 0
while True:
    # Recibe los datos desde el cliente en main.py
    #data = connection.recv(1024).decode()
    
    # Convierte los datos a una lista
    lista_actualizable = [int(x) for x in data.split()]
    datos.append(lista_actualizable)
    #x1, y1, x2, y2 = lista_actualizable
    # Haz algo con la lista actualizada
    #data.append(data)
    datos_con_distancias = list(zip(datos))
    print(lista_actualizable)
    #os.system('cls')
    # Guardar los datos en un archivo CSV
    with open('coordenadas.csv', 'w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(['coordenadas'])
        for coordenadas in datos_con_distancias:
            writer.writerow([coordenadas])