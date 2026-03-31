from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 🔹 CONFIGURAÇÃO DO BANCO
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 🔹 MODEL
class Jogo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)

# 🔹 CRIAR BANCO
with app.app_context():
    db.create_all()

# 🔹 HOME
@app.route('/')
def home():
    return "API de Jogos funcionando 🚀"


# ✅ GET - listar todos
@app.route('/jogos', methods=['GET'])
def listar():
    jogos = Jogo.query.all()
    return jsonify([
        {"id": j.id, "nome": j.nome, "genero": j.genero, "preco": j.preco}
        for j in jogos
    ]), 200


# ✅ GET por ID
@app.route('/jogos/<int:id>', methods=['GET'])
def buscar(id):
    jogo = db.session.get(Jogo, id)

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    return jsonify({
        "id": jogo.id,
        "nome": jogo.nome,
        "genero": jogo.genero,
        "preco": jogo.preco
    }), 200


# ✅ POST
@app.route('/jogos', methods=['POST'])
def criar():
    dados = request.get_json()

    if not dados or not all(k in dados for k in ('nome', 'genero', 'preco')):
        return jsonify({"erro": "Dados inválidos"}), 400

    novo = Jogo(
        nome=dados['nome'],
        genero=dados['genero'],
        preco=dados['preco']
    )

    db.session.add(novo)
    db.session.commit()

    return jsonify({"mensagem": "Jogo criado com sucesso"}), 201


# ✅ PUT
@app.route('/jogos/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    jogo = db.session.get(Jogo, id)

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    jogo.nome = dados.get('nome', jogo.nome)
    jogo.genero = dados.get('genero', jogo.genero)
    jogo.preco = dados.get('preco', jogo.preco)

    db.session.commit()

    return '', 204


# ✅ DELETE
@app.route('/jogos/<int:id>', methods=['DELETE'])
def deletar(id):
    jogo = db.session.get(Jogo, id)

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    db.session.delete(jogo)
    db.session.commit()

    return '', 204


# 🚀 EXECUÇÃO FORÇADA
print("INICIANDO SERVIDOR...")

app.run(host='0.0.0.0', port=5000, debug=True)