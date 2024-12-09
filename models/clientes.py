from banco.config_banco import db;
from models.usuarios import User;
#uso de polimorfismo no get_info 
#criscso do cliente
class Cliente(User):
    #criacao no banco de dados 
    __tablename__ = 'cliente';
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True);
    agendamento = db.relationship('Agendamento', backref='clientes', lazy=True);

    def __init__(self, nome, telefone, email, senha):
        super().__init__(nome,telefone, email, senha);
    
    @staticmethod
    def get_infos(email_cliente, info_):
        get_infos = Cliente.query.filter_by(email=email_cliente).first();
        info_want = getattr(get_infos,info_);
        return info_want;






