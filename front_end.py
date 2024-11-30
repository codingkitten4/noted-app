import customtkinter
from gemini_file import summarize_image, make_questions, return_text
from img_handling import import_image
from PIL import Image

app = customtkinter.CTk()
app.geometry("1000x700")
app.title("Noted!")

def import_image_display():
    import_image()
    global img
    img = Image.open(r"images/unchanged.jpg")

summarize = customtkinter.CTkLabel(app, text="", fg_color="transparent", wraplength=300)
summarize.grid(row=1, column=1, padx=10)

question = customtkinter.CTkLabel(app, text="", fg_color="transparent", wraplength=300)
question.grid(row=1, column=2, padx=10)

text = customtkinter.CTkLabel(app, text="", fg_color="transparent", wraplength=300)
text.grid(row=1, column=3, padx=10)

def summarize_image_display():
    summarize_img_text = summarize_image(img)
    summarize.configure(text=summarize_img_text)

def make_questions_display():
    questions_img_text = make_questions(img)
    question.configure(text=questions_img_text)

def convert_to_text_display():
    return_img_text = return_text(img)
    text.configure(text=return_img_text)

import_btn = customtkinter.CTkButton(app, text="take picture", command=import_image_display)
import_btn.grid(row=0, column=0, padx=10)

summarize_btn = customtkinter.CTkButton(app, text="summarize", command=summarize_image_display)
summarize_btn.grid(row=0, column=1, padx=10)

questions_btn = customtkinter.CTkButton(app, text="questions", command=make_questions_display)
questions_btn.grid(row=0, column=2, padx=10)

text_btn = customtkinter.CTkButton(app, text="convert", command=convert_to_text_display)
text_btn.grid(row=0, column=3, padx=10)

app.mainloop()