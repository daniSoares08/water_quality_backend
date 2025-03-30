from flask import Flask
from flask_cors import CORS
from flask import Flask, request, jsonify, make_response
from api.sensor_api import sensor_bp
from api.ph_api import ph_bp
from api.temperatura_api import temperatura_bp
from api.turbidez_api import turbidez_bp
from api.tds_api import tds_bp

app = Flask(__name__)
# Registrar os blueprints para sensores e parâmetros
app.register_blueprint(sensor_bp)
app.register_blueprint(ph_bp)
app.register_blueprint(temperatura_bp)
app.register_blueprint(turbidez_bp)
app.register_blueprint(tds_bp)

CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
