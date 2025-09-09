CREATE TABLE IF NOT EXISTS family (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    type VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO family (name, description, type) VALUES
('RF00001', 'tRNA family', 'Gene'),
('RF00002', 'microRNA family', 'Gene'),
('RF00003', 'rRNA family', 'Gene'),
('RF00004', 'snoRNA family', 'Gene'),
('RF00005', 'ribozyme family', 'Ribozyme');

CREATE TABLE IF NOT EXISTS family_stats (
    family_id INTEGER REFERENCES family(id),
    sequence_count INTEGER,
    avg_length DECIMAL(10,2),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO family_stats (family_id, sequence_count, avg_length) VALUES
(1, 150, 75.5),
(2, 89, 22.3),
(3, 1200, 1800.0),
(4, 45, 120.7),
(5, 12, 350.2);