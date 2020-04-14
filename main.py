from Window.window import Window
import pyautogui
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Main(Window):
    def __init__(self):
        Window.__init__(self)
        self.salt = b'O\x18\xdd\xb2\xf3\xaa\x11e\xfc\xd4\xf6=J\x0f\x85\xb5'
        self.debug = True
    def run_win(self):
        self.create_widgets()
        self.connect()
        self.win.mainloop()
    def create_key(self):
        password_provided = pyautogui.password(title="enter Secret Key", text="Enter a secret key to encrypt the file (Save it to decrypt it later)")
        password = password_provided.encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend()
        )
        self.key = base64.urlsafe_b64encode(kdf.derive(password))
        print(self.key)
    def connect(self):
        if self.debug:
            self.encrypt_file.config(command=self.create_key)




def main():
    main = Main()
    main.run_win()
if __name__ == '__main__':
    main()