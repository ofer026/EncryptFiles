import tkinter as tk
from tkinter import filedialog

class Window():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Encrypt Files")
        self.win.geometry("800x800")
    def create_widgets(self):
        self.encrypt_file = tk.Button(text="Encrypt", font=("Roboto Light", 12), height=4, width=12)
        self.encrypt_file.place(x=50, y=60)
        self.decrypt_file = tk.Button(text="Decrypt", font=("Roboto Light", 12), height=4, width=12)
        self.decrypt_file.place(x=200, y=60)
        self.encrypt_decrypt_text_label = tk.Label(text="Enter text to encrypt/decrypt:", font=("Roboto Light", 18))
        self.encrypt_decrypt_text_label.place(x=320, y=160)
        self.text_box = tk.Text(height=24, width=50, font=("Roboto Light", 12))
        self.text_box.place(x=320, y=200)
        self.encrypt_text = tk.Button(text="Encrypt", font=("Roboto Light", 12), height=4, width=12)
        self.encrypt_text.place(x=580, y=680)
        self.decrypt_text = tk.Button(text="Decrypt", font=("Roboto Light", 12), height=4, width=12)
        self.decrypt_text.place(x=420, y=680)
    def get_file(self, title):
        self.file = filedialog.askopenfilename(title=title, initaldir="/", multiple=False)
    def run(self):
        self.win.mainloop()

if __name__ == '__main__':
    win = Window()
    win.create_widgets()
    win.run()