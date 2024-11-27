from models.clientes import Cliente;
from models.baber import Barber;
from banco.config_banco import db;

class Autenticar():
    def __init__(self,email, senha):
        self._email =email;
        self._senha = senha;
        self._status = False;
    
    def autenticacao_cliente(self):
        lista_clientes = Cliente.query.order_by(Cliente.id_cliente);
        for usuarios in lista_clientes:
            if usuarios.email == self._email and usuarios.senha == self._senha:
                self._status = True;
                
            else:
                continue;
    
    def autenticacao_baber(self):
        lista_babearia = Barber.query.order_by(Barber.id_barber);
        for usuarios in lista_babearia:
            if usuarios.email == self._email and usuarios.senha == self._senha:
                self._status = True;
                
            else:
                continue;



