from models.clientes import Cliente;
from banco.config_banco import db;
from models.baber import Barber

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'

    id_agendamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.Date, nullable=False)
    hora = db.Column(db.String(5), nullable=False)  # Formato 'HH:MM'
    fk_id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente', ondelete='CASCADE'))
    fk_id_barber = db.Column(db.Integer, db.ForeignKey('barbearia.id_barber', ondelete='CASCADE'))
    status = db.Column(db.CHAR(1), nullable=False)  # 'P' para pendente, 'C' para concluído, etc.

    # Relacionamentos
    cliente = db.relationship("Cliente", backref="agendamentos")
    barber = db.relationship("Barbearia", backref="agendamentos")

    def __init__(self, data, hora, fk_id_cliente, fk_id_barber):
        self.data = data
        self.hora = hora
        self.fk_id_cliente = fk_id_cliente
        self.fk_id_barber = fk_id_barber
        self.status ="P"
    
    # @staticmethod
    # def listar_agenda():
    #     print(f'{'Cliente'.ljust(25)}| {'Horário'.ljust(25)}| Status');
    #     for horario in Agendamento.agenda:
    #         print(f'{str(horario._cliente).ljust(25)}| {horario._horario.ljust(25)}| {horario._status}');
    
    # def confirmar_agendamento(self):
    #     self._status = "confirmado";
    
    # def cancelar_agendamento(self):
    #     self._status ="cancelado";
    
    # def alterar_horario(self,novo_horario):
    #     self._horario = novo_horario;
    
    # def adicionar_cliente(self, nome,cpf,telefone):
    #     cliente_add = Cliente(nome,telefone,cpf);
    #     self._cliente.append(cliente_add.mostrar_nome());
    


