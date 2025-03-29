from flask import Blueprint, request, jsonify
from services.temperatura_service import TemperaturaService

temperatura_bp = Blueprint('temperatura_api', __name__, url_prefix='/temperatura')
temperatura_service = TemperaturaService()

@temperatura_bp.route('', methods=['GET', 'POST'])
def handle_temperatura():
    if request.method == 'GET':
        sensor_id = request.args.get('sensor_id', default=None, type=int)
        latest = request.args.get('latest')
        if latest:
            reading = temperatura_service.get_latest_reading(sensor_id)
            if not reading:
                return jsonify({"error": "Nenhuma leitura de temperatura encontrada"}), 404
            return jsonify(reading.to_dict()), 200
        else:
            readings = temperatura_service.get_all_readings(sensor_id)
            return jsonify([r.to_dict() for r in readings]), 200
    elif request.method == 'POST':
        data = request.get_json() or {}
        sensor_id = data.get('sensor_id')
        value = data.get('value')
        timestamp = data.get('timestamp')
        if sensor_id is None or value is None:
            return jsonify({"error": "Campos 'sensor_id' e 'value' são obrigatórios"}), 400
        new_reading = temperatura_service.add_reading(int(sensor_id), float(value), timestamp)
        if not new_reading:
            return jsonify({"error": "Sensor não encontrado ou incompatível com temperatura"}), 400
        return jsonify(new_reading.to_dict()), 201

@temperatura_bp.route('/<int:reading_id>', methods=['GET'])
def get_temperatura_reading(reading_id):
    reading = temperatura_service.get_reading_by_id(reading_id)
    if not reading:
        return jsonify({"error": "Leitura de temperatura não encontrada"}), 404
    return jsonify(reading.to_dict()), 200

@temperatura_bp.route('/<int:reading_id>', methods=['DELETE'])
def delete_temperatura_reading(reading_id):
    deleted = temperatura_service.delete_reading(reading_id)
    if not deleted:
        return jsonify({"error": "Leitura de temperatura não encontrada"}), 404
    return '', 204
