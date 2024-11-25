from models.agendamento import Agendamento;
from models.clientes import Cliente;
from models.autenticar import Autenticar;
from flask import Flask, render_template, request, redirect;
from flask_sqlalchemy import SQLAlchemy;
from banco.config_banco import db;

#informacoes do banco de dados, conexao, etc
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD="mysql+mysqlconnector", 
        usuario="root",
        senha="",
        servidor="localhost",
        database="agendamento"
    )
db.init_app(app)
#fim db

#Login comeco 
@app.route("/login", methods=["POST","GET"])
def login():
    return render_template("login.html");

@app.route("/autenticar",methods=["POST","GET"])
def autenticar():
    #Pega informacoes do input do html
    lista_clientes = Cliente.query.order_by(Cliente.id_cliente)
    email = request.form.get('Email');
    senha = request.form.get('Senha');
    #autentica o login pela classe autenticar
    Autenticacao1 = Autenticar(email,senha);
    Autenticacao1.autenticacao();

    if Autenticacao1._status:
        return redirect("/index");
    elif not Autenticacao1._status:
        return render_template("login.html", lista = lista_clientes, login_falhou ="True"); 
#FIM LOGIN

#comeco do cadastro
@app.route("/cadastro",methods=["POST","GET"])
def cadastro():
    return render_template("cadastro.html", falha = None);    

@app.route('/cadastrar', methods=["POST","GET"])
def cadastrar():
    # atribuicao das variaveis pegando do input do cadastro.html
    nome_cadastrado = request.form.get('Nome');
    email_cadastrado = request.form.get("Email");
    telefone_cadastrado = request.form.get('Telefone');
    senha_cadastrada = request.form.get('Senha');

    #verifica se os campos estao vazio 
    if nome_cadastrado and email_cadastrado and telefone_cadastrado and senha_cadastrada:
        #filtra no banco se tem email ou telefone repetido, para nao deixar que aconteca a criacao do  usuario
        cliente_existente = Cliente.query.filter((Cliente.email == email_cadastrado) | (Cliente.telefone == telefone_cadastrado)).first()

        if cliente_existente:
            return render_template("cadastro.html", falha = True);
        else:
            cliente_cadastrado = Cliente(nome=nome_cadastrado,telefone=telefone_cadastrado,email=email_cadastrado,senha=senha_cadastrada);
            db.session.add(cliente_cadastrado);
            db.session.commit();
            return render_template("cadastro.html", falha = False);
    else: #se os campos de cadastro forem vazios vai aparecer um alert no Html
        return render_template("cadastro.html", falha = True);
#fim cadastro

#inicio home 
@app.route("/index")
def index():
    return render_template("index.html");

app.run(debug=True);   