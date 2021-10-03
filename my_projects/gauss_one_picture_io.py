import cv2

from my_filters.boarder_detection import gauss


def run():
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()

        if success:
            image_to_show = gauss(img)
            cv2.namedWindow("output", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("output", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow("output", image_to_show)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()