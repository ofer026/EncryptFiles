# A window class and all GUI management for the Encryptor
# author: Ofer026

import tkinter as tk
from tkinter import filedialog
import pyautogui


class Window():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Encrypt Files")
        self.win.geometry("800x800")
        # ------ Setting up Objects for the GUI ------
        self.encrypt_file_label = None
        self.encrypt_file_button = None
        self.decrypt_file_button = None
        self.encrypt_decrypt_text_label = None
        self.text_box = None
        self.encrypt_text_button = None
        self.decrypt_text_button = None
        # -------- Setting up objects for other functions -------
        self.file = None
        self.dist_file = None
        
    def create_widgets(self):
        self.encrypt_file_label = tk.Label(text="Encrypt/decrypt files:", font=("Roboto Light", 18))
        self.encrypt_file_label.place(x=50, y=22)
        self.encrypt_file_button = tk.Button(text="Encrypt", font=("Roboto Light", 12), height=4, width=12)
        self.encrypt_file_button.place(x=50, y=60)
        self.decrypt_file_button = tk.Button(text="Decrypt", font=("Roboto Light", 12), height=4, width=12)
        self.decrypt_file_button.place(x=200, y=60)
        self.encrypt_decrypt_text_label = tk.Label(text="Enter text to encrypt/decrypt:", font=("Roboto Light", 18))
        self.encrypt_decrypt_text_label.place(x=320, y=160)
        self.text_box = tk.Text(height=24, width=50, font=("Roboto Light", 12))
        self.text_box.place(x=320, y=200)
        self.encrypt_text_button = tk.Button(text="Encrypt", font=("Roboto Light", 12), height=4, width=12)
        self.encrypt_text_button.place(x=580, y=680)
        self.decrypt_text_button = tk.Button(text="Decrypt", font=("Roboto Light", 12), height=4, width=12)
        self.decrypt_text_button.place(x=420, y=680)

    def get_file(self, title):
        self.file = filedialog.askopenfilename(title=title, initialdir="/", multiple=False)

    def show_msg(self, title, text):
        pyautogui.alert(title=title, text=text)

    def get_file_save_dist(self, title, extensions):
        self.dist_file = filedialog.asksaveasfilename(title=title, filetypes=extensions)

    def get_password(self, title, text):
        result = pyautogui.password(title=title, text=text)
        return result

    def run(self):
        self.win.mainloop()


if __name__ == '__main__':
    win = Window()
    win.create_widgets()
    win.run()
