from banco.config_banco import db;
from models.baber import Barber
class Servicos(db.Model):
    __tablename__="servicos";
    id_servico =  db.Column(db.Integer, primary_key=True, autoincrement=True);
    nome = db.Column(db.String(255), nullable=False);
    descricao = db.Column(db.String(255), nullable=False);
    valor = db.Column(db.Numeric(10, 2), nullable=True);   
    status = db.Column(db.String(1), nullable=False);

    fk_id_barber = db.Column(db.Integer, db.ForeignKey('barbearia.id_barber'), nullable=False)

    def __init__(self,nome,descricao,valor,fk_id_barber):
        self.nome = nome;
        self.descricao = descricao;
        self.valor = valor;
        self.status = "A";
        self.fk_id_barber = fk_id_barber;
    @staticmethod
    def listar_servicos( id_barber):
        list_servicos = Servicos.query.filter_by(fk_id_barber=id_barber).all();
        return list_servicos;