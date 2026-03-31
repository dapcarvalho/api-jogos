# 🎮 API de Jogos - Flask + SQLAlchemy

API RESTful para gerenciamento de jogos, desenvolvida com Python, Flask e SQLAlchemy.

---

## 🚀 Funcionalidades

* ✔️ Listar todos os jogos
* ✔️ Buscar jogo por ID
* ✔️ Criar novo jogo
* ✔️ Atualizar jogo existente
* ✔️ Remover jogo
* ✔️ Validação de dados
* ✔️ Retorno em JSON

---

## 🛠️ Tecnologias utilizadas

* Python
* Flask
* Flask-SQLAlchemy
* SQLite

---

## 📁 Estrutura do projeto

```
api-jogos/
│
└── app.py
```

---

## ⚙️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone <SEU_LINK_AQUI>
cd api-jogos
```

---

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

---

### 3. Ativar ambiente

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

### 4. Instalar dependências

```bash
pip install flask flask_sqlalchemy
```

---

### 5. Executar a aplicação

```bash
python app.py
```

A API estará disponível em:

```
http://127.0.0.1:5000
```

---

## 🧪 Testes com CURL

### ➕ Criar jogo

```bash
curl -X POST http://127.0.0.1:5000/jogos \
-H "Content-Type: application/json" \
-d "{\"nome\":\"FIFA\",\"genero\":\"Esporte\",\"preco\":200}"
```

---

### 📄 Listar jogos

```bash
curl http://127.0.0.1:5000/jogos
```

---

### 🔍 Buscar jogo por ID

```bash
curl http://127.0.0.1:5000/jogos/1
```

---

### ✏️ Atualizar jogo

```bash
curl -X PUT http://127.0.0.1:5000/jogos/1 \
-H "Content-Type: application/json" \
-d "{\"nome\":\"FIFA 24\",\"genero\":\"Esporte\",\"preco\":250}"
```

---

### ❌ Remover jogo

```bash
curl -X DELETE http://127.0.0.1:5000/jogos/1
```

---

## 📌 Padrões utilizados

* API REST
* Métodos HTTP (GET, POST, PUT, DELETE)
* Status HTTP corretos (200, 201, 204, 404)
* JSON para comunicação

---

## 🎯 Critérios atendidos

✔ CRUD completo
✔ Padrão REST & JSON
✔ Organização do código
✔ Uso de banco de dados (SQLite)
✔ Tratamento de erros

---

## 💡 Diferencial

Uso de ORM com SQLAlchemy para melhor organização e manipulação do banco de dados.

---

## 👩‍💻 Autor

Daphne Cristine de Sá Carvalho

---
