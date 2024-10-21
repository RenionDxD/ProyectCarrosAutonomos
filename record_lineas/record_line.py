import cv2
import numpy as np
import socket
import time


# Crea un objeto de socket
##sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta el socket al servidor en render.py
##server_address = ('localhost', 1234)
##sock.connect(server_address)


def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5),0)
    canny = cv2.Canny(blur, 50 ,150)
    return canny

def detectar_lineas(imagen, y_limite):
    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    # Aplicar suavizado para reducir el ruido
    imagen_suavizada = cv2.GaussianBlur(imagen_gris, (5, 5), 0)
    # Detectar bordes con el operador de Canny
    bordes = cv2.Canny(imagen_suavizada, 50, 150, apertureSize=3)
    # Detectar líneas utilizando la transformada de Hough
    lineas = cv2.HoughLinesP(bordes, 1, np.pi/180, threshold=50, minLineLength=50, maxLineGap=10)
    # Dibujar las líneas detectadas
    imagen_resultado = imagen.copy()
    coordenadas_lineas = []
    if lineas is not None:
        for linea in lineas:
            x1, y1, x2, y2 = linea[0]
            if y1 >= y_limite and y2 >= y_limite:
                coordenadas_lineas.append((x1, y1, x2, y2))
                if abs(x2 - x1) > abs(y2 - y1):
                    # Línea horizontal
                    cv2.line(imagen_resultado, (x1, y1), (x2, y2), (0, 255, 0), 2)
                else:
                    # Línea punteada
                    cv2.line(imagen_resultado, (x1, y1), (x2, y2), (0, 0, 255), 2, cv2.LINE_AA)
    return imagen_resultado, np.array(coordenadas_lineas)


def region_of_interest(frame):
    height, width, _ = frame.shape
    # Define las coordenadas del rectángulo de interés
    top_left = (0, int(height * 0.6))  # Esquina superior izquierda
    y_limite = int(frame.shape[0] * 0.61)
    bottom_right = (width, height)  # Esquina inferior derecha
    # Crea una imagen en negro del mismo tamaño que el marco original
    mask = np.zeros_like(frame)
    # Dibuja un rectángulo blanco en la máscara
    cv2.rectangle(mask, top_left, bottom_right, (255, 255, 255), -1)
    # Aplica la máscara al marco original utilizando la operación bitwise AND
    cropped_image = cv2.bitwise_and(frame, mask)
    #combined_image = cv2.addWeighted(frame, 1, cropped_image, 0.5, 0)
    return cropped_image, y_limite


def dibujar_lineas_en_frame(frame, lineas):
    frame_con_lineas = frame.copy()
    for linea in lineas:
        x1, y1, x2, y2 = linea
        #print(x1, y1, x2, y2)
        #lista_actualizable = [1,2,3,4,5]
            # Actualiza la lista
        #lista_actualizable.append(lista_actualizable[4] + linea)
        
        # Convierte la lista a una cadena de texto
        datos = " ".join(str(x) for x in linea)
        #print(datos)
        #os.system('cls')
        
        # Envía los datos al servidor en render.py
        ##sock.sendall(datos.encode())
        
        # Espera un segundo antes de la siguiente actualización
        time.sleep(0.001)
    

        cv2.line(frame_con_lineas, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return frame_con_lineas, datos



# Abrir el video
video = cv2.VideoCapture('../Multimedia/video_cars3.mp4')
while (video.isOpened()):
    # Leer un cuadro del video
    _, frame = video.read()
    frame=cv2.resize(frame,(1100,800))
    # Detectar líneas en el cuadro
    canny_image = canny(frame)
    cropped_image, top_left = region_of_interest(frame)
    frame_con_lineas, lineas = detectar_lineas(cropped_image, top_left)
    frame_con_lineas_convinadas,datos = dibujar_lineas_en_frame(frame, lineas)
    #print(frame_con_lineas_convinadas)
    #combined_image = cv2.addWeighted(cropped_image, 1, frame_con_lineas_originales, 0.5, 0)
    # Mostrar el cuadro con las líneas detectadas
    cv2.imshow("Lineas detectadas", frame_con_lineas_convinadas)
    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

# Liberar los recursos
video.release()
cv2.destroyAllWindows()

