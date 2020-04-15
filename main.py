# The main script of the Encryptor
# author: Ofer026

from Window.window import Window
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import cryptography.fernet

class Main(Window):
    def __init__(self):
        Window.__init__(self)
        self.salt = b'O\x18\xdd\xb2\xf3\xaa\x11e\xfc\xd4\xf6=J\x0f\x85\xb5'
        self.debug = True

    def run_win(self):
        self.create_widgets()
        self.connect_buttons_commands()
        self.win.mainloop()

    def create_key(self, text):
        password_provided = self.get_password(title="enter Secret Key", text=text)
        password = password_provided.encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend()
        )
        self.key = base64.urlsafe_b64encode(kdf.derive(password))

    def encrypt_file(self):
        self.create_key(text="Enter a secret key to encrypt the file (Save it to decrypt it later)")
        self.get_file("Select a File to Encrypt")
        with open(self.file, "rb") as file:
            data = file.read()
        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(data)
        self.get_file_save_dist(title="Save Encrypted File", extensions=(("Encrypted Files", "*.encrypted"),
                                                                         ("All Files", "*.*")))
        try:
            with open(self.dist_file + os.path.splitext(self.dist_file)[-1], "wb") as encrypted_file:
                encrypted_file.write(encrypted_data)
        except FileNotFoundError:
            self.show_msg(title="Error!", text="No text to decrypt was given")
        self.show_msg(title="File saved", text=f"File saved at {self.dist_file}.encrypted")

    def decrypt_file(self):
        self.create_key(text="Enter a secret key to decrypt the file")
        self.get_file("Select a File to Decrypt")
        with open(self.file, "rb") as file:
            data = file.read()
        fernet = Fernet(self.key)
        try:
            decrypted_data = fernet.decrypt(data)
        except cryptography.fernet.InvalidToken:
            self.show_msg(title="Wrong Key", text="The key given is not correct, try again")
            return
        self.get_file_save_dist(title="Save Decrypted File", extensions=(("Decrypted Files", "*.decrypted"),
                                                                         ("Text", "*.txt"),
                                                                         ("All Files", "*.*")))
        try:
            with open(self.dist_file + os.path.splitext(self.dist_file)[-1], "wb") as decrypted_file:
                decrypted_file.write(decrypted_data)
        except FileNotFoundError:
            self.show_msg(title="Error!", text="No text to decrypt was given")
        self.show_msg(title="File saved", text=f"File saved at {self.dist_file}.decrypted")

    def encrypt_text(self):
        text = self.text_box.get("1.0", "end")
        if text == "\n":
            self.show_msg(title="Error!", text="No text to encrypt was given")
            return
        self.create_key(text="Enter a create a secret key to encrypt the text (save it to decrypt it later)")
        encoded_text = text.encode()
        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(encoded_text)
        self.get_file_save_dist(title="Save Encrypted File", extensions=(("Encrypted Files", "*.encrypted"),
                                                                         ("All Files", "*.*")))
        try:
            with open(self.dist_file + os.path.splitext(self.dist_file)[-1], "wb") as encrypted_file:
                encrypted_file.write(encrypted_data)
        except FileNotFoundError:
            self.show_msg(title="ERROR!", text="Error while saving file")
            return
        self.show_msg(title="File saved", text=f"File saved at {self.dist_file}.encrypted")

    def decrypt_text(self):
        text = self.text_box.get("1.0", "end")
        if text == "\n":
            self.show_msg(title="Error!", text="No text to decrypt was given")
            return
        self.create_key(text="Enter a create a secret key to decrypt the text")
        encoded_text = text.encode()
        fernet = Fernet(self.key)
        try:
            decrypted_data = fernet.decrypt(encoded_text)
        except cryptography.fernet.InvalidToken:
            self.show_msg(title="Wrong Key", text="The key given is not correct, try again")
            return

        self.get_file_save_dist(title="Save Encrypted File", extensions=(("decrypted Files", "*.decrypted"),
                                                                         ("All Files", "*.*")))
        try:
            with open(self.dist_file + os.path.splitext(self.dist_file)[-1], "wb") as decrypted_file:
                decrypted_file.write(decrypted_data)
        except FileNotFoundError:
            self.show_msg(title="Error!", text="No text to decrypt was given")
            return
        self.show_msg(title="File saved", text=f"File saved at {self.dist_file}.decrypted")

    def connect_buttons_commands(self):
        if self.debug:
            self.encrypt_file_button.config(command=self.encrypt_file)
            self.decrypt_file_button.config(command=self.decrypt_file)
            self.encrypt_text_button.config(command=self.encrypt_text)
            self.decrypt_text_button.config(command=self.decrypt_text)




def main():
    main = Main()
    main.run_win()

if __name__ == '__main__':
    main()