from banco.config_banco import db;
class User(db.Model):
    __abstract__ = True 
    nome = db.Column(db.String(255), nullable=False);
    telefone = db.Column(db.String(15), nullable=False);
    email = db.Column(db.String(255), nullable=False);
    senha = db.Column(db.String(255), nullable=False);

    def __init__(self, nome,telefone,email, senha):
        self.nome = nome;
        self.telefone = telefone;
        self.email = email;
        self.senha = senha;
  