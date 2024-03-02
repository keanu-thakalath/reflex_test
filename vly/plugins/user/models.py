import reflex as rx
import werkzeug

class User(rx.Model, table=True):
    email: str
    password_hash: str

    def __init__(self, password: str, *args, **kwargs):
        password_hash = werkzeug.security.generate_password_hash(password)
        super().__init__(password_hash=password_hash, *args, **kwargs)
    
    def check_password(self, password: str) -> bool:
        return werkzeug.security.check_password_hash(self.password_hash, password)