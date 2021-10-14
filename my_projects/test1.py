import cv2

anzahl_wiederholungn = 6

while True:
    success = True
    if not success:
        print("Konnte Kamera nicht öffnen!")
        break
    else:
        #

        key= cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        if key == ord('-') & anzahl_wiederholungen > 2:
            anzahl_wiederholungen = anzahl_wiederholungen - 1
        if key == ord('+'): anzahl_wiederholungen = anzahl_wiederholungen + 1
