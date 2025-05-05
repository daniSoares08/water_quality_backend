# 🌊 Water Quality Backend

Este é o backend de um sistema completo de monitoramento da qualidade da água, desenvolvido com **Flask (Python)**. Ele é responsável por receber, armazenar e fornecer dados de sensores como **pH**, **temperatura**, **oxigênio dissolvido** e **turbidez**, geralmente provenientes de um microcontrolador **ESP32** via requisições HTTP.

## 🚀 Tecnologias Utilizadas

- **Python 3.11+**
- **Flask**
- **MySQL** (banco relacional)
- **SQLAlchemy** (ORM)
- **Flask-CORS**
- **Flask-Migrate**
- **Gunicorn** (para produção)
- **Docker** (opcional para deploy)
- **Tailscale** (segurança opcional via VPN)

## 📦 Instalação

### Pré-requisitos

- Python instalado (recomendado 3.11 ou superior)
- MySQL rodando localmente ou remotamente
- (Opcional) Docker e Docker Compose

### Clonando o projeto

```bash
git clone https://github.com/daniSoares08/water_quality_backend.git
cd water_quality_backend
```

### Ambiente virtual e dependências

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### Variáveis de ambiente

Crie um arquivo `.env` com as seguintes variáveis:

```env
FLASK_ENV=development
SECRET_KEY=sua_chave_secreta
SQLALCHEMY_DATABASE_URI=mysql+pymysql://usuario:senha@host:porta/banco
```

### Migrando o banco de dados

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Executando localmente

```bash
flask run
```

## 📡 Estrutura da API

* `GET /api/sensores` — Lista sensores registrados
* `POST /api/leituras` — Recebe leitura dos sensores (via ESP32)
* `GET /api/leituras` — Retorna dados filtrados por sensor, data etc.
* `GET /api/dashboard` — Estatísticas e métricas agregadas

> A documentação completa da API está disponível em breve com Swagger ou Postman Collection.

## 🧠 Funcionalidades

* Integração direta com dispositivos IoT (como ESP32)
* Autenticação via token (em desenvolvimento)
* Armazenamento eficiente e consulta de dados ambientais
* Pronto para deploy com Gunicorn + Nginx + Docker

## 🛠️ Futuras melhorias

* Sistema de alertas e notificações (ex: níveis críticos de pH)
* Dashboard completo com gráficos (frontend Vue integrado)
* Exportação de dados (.CSV)
* Usuários e permissões

## 🤝 Contribuição

Contribuições são bem-vindas! Abra uma *issue* ou *pull request* com sugestões, correções ou melhorias.

## 👨‍💻 Autor

Desenvolvido por [Daniel Soares](https://www.linkedin.com/in/daniel-campos-soares-b47426238/)

* GitHub: [@daniSoares08](https://github.com/daniSoares08)
* Email: [campossoares.daniel@gmail.com](mailto:campossoares.daniel@gmail.com)
