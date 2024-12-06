from models.usuarios import User;
from banco.config_banco import db;

class Admin(User):
    __tablename__ = 'Admin';
    id_admin =  db.Column(db.Integer, primary_key=True, autoincrement=True);

def __init__(self, nome, telefone, email, senha):
        super().__init__(nome, telefone, email, senha);