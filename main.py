from Window.window import Window
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

class Main(Window):
    def __init__(self):
        Window.__init__(self)
        self.salt = b'O\x18\xdd\xb2\xf3\xaa\x11e\xfc\xd4\xf6=J\x0f\x85\xb5'
        self.debug = True
    def run_win(self):
        self.create_widgets()
        self.connect_buttons_commands()
        self.win.mainloop()
    def create_key(self):
        password_provided = self.get_password(title="enter Secret Key", text="Enter a secret key to encrypt the file (Save it to decrypt it later)")
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
        self.create_key()
        self.get_file("Select a File to Encrypt")
        with open(self.file, "rb") as file:
            data = file.read()
        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(data)
        print(encrypted_data)
            
    def connect_buttons_commands(self):
        if self.debug:
            self.encrypt_file_button.config(command=self.encrypt_file)




def main():
    main = Main()
    main.run_win()
if __name__ == '__main__':
    main()