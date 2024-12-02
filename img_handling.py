import cv2 as cv
import time
from PIL import Image, ImageTk

def import_image(label):
    cap = cv.VideoCapture(0)
    start_time = time.time()
    countdown = 4

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        elapsed_time = time.time() - start_time
        remaining_time = countdown - int(elapsed_time)

        if remaining_time > 0:
            cv.putText(frame, str(remaining_time), (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3, cv.LINE_AA)
        else:
            cv.putText(frame, "", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3, cv.LINE_AA)
            label.imgtk = ImageTk.PhotoImage(image=Image.fromarray(cv.cvtColor(frame, cv.COLOR_BGR2RGB)))
            label.configure(image=label.imgtk)
            label.update()
            cv.waitKey(1000)  # Wait for 1 second to capture the final frame
            break

        label.imgtk = ImageTk.PhotoImage(image=Image.fromarray(cv.cvtColor(frame, cv.COLOR_BGR2RGB)))
        label.configure(image=label.imgtk)
        label.update()
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    ret, frame = cap.read()
    cv.imwrite(r'images/unchanged.jpg', frame)
    cap.release()