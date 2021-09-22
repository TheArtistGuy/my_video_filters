import cv2
from my_filters.gauss import gauss

def run():
    cap = cv2.VideoCapture(0)
    pic_list = []

    while True:
        success, img = cap.read()

        if success:
            pic_list.append(img)
            if len(pic_list) > 2:
                pic_list.pop(0)

            if(len(pic_list) >= 2):
                image_to_show = gauss(pic_list[0], pic_list[1])
                cv2.imshow("output", image_to_show)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()