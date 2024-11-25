from banco.config_banco import db;
#criscso do cliente
class Cliente(db.Model):
    #criacao no banco de dados 
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True);
    nome = db.Column(db.String(255), nullable=False);
    telefone = db.Column(db.String(15), nullable=False);
    email = db.Column(db.String(255), nullable=False);
    senha = db.Column(db.String(255), nullable=False);


    def __init__(self, nome, telefone, email, senha):
        self.status = True;
        self.telefone = telefone;
        self.nome = nome;
        self.email= email;
        self.senha = senha;
    
    





