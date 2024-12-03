import cv2 as cv
import time
from PIL import Image, ImageTk

def import_image(label, activate_camera, width=400, height=300):
    # Display placeholder image
    placeholder = Image.open('images/img_placeholder.png')
    placeholder_imgtk = ImageTk.PhotoImage(image=placeholder)
    label.imgtk = placeholder_imgtk
    label.configure(image=placeholder_imgtk)
    label.update()

    cap = cv.VideoCapture(0)
    start_time = time.time()
    countdown = 4

    if activate_camera:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            elapsed_time = time.time() - start_time
            remaining_time = countdown - int(elapsed_time)

            if remaining_time > 0:
                cv.putText(frame, str(remaining_time), (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3, cv.LINE_AA)
            else:
                frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                frame = cv.resize(frame, (width, height))
                frame = Image.fromarray(frame)
                label.imgtk = ImageTk.PhotoImage(image=frame)
                label.configure(image=label.imgtk)
                label.update()
                cv.waitKey(1000)  # Wait for 1 second to capture the final frame
                break

            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            frame = cv.resize(frame, (width, height))
            frame = Image.fromarray(frame)
            label.imgtk = ImageTk.PhotoImage(image=frame)
            label.configure(image=label.imgtk)
            label.update()
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        ret, frame = cap.read()
        frame = cv.resize(frame, (width, height))
        cv.imwrite(r'images/unchanged.jpg', frame)
        cap.release()