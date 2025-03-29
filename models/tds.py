class Tds:
    def __init__(self, id: int, sensor_id: int, value: float, timestamp: str):
        self.id = id
        self.sensor_id = sensor_id
        self.value = value
        self.timestamp = timestamp

    def to_dict(self) -> dict:
        """Converte a leitura de TDS para um dicionário."""
        return {
            "id": self.id,
            "sensor_id": self.sensor_id,
            "value": self.value,
            "timestamp": self.timestamp
        }
