from models.usuarios import User;
from banco.config_banco import db;
#uso de heranca
#uso de polimorfismo no get_info 
class Barber(User):
    __tablename__ = 'barbearia';
    id_barber = db.Column(db.Integer, primary_key=True, autoincrement=True);
    descricao = db.Column(db.Text, nullable=True); descricao = db.Column(db.Text, nullable=True);
    logradouro = db.Column(db.Text, nullable=True);
    cidade = db.Column(db.Text, nullable=True);
    bairro = db.Column(db.Text, nullable=True);
    numero = db.Column(db.Text, nullable=True);
    status = db.Column(db.Text, nullable = False);
    servicos = db.relationship('Servicos', backref='barber', lazy=True);
    agendamento = db.relationship('Agendamento', backref='barber', lazy=True);

    def __init__(self, nome, telefone, email, senha):
        super().__init__(nome, telefone, email, senha);
        self.status ="P"; #status deve ser P para pendente ou A para ativo, deve ser usado para saber se a barbearua foi aceita pelo administrador
   
    @staticmethod
    def listar_barbearia():
        lista_babearias = Barber.query.order_by(Barber.id_barber).all();    
        return lista_babearias;

    def add_infos (self, descricao,logradouro,cidade,bairro,numero, email_update):
        Barber.query.filter_by(email=email_update).update({
            "cidade": cidade,
            "descricao":descricao,
            "logradouro":logradouro,
            "bairro":bairro,
            "numero":numero
            })
        db.session.commit();
    
    @staticmethod
    def get_infos(**kwargs):
        query = Barber.query;

        for key, value in kwargs.items():
            query = query.filter(getattr(Barber, key) == value)
            
        result = query.first()
        return result
    
    def validar_dados(self):
        if not self.senha:
            raise ValueError("A senha do barbeiro(a) é obrigatória")
        if not self.email:
            raise ValueError("O email do barbeiro(a) é obrigatório")

    def salvar(self):
        self.validar_dados()
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def buscar_todos():
        return Barber.query.all()

    @staticmethod
    def buscar_por_id(barber_id):
        return Barber.query.get(barber_id)
