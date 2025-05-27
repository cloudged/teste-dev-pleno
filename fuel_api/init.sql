CREATE TABLE IF NOT EXISTS combustiveis (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE
);

INSERT INTO combustiveis (nome) VALUES 
('Etanol'),
('Gasolina'),
('Diesel')
ON CONFLICT DO NOTHING;
