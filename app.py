from models.agendamento import Agendamento;
from models.clientes import Cliente;
from models.autenticar import Autenticar;
from models.baber import Barber;
from models.servicos import Servicos;
from models.gerenciar_users import Gerenciar;
from flask import Flask, render_template, request, redirect,url_for, session,flash;
from flask_sqlalchemy import SQLAlchemy;
from banco.config_banco import db;

from models.dados import ServicoHelper, No,ListaLigada, FilaAtendimentos,ArvoreBinaria,NoArvore


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
app.secret_key="34b19cbe42cb947073759f8e5f993d82";
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
    tipo_conta = request.form.get('tipo_login');

    #autentica o login pela classe autenticar
    if tipo_conta:
        if tipo_conta == "cliente":
            Autenticacao1 = Autenticar(email,senha);
            Autenticacao1.autenticacao_cliente();

            if Autenticacao1._status:
                get_name = Cliente.get_infos(email,"nome");
                return redirect(url_for("home_cliente", name = get_name,get_email_cliente = email));
            elif not Autenticacao1._status:
                return render_template("login.html", lista = lista_clientes, login_falhou ="True"); 
        
        elif tipo_conta == "barber":
            Autenticacao1 = Autenticar(email,senha);
            Autenticacao1.autenticacao_baber();

            if Autenticacao1._status:
                if Autenticacao1._pendente:
                    return render_template("login.html", lista = lista_clientes, pendente ="True"); 
                else:
                    return redirect(url_for("barber_home",Email_barber = email));
                    
            elif not Autenticacao1._status:
                return render_template("login.html", lista = lista_clientes, login_falhou ="True"); 
        elif tipo_conta == "admin":
            Autenticacao1 = Autenticar(email,senha);
            Autenticacao1.autenticacao_admin();

            if Autenticacao1._status:
                return redirect("/home_admin");
            elif not Autenticacao1._status:
                return render_template("login.html", lista = lista_clientes, login_falhou ="True"); 
    return render_template("login.html", lista=lista_clientes,login_falhou="True");
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
        cliente_existente = Cliente.query.filter((Cliente.email == email_cadastrado) | (Cliente.telefone == telefone_cadastrado)).first();
        barber_existente = Barber.query.filter((Barber.email == email_cadastrado)|(Barber.telefone == telefone_cadastrado)).first();
        tipo_cad = request.form.get('tipo_cad');

        if cliente_existente or barber_existente:
            return render_template("cadastro.html", falha = True);
        else:
            if tipo_cad and tipo_cad=="cliente": 
                cliente_cadastrado = Cliente(nome=nome_cadastrado,telefone=telefone_cadastrado,email=email_cadastrado,senha=senha_cadastrada);
                db.session.add(cliente_cadastrado);
                db.session.commit();
                return render_template("cadastro.html", falha = False);
        
            elif tipo_cad and tipo_cad =="barber":
                barber_cadastrado = Barber(nome=nome_cadastrado,telefone=telefone_cadastrado,email=email_cadastrado,senha=senha_cadastrada);
                db.session.add(barber_cadastrado);
                db.session.commit();
                return render_template("cadastro.html", falha = False);
            else:
                return render_template("cadastro.html", falha = True,teste =tipo_cad);
    else: #se os campos de cadastro forem vazios vai aparecer um alert no Html
        return render_template("cadastro.html", falha = True);
#fim cadastro

#inicio home cliente
@app.route("/home_cliente/<string:name>")
def home_cliente(name):
    lista_barber = Barber.listar_barbearia();
    email_ = request.args.get("get_email_cliente");
    return render_template("home_cliente.html", nome = name, list = lista_barber, email_cliente = email_);

@app.route("/view_barber/<int:id>")
def view_barber(id):
    get_barber_infos = Barber.get_infos(id_barber = id);
    lista_servicos = Servicos.listar_servicos(id_barber=id); 
    arvore_servicos = ArvoreBinaria()
    for servico in lista_servicos:
        arvore_servicos.adicionar({
            'id': servico.id_servico,
            'nome': servico.nome,
            'valor': servico.valor,
            'descricao': servico.descricao
        })
    servicos_ordenados = arvore_servicos.listar_ordenado()
    email_ = request.args.get("get_email_cliente");
    return render_template("view_barber.html", info_barber = get_barber_infos,  id_barber = id, email_cliente = email_, service=servicos_ordenados);
    #fim home cliente

