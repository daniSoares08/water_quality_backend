class Sensor:
    def __init__(self, id: int, name: str, sensor_type: str, location: str, status: str):
        self.id = id
        self.name = name
        self.sensor_type = sensor_type
        self.location = location
        self.status = status

    def to_dict(self) -> dict:
        """Converte o objeto Sensor para um dicionário."""
        return {
            "id": self.id,
            "name": self.name,
            "type": self.sensor_type,
            "location": self.location,
            "status": self.status
        }
