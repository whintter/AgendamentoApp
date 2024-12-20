from models.clientes import Cliente;
from banco.config_banco import db;
class Agendamento(db.Model):
   #uso de associacao de agendamento com barber e cliente 
   #Heranca
   #SOLID 
    __tablename__ = 'agendamentos'
    __table_args__ = {'extend_existing': True}  # Adicionando para evitar redefinir a tabela

    id_agendamento = db.Column(db.Integer, primary_key=True, autoincrement=True);
    data = db.Column(db.Date, nullable=False);
    hora = db.Column(db.String(5), nullable=False); # Formato 'HH:MM'
    fk_id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente', ondelete='CASCADE'));
    fk_id_barber = db.Column(db.Integer, db.ForeignKey('barbearia.id_barber', ondelete='CASCADE'));
    status = db.Column(db.CHAR(1), nullable=False) ; # 'P' para pendente,  A para ativo 'C' para concluído, etc.


    cliente = db.relationship('Cliente', backref='agendamentos') 
    barber = db.relationship('Barber', backref='agendamentos_barber', lazy=True)


    def __init__(self, data, hora, fk_id_cliente, fk_id_barber):
        self.data = data
        self.hora = hora
        self.fk_id_cliente = fk_id_cliente
        self.fk_id_barber = fk_id_barber
        self.status ='P'

    @staticmethod
    def lista_agendamento(id_barber):
        return Agendamento.query.filter_by(fk_id_barber=id_barber).all()

    @staticmethod
    def listar_pendentes(id_barber):
        return Agendamento.query.filter_by(fk_id_barber=id_barber, status="P").all()
    
    def mudar_status(self):
        self.status = "A";
        db.session.commit()


