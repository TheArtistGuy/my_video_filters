import cv2
from my_filters.echoes import echo_with_alpha

def run():

    cap = cv2.VideoCapture(0)
    pic_list = []

    while True:
        success, img = cap.read()

        if success:
            pic_list.append(img)
            if len(pic_list) > 10:
                pic_list.pop(0)

            image_to_show = echo_with_alpha(pic_list)

            cv2.imshow("output", image_to_show)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()