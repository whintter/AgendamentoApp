from models.clientes import Cliente;
from banco.config_banco import db;

class Autenticar():
    def __init__(self,email, senha):
        self._email =email;
        self._senha = senha;
        self._status = False;
    
    def autenticacao(self):
        lista_clientes = Cliente.query.order_by(Cliente.id_cliente)
        for usuarios in lista_clientes:
            if usuarios.email == self._email and usuarios.senha == self._senha:
                self._status = True;
                
            else:
                continue;



