import cv2
from my_filters.boarder_detection import picture_difference
from my_filters.echoes import echo_with_alpha


def run():


    cap = cv2.VideoCapture(0)
    pic_list_for_picture_difference = []
    pic_list_for_echo = []
    anzahl_wiederholungen = 6

    while True:
        success, img = cap.read()

        if not success:
            print("Konnte Kamera nicht öffnen!")
            break
        else:
            pic_list_for_picture_difference.append(img)
            crop_list_to_size(2 ,pic_list_for_picture_difference)
            if(len(pic_list_for_picture_difference) >= 2):
                image_to_buffer = picture_difference(pic_list_for_picture_difference[0], pic_list_for_picture_difference[1])

                pic_list_for_echo.append(image_to_buffer)
                crop_list_to_size(anzahl_wiederholungen, pic_list_for_echo)
                image_to_show = echo_with_alpha(pic_list_for_echo, anzahl_wiederholungen)
                output_to_screen(image_to_show)


            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            if key == ord('-'):
                if anzahl_wiederholungen > 2 :
                    anzahl_wiederholungen = anzahl_wiederholungen - 1
                print(anzahl_wiederholungen)
            if key == ord('+'):
                anzahl_wiederholungen = anzahl_wiederholungen + 1
                print(anzahl_wiederholungen)

    cap.release()
    cv2.destroyAllWindows()


def crop_list_to_size(size, list):
    while len(list) > size:
        list.pop(0)


def output_to_screen(image_to_show):
    cv2.namedWindow("output", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("output", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("output", image_to_show)
