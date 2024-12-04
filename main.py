import customtkinter as ctk
from gemini import summarize_image, make_questions, return_text
from img_handling import import_image
from PIL import Image
import os

class NotedApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.title("Noted!")
        self.resizable(False, False)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(5, weight=1)

        self.video_label = ctk.CTkLabel(self, text="", fg_color="transparent", wraplength=100, width=400, height=300)
        self.video_label.grid(row=0, column=1, padx=10, pady=10, rowspan=5)
        import_image(self.video_label, activate_camera=False, width=400, height=300)

        self.img = None

        self.create_widgets()

    def import_image_display(self):
        import_image(self.video_label, activate_camera=True, width=400, height=300)
        try:
            self.img = Image.open(r'images/unchanged.jpg')
        except FileNotFoundError:
            print("Error: The image file was not found.")
            self.img = None

    def summarize_image_display(self):
        if self.img:
            self.summarize_label.grid()
            summarize_img_text = summarize_image(self.img)
            self.summarize_label.configure(text=summarize_img_text)
            self.question_label.grid_forget()
            self.text_label.grid_forget()
        else:
            print("Error: No image to summarize.")

    def make_questions_display(self):
        if self.img:
            self.question_label.grid()
            questions_img_text = make_questions(self.img)
            self.question_label.configure(text=questions_img_text)
            self.summarize_label.grid_forget()
            self.text_label.grid_forget()
        else:
            print("Error: No image to generate questions from.")

    def convert_to_text_display(self):
        if self.img:
            self.text_label.grid()
            return_img_text = return_text(self.img)
            self.text_label.configure(text=return_img_text)
            self.question_label.grid_forget()
            self.summarize_label.grid_forget()
        else:
            print("Error: No image to convert to text.")


    def create_widgets(self):
        import_btn = ctk.CTkButton(self, text="take picture", command=self.import_image_display)
        import_btn.grid(row=0, column=0, padx=10, pady=10)

        self.summarize_btn = ctk.CTkButton(self, text="summarize", command=self.summarize_image_display)
        self.summarize_btn.grid(row=1, column=0, padx=10, pady=10)

        self.questions_btn = ctk.CTkButton(self, text="questions", command=self.make_questions_display)
        self.questions_btn.grid(row=2, column=0, padx=10, pady=10)

        self.text_btn = ctk.CTkButton(self, text="convert", command=self.convert_to_text_display)
        self.text_btn.grid(row=3, column=0, padx=10, pady=10)

        self.summarize_label = ctk.CTkLabel(self, text="", fg_color="transparent", wraplength=300)
        self.summarize_label.grid(row=2, column=2, padx=10)

        self.question_label = ctk.CTkLabel(self, text="", fg_color="transparent", wraplength=300)
        self.question_label.grid(row=3, column=2, padx=10)

        self.text_label = ctk.CTkLabel(self, text="", fg_color="transparent", wraplength=300)
        self.text_label.grid(row=4, column=2, padx=10)

if __name__ == "__main__":
    app = NotedApp()
    app.mainloop()