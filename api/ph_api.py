from flask import Blueprint, request, jsonify
from services.ph_service import PhService

ph_bp = Blueprint('ph_api', __name__, url_prefix='/ph')
ph_service = PhService()

@ph_bp.route('', methods=['GET', 'POST'])
def handle_ph():
    if request.method == 'GET':
        sensor_id = request.args.get('sensor_id', default=None, type=int)
        latest = request.args.get('latest')
        if latest:
            # Retorna o último valor de pH
            reading = ph_service.get_latest_reading(sensor_id)
            if not reading:
                return jsonify({"error": "Nenhuma leitura de pH encontrada"}), 404
            return jsonify(reading.to_dict()), 200
        else:
            # Retorna histórico de leituras (possivelmente filtrado por sensor_id)
            readings = ph_service.get_all_readings(sensor_id)
            return jsonify([r.to_dict() for r in readings]), 200
    elif request.method == 'POST':
        data = request.get_json() or {}
        sensor_id = data.get('sensor_id')
        value = data.get('value')
        timestamp = data.get('timestamp')
        if sensor_id is None or value is None:
            return jsonify({"error": "Campos 'sensor_id' e 'value' são obrigatórios"}), 400
        new_reading = ph_service.add_reading(int(sensor_id), float(value), timestamp)
        if not new_reading:
            return jsonify({"error": "Sensor não encontrado ou incompatível com pH"}), 400
        return jsonify(new_reading.to_dict()), 201

@ph_bp.route('/<int:reading_id>', methods=['GET'])
def get_ph_reading(reading_id):
    reading = ph_service.get_reading_by_id(reading_id)
    if not reading:
        return jsonify({"error": "Leitura de pH não encontrada"}), 404
    return jsonify(reading.to_dict()), 200

@ph_bp.route('/<int:reading_id>', methods=['DELETE'])
def delete_ph_reading(reading_id):
    deleted = ph_service.delete_reading(reading_id)
    if not deleted:
        return jsonify({"error": "Leitura de pH não encontrada"}), 404
    return '', 204
