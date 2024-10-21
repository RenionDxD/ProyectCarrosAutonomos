import cv2
import numpy as np




video = cv2.VideoCapture('../Multimedia/video_cars3.mp4')
while (video.isOpened()):
    # Leer un cuadro del video
    _, frame = video.read()

    # Definir los cuatro puntos del trapecio
    pts = np.array([(250, 250), (400, 250), (500, 300), (150, 300)], np.int32)
    pts2 = np.array([(250, 270), (400, 270), (500, 300), (150, 300)], np.int32)
    pts3 = np.array([(250, 290), (400, 290), (500, 300), (150, 300)], np.int32)

    pts = pts.reshape((-1, 1, 2))
    

    # Dibujar el trapecio en el cuadro
    cv2.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
    cv2.polylines(frame, [pts2], isClosed=True, color=(0, 255, 0), thickness=2)
    cv2.polylines(frame, [pts3], isClosed=True, color=(0, 255, 0), thickness=2)
    cv2.imshow("guia lineas", frame)
    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

# Liberar los recursos
video.release()
cv2.destroyAllWindows()
