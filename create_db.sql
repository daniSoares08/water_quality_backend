-- Script SQL para criar o banco de dados SQLite (compatível com MySQL Workbench)
-- Remove tabelas existentes, se houver (reset do banco)
DROP TABLE IF EXISTS tds;
DROP TABLE IF EXISTS turbidez;
DROP TABLE IF EXISTS temperatura;
DROP TABLE IF EXISTS ph;
DROP TABLE IF EXISTS sensor;

-- Criação da tabela de sensores
CREATE TABLE sensor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    location TEXT,
    status TEXT NOT NULL DEFAULT 'ativo'
);

-- Criação das tabelas de histórico para cada parâmetro
CREATE TABLE ph (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_id INTEGER NOT NULL,
    value REAL NOT NULL,
    timestamp TEXT NOT NULL,
    FOREIGN KEY(sensor_id) REFERENCES sensor(id) ON DELETE CASCADE
);

CREATE TABLE temperatura (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_id INTEGER NOT NULL,
    value REAL NOT NULL,
    timestamp TEXT NOT NULL,
    FOREIGN KEY(sensor_id) REFERENCES sensor(id) ON DELETE CASCADE
);

CREATE TABLE turbidez (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_id INTEGER NOT NULL,
    value REAL NOT NULL,
    timestamp TEXT NOT NULL,
    FOREIGN KEY(sensor_id) REFERENCES sensor(id) ON DELETE CASCADE
);

CREATE TABLE tds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_id INTEGER NOT NULL,
    value REAL NOT NULL,
    timestamp TEXT NOT NULL,
    FOREIGN KEY(sensor_id) REFERENCES sensor(id) ON DELETE CASCADE
);

-- Inserção de sensores iniciais (dados simulados)
INSERT INTO sensor (name, type, location, status) VALUES
('Sensor de pH - 1', 'ph', 'Reservatório A', 'ativo'),
('Sensor de Temperatura - 1', 'temperatura', 'Reservatório A', 'ativo'),
('Sensor de Turbidez - 1', 'turbidez', 'Reservatório A', 'ativo'),
('Sensor de TDS - 1', 'tds', 'Reservatório A', 'inativo');

-- Inserção de leituras históricas simuladas para cada sensor
-- Leituras de pH (sensor_id = 1)
INSERT INTO ph (sensor_id, value, timestamp) VALUES
(1, 6.5, '2025-03-25 08:00:00'),
(1, 6.7, '2025-03-25 09:00:00'),
(1, 6.8, '2025-03-25 10:00:00'),
(1, 7.0, '2025-03-25 11:00:00'),
(1, 7.2, '2025-03-25 12:00:00');

-- Leituras de Temperatura (sensor_id = 2)
INSERT INTO temperatura (sensor_id, value, timestamp) VALUES
(2, 20.0, '2025-03-25 08:00:00'),
(2, 20.5, '2025-03-25 09:00:00'),
(2, 21.0, '2025-03-25 10:00:00'),
(2, 21.2, '2025-03-25 11:00:00'),
(2, 21.4, '2025-03-25 12:00:00');

-- Leituras de Turbidez (sensor_id = 3)
INSERT INTO turbidez (sensor_id, value, timestamp) VALUES
(3, 1.0, '2025-03-25 08:00:00'),
(3, 2.0, '2025-03-25 09:00:00'),
(3, 5.0, '2025-03-25 10:00:00'),
(3, 3.0, '2025-03-25 11:00:00'),
(3, 4.0, '2025-03-25 12:00:00');

-- Leituras de TDS (sensor_id = 4)
INSERT INTO tds (sensor_id, value, timestamp) VALUES
(4, 300.0, '2025-03-25 08:00:00'),
(4, 320.0, '2025-03-25 09:00:00'),
(4, 310.0, '2025-03-25 10:00:00'),
(4, 330.0, '2025-03-25 11:00:00'),
(4, 340.0, '2025-03-25 12:00:00');
