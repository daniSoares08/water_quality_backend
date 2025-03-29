from repositories.sensor_repository import SensorRepository

class SensorService:
    def __init__(self):
        self.repository = SensorRepository()
        # Tipos de sensor válidos
        self.valid_types = {"ph", "temperatura", "turbidez", "tds"}

    def create_sensor(self, name: str, sensor_type: str, location: str = None, status: str = "ativo"):
        # Valida o tipo do sensor
        if sensor_type not in self.valid_types:
            return None
        if not status:
            status = "ativo"
        return self.repository.create(name, sensor_type, location, status)

    def get_sensor(self, sensor_id: int):
        return self.repository.get_by_id(sensor_id)

    def get_all_sensors(self):
        return self.repository.get_all()

    def update_sensor(self, sensor_id: int, name: str = None, sensor_type: str = None,
                      location: str = None, status: str = None):
        sensor = self.repository.get_by_id(sensor_id)
        if not sensor:
            return None
        # Mantém valores atuais se não fornecidos
        if name is None:
            name = sensor.name
        if sensor_type is None:
            sensor_type = sensor.sensor_type
        if location is None:
            location = sensor.location
        if status is None:
            status = sensor.status
        # Valida tipo se foi fornecido/alterado
        if sensor_type not in self.valid_types:
            return None
        return self.repository.update(sensor_id, name, sensor_type, location, status)

    def delete_sensor(self, sensor_id: int):
        return self.repository.delete(sensor_id)
