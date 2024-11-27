from models.usuarios import User;
from banco.config_banco import db;
#uso de heranca
class Barber(User):
    __tablename__ = 'barbearia';
    id_barber = db.Column(db.Integer, primary_key=True, autoincrement=True);
    descricao = db.Column(db.Text, nullable=True);
    logradouro = db.Column(db.Text, nullable=True);
    cidade = db.Column(db.Text, nullable=True);
    bairro = db.Column(db.Text, nullable=True);
    numero = db.Column(db.Text, nullable=True);

    def __init__(self, nome, telefone, email, senha, descricao, logradouro, cidade, bairro, numero):
        super().__init__(nome, telefone, email, senha);
        self.descricao = descricao;
        self.logradouro = logradouro;
        self.cidade = cidade;
        self.bairro = bairro;
        self.numero = numero;

baber1= Barber(nome="baber",telefone="111",email="Barber@",senha="barber123");