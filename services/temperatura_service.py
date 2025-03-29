from datetime import datetime
from repositories.temperatura_repository import TemperaturaRepository
from repositories.sensor_repository import SensorRepository

class TemperaturaService:
    def __init__(self):
        self.repository = TemperaturaRepository()
        self.sensor_repository = SensorRepository()
        self.param_type = "temperatura"

    def get_all_readings(self, sensor_id: int = None):
        return self.repository.get_all(sensor_id)

    def get_latest_reading(self, sensor_id: int = None):
        return self.repository.get_latest(sensor_id)

    def get_reading_by_id(self, reading_id: int):
        return self.repository.get_by_id(reading_id)

    def add_reading(self, sensor_id: int, value: float, timestamp: str = None):
        sensor = self.sensor_repository.get_by_id(sensor_id)
        if not sensor or sensor.sensor_type != self.param_type:
            return None
        if timestamp is None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return self.repository.create(sensor_id, value, timestamp)

    def delete_reading(self, reading_id: int):
        return self.repository.delete(reading_id)
