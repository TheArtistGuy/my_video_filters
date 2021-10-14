import cv2
import numpy as np


def run():


    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()

        if not success:
            print("Konnte Kamera nicht öffnen!")
            break
        else:
            img_canny = cv2.Canny(img, 150, 180)

            kernel = np.ones((3, 3), dtype=np.uint8)
            img_dialation = cv2.dilate(img_canny, kernel, iterations=1)
            cv2.namedWindow("output", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("output", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow("output", img_dialation)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()


run()