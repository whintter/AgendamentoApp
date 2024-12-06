from banco.config_banco import db;
class Gerenciar():
    def __init__(self, classe_gerenciar, id_item):
        self._classe_gerenciar = classe_gerenciar;
        self._id_item = id_item;
    
    def delete(self, tipo_user):
        if tipo_user == "barber":
            self._classe_gerenciar.query.filter_by(id_barber=self._id_item).delete();
            db.session.commit();
        elif tipo_user == "cliente":
            self._classe_gerenciar.query.filter_by(id_cliente=self._id_item).delete();
            db.session.commit();
        
    def update(self):
        pass;
    def aceitar_cad(self):
        mudar_status = self._classe_gerenciar.query.filter_by(id_barber=self._id_item).first();
        mudar_status.status = "A";
        db.session.commit();
