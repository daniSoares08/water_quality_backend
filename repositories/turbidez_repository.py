import sqlite3
from models.turbidez import Turbidez

class TurbidezRepository:
    def __init__(self, db_path: str = "data/sensors.db"):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def get_all(self, sensor_id: int = None):
        conn = self._connect()
        cursor = conn.cursor()
        if sensor_id is not None:
            cursor.execute(
                "SELECT id, sensor_id, value, timestamp FROM turbidez WHERE sensor_id = ? ORDER BY timestamp ASC",
                (sensor_id,)
            )
        else:
            cursor.execute("SELECT id, sensor_id, value, timestamp FROM turbidez ORDER BY timestamp ASC")
        rows = cursor.fetchall()
        conn.close()
        return [Turbidez(*row) for row in rows]

    def get_by_id(self, reading_id: int):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, sensor_id, value, timestamp FROM turbidez WHERE id = ?", (reading_id,))
        row = cursor.fetchone()
        conn.close()
        return Turbidez(*row) if row else None

    def get_latest(self, sensor_id: int = None):
        conn = self._connect()
        cursor = conn.cursor()
        if sensor_id is not None:
            cursor.execute(
                "SELECT id, sensor_id, value, timestamp FROM turbidez WHERE sensor_id = ? ORDER BY timestamp DESC LIMIT 1",
                (sensor_id,)
            )
        else:
            cursor.execute("SELECT id, sensor_id, value, timestamp FROM turbidez ORDER BY timestamp DESC LIMIT 1")
        row = cursor.fetchone()
        conn.close()
        return Turbidez(*row) if row else None

    def create(self, sensor_id: int, value: float, timestamp: str):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO turbidez (sensor_id, value, timestamp) VALUES (?, ?, ?)",
            (sensor_id, value, timestamp)
        )
        conn.commit()
        reading_id = cursor.lastrowid
        conn.close()
        return Turbidez(reading_id, sensor_id, value, timestamp)

    def delete(self, reading_id: int):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM turbidez WHERE id = ?", (reading_id,))
        deleted_rows = cursor.rowcount
        conn.commit()
        conn.close()
        return deleted_rows > 0
