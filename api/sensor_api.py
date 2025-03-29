from flask import Blueprint, request, jsonify
from services.sensor_service import SensorService

sensor_bp = Blueprint('sensor_api', __name__, url_prefix='/sensors')
sensor_service = SensorService()

@sensor_bp.route('', methods=['GET', 'POST'])
def handle_sensors():
    if request.method == 'GET':
        # Lista todos os sensores
        sensors = sensor_service.get_all_sensors()
        return jsonify([s.to_dict() for s in sensors]), 200
    elif request.method == 'POST':
        data = request.get_json() or {}
        name = data.get('name')
        sensor_type = data.get('type')
        location = data.get('location')
        status = data.get('status')
        if not name or not sensor_type:
            return jsonify({"error": "Campos 'name' e 'type' são obrigatórios"}), 400
        new_sensor = sensor_service.create_sensor(name, sensor_type, location, status)
        if not new_sensor:
            return jsonify({"error": "Tipo de sensor inválido (use ph, temperatura, turbidez ou tds)"}), 400
        return jsonify(new_sensor.to_dict()), 201

@sensor_bp.route('/<int:sensor_id>', methods=['GET'])
def get_sensor(sensor_id):
    sensor = sensor_service.get_sensor(sensor_id)
    if not sensor:
        return jsonify({"error": "Sensor não encontrado"}), 404
    return jsonify(sensor.to_dict()), 200

@sensor_bp.route('/<int:sensor_id>', methods=['PUT'])
def update_sensor(sensor_id):
    sensor = sensor_service.get_sensor(sensor_id)
    if not sensor:
        return jsonify({"error": "Sensor não encontrado"}), 404
    data = request.get_json() or {}
    name = data.get('name')
    sensor_type = data.get('type')
    location = data.get('location')
    status = data.get('status')
    if sensor_type and sensor_type not in sensor_service.valid_types:
        return jsonify({"error": "Tipo de sensor inválido"}), 400
    updated = sensor_service.update_sensor(sensor_id, name, sensor_type, location, status)
    if not updated:
        return jsonify({"error": "Falha ao atualizar sensor"}), 400
    return jsonify(updated.to_dict()), 200

@sensor_bp.route('/<int:sensor_id>', methods=['DELETE'])
def delete_sensor(sensor_id):
    deleted = sensor_service.delete_sensor(sensor_id)
    if not deleted:
        return jsonify({"error": "Sensor não encontrado"}), 404
    return '', 204
