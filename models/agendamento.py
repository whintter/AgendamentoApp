from models.clientes import Cliente;
class Agendamento():
    agenda = [];
    def __init__(self, horario):
        self._status = "pendente";
        self._cliente = [];
        self._horario = horario;
        Agendamento.agenda.append(self);
    
    @staticmethod
    def listar_agenda():
        print(f'{'Cliente'.ljust(25)}| {'Horário'.ljust(25)}| Status');
        for horario in Agendamento.agenda:
            print(f'{str(horario._cliente).ljust(25)}| {horario._horario.ljust(25)}| {horario._status}');
    
    def confirmar_agendamento(self):
        self._status = "confirmado";
    
    def cancelar_agendamento(self):
        self._status ="cancelado";
    
    def alterar_horario(self,novo_horario):
        self._horario = novo_horario;
    
    def adicionar_cliente(self, nome,cpf,telefone):
        cliente_add = Cliente(nome,telefone,cpf);
        self._cliente.append(cliente_add.mostrar_nome());
    


