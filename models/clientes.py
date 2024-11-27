from banco.config_banco import db;
from models.usuarios import User;

#criscso do cliente
class Cliente(User):
    #criacao no banco de dados 
    __tablename__ = 'cliente';
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True);

    def __init__(self, nome, telefone, email, senha):
        super().__init__(nome,telefone, email, senha);
    
    





