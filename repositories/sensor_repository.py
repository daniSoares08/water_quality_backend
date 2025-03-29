import sqlite3
from models.sensor import Sensor

class SensorRepository:
    def __init__(self, db_path: str = "data/sensors.db"):
        self.db_path = db_path

    def _connect(self):
        """Conecta ao banco de dados SQLite."""
        return sqlite3.connect(self.db_path)

    def get_all(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, type, location, status FROM sensor")
        rows = cursor.fetchall()
        conn.close()
        sensors = [Sensor(*row) for row in rows]
        return sensors

    def get_by_id(self, sensor_id: int):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, type, location, status FROM sensor WHERE id = ?", (sensor_id,))
        row = cursor.fetchone()
        conn.close()
        return Sensor(*row) if row else None

    def create(self, name: str, sensor_type: str, location: str = None, status: str = "ativo"):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sensor (name, type, location, status) VALUES (?, ?, ?, ?)",
            (name, sensor_type, location, status)
        )
        conn.commit()
        sensor_id = cursor.lastrowid
        conn.close()
        return Sensor(sensor_id, name, sensor_type, location, status)

    def update(self, sensor_id: int, name: str, sensor_type: str, location: str, status: str):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE sensor SET name = ?, type = ?, location = ?, status = ? WHERE id = ?",
            (name, sensor_type, location, status, sensor_id)
        )
        conn.commit()
        updated_rows = cursor.rowcount
        conn.close()
        return Sensor(sensor_id, name, sensor_type, location, status) if updated_rows > 0 else None

    def delete(self, sensor_id: int):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM sensor WHERE id = ?", (sensor_id,))
        deleted_rows = cursor.rowcount
        conn.commit()
        conn.close()
        return deleted_rows > 0