@app.route("/agendamento", methods=["POST","GET"])
def agendamento():
    data_agendamento = request.form.get("data_agendamento");
    horario_agendamento  = request.form.get("horario_agendamento");
    get_id_barber  = request.form.get("id_barber1");
    get_email_cliente =  request.form.get("email_cliente");
    if get_email_cliente :
        get_id_cliente = Cliente.get_infos(get_email_cliente,"id_cliente");
        agendamento1= Agendamento(data=data_agendamento,hora=horario_agendamento,fk_id_cliente=get_id_cliente,fk_id_barber=get_id_barber);
        db.session.add(agendamento1);
        db.session.commit();
        flash("agendamento feito com sucesso!!");
        return redirect(url_for("view_barber",id=get_id_barber));   


    else:
        return redirect('/login')

#inicio home admin
@app.route("/home_admin",methods =["POST","GET"])
def home_admin():
    listar = Barber.listar_barbearia();
    return render_template("home_admin.html",lista = listar);

@app.route("/manage_barber/<int:id>/<string:acept>/<string:delete>",methods =["POST","GET"])
def manage_barber(id, acept,delete):

    id_barber = id;
    acept_cad = acept;
    delete_cad = delete;
    if acept_cad=="True":
        aceitar_barber1 = Gerenciar(Barber,id_barber);
        aceitar_barber1.aceitar_cad();
        flash('Status da barbearia alterado com sucesso')
        return redirect(url_for('home_admin'));
    elif delete_cad == "True":
        delete_barber1 = Gerenciar(Barber, id_barber);
        delete_barber1.delete("barber");
        return redirect(url_for('home_admin'));
    else:
        return redirect(url_for('home_admin'));
#fim home admin

#inicio home barbearia
@app.route("/barber_home", methods=["POST", "GET"])
def barber_home():
    email_barber = request.args.get('Email_barber')  # Pega o email passado pela URL
    infos_cadastradas = Barber.query.filter(Barber.email == email_barber).filter(Barber.descricao.is_(None)).first()
    session['email'] = email_barber
    list = Barber.get_infos(email=session['email'])
    list_agendamento = Agendamento.lista_agendamento(list.id_barber)

    fila_atendimentos = FilaAtendimentos()
    agendamentos_pendentes = Agendamento.listar_pendentes(list.id_barber)

    for agendamento in agendamentos_pendentes:
        fila_atendimentos.adicionar_agendamento(agendamento)
    return render_template(
        "home_barber.html", 
        email_ = email_barber, 
        lista_agendamento = list_agendamento, 
        fila_pendentes=fila_atendimentos.obter_agendamentos(), 
        infos_false = infos_cadastradas
    )


@app.route("/cad_infos",methods =["POST","GET"])
def cad_infos():
    infos_adc = request.args.get("adic_infos");
    email_ = request.form.get('email');
    Cidade= request.form.get('Cidade');
    Rua = request.form.get('Rua');
    Bairro = request.form.get('Bairro');
    Numero = request.form.get('Numero');
    Descricao = request.form.get('Descricao');
    barbearia = Barber.query.filter_by(email = email_ ).first();

    if barbearia:
        barbearia.add_infos(Descricao, Rua,Cidade,Bairro,Numero,email_);
        return render_template("home_barber.html", infos_adc = True, email1_ = email_ );
    else:
        return render_template("home_barber.html", infos_adc = None);

@app.route("/cad_servicos",methods =["POST","GET"])
def cad_servicos():
    email_barber = session.get('email');
    nome_servico = request.form.get('nome_servico');
    valor_servico =  request.form.get('valor');
    descricao_servico =  request.form.get('Descricao');
    if email_barber and nome_servico and valor_servico and descricao_servico:
        barber_ = Barber.get_infos(email = email_barber)
        add_servico= Servicos(nome=nome_servico,descricao=descricao_servico, valor=valor_servico,fk_id_barber=barber_.id_barber);
        db.session.add(add_servico);
        db.session.commit();
        flash(f"Serviço Cadastrado com Sucesso");
    return render_template("home_barber.html");

@app.route("/mudar_status", methods=["GET", "POST"])
def mudar_status():
    email_barber =  session['email'];
    id_barber = Barber.get_infos(email=session.get("email")).id_barber
    proximo_agendamento = Agendamento.query.filter_by(fk_id_barber=id_barber, status="P").first()
    if proximo_agendamento.status == "P": 
            proximo_agendamento.status = "A";
            db.session.commit()
            flash(f"Status do agendamento alterado!")
        
    else:
        flash("Agendamento não encontrado!")

    return redirect(url_for("barber_home",Email_barber = session['email']))  


app.run(debug=True);   