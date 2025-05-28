-- Criação das tabelas
CREATE TABLE IF NOT EXISTS combustivel (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS ref_compra (
    id SERIAL PRIMARY KEY,
    combustivel_id INTEGER NOT NULL REFERENCES combustivel(id),
    mes INTEGER NOT NULL CHECK (mes BETWEEN 1 AND 12),
    preco DECIMAL(10, 2) NOT NULL,
    tributo DECIMAL(5, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS ref_venda (
    id SERIAL PRIMARY KEY,
    combustivel_id INTEGER NOT NULL REFERENCES combustivel(id),
    mes INTEGER NOT NULL CHECK (mes BETWEEN 1 AND 12),
    preco DECIMAL(10, 2) NOT NULL,
    tributo DECIMAL(5, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS operacoes (
    id SERIAL PRIMARY KEY,
    combustivel_id INTEGER NOT NULL REFERENCES combustivel(id),
    tipo VARCHAR(10) NOT NULL CHECK (tipo IN ('compra', 'venda')),
    data DATE NOT NULL,
    ref_id INTEGER NOT NULL,
    litros DECIMAL(10, 2) NOT NULL,
    valor DECIMAL(15, 2) NOT NULL,
    selic DECIMAL(5, 2) NOT NULL
);

-- Inserção dos combustíveis
INSERT INTO combustivel (nome) VALUES 
('Etanol'),
('Gasolina'),
('Diesel')
ON CONFLICT DO NOTHING;

-- Gasolina - Referência de compra
INSERT INTO ref_compra (combustivel_id, mes, preco, tributo) VALUES
(1, 1, 5.92, 17.2), (1, 2, 5.95, 19.3), (1, 3, 5.90, 18.1), (1, 4, 5.94, 19.2),
(1, 5, 5.93, 19.7), (1, 6, 5.90, 20.1), (1, 7, 5.89, 20.6), (1, 8, 5.99, 21.1),
(1, 9, 6.04, 21.6), (1,10, 6.01, 22.1), (1,11, 6.03, 22.6), (1,12, 6.08, 23.1);

-- Etanol - Referência de compra
INSERT INTO ref_compra (combustivel_id, mes, preco, tributo) VALUES
(2, 1, 3.38, 17.2), (2, 2, 3.53, 19.3), (2, 3, 3.56, 18.1), (2, 4, 3.63, 19.2),
(2, 5, 3.82, 19.7), (2, 6, 3.81, 20.1), (2, 7, 4.09, 20.6), (2, 8, 4.06, 21.1),
(2, 9, 4.07, 21.6), (2,10, 4.03, 22.1), (2,11, 4.02, 22.6), (2,12, 4.10, 23.1);

-- Diesel - Referência de compra
INSERT INTO ref_compra (combustivel_id, mes, preco, tributo) VALUES
(3, 1, 5.87, 17.2), (3, 2, 5.88, 19.3), (3, 3, 5.84, 18.1), (3, 4, 5.85, 19.2),
(3, 5, 5.86, 19.7), (3, 6, 5.83, 20.1), (3, 7, 5.93, 20.6), (3, 8, 5.93, 21.1),
(3, 9, 5.91, 21.6), (3,10, 5.92, 22.1), (3,11, 5.96, 22.6), (3,12, 6.01, 23.1);

-- Gasolina - Referência de venda
INSERT INTO ref_venda (combustivel_id, mes, preco, tributo) VALUES
(1, 1, 5.94, 17.0), (1, 2, 5.97, 19.0), (1, 3, 5.92, 18.0), (1, 4, 5.96, 19.0),
(1, 5, 5.95, 19.5), (1, 6, 5.92, 20.0), (1, 7, 5.91, 20.5), (1, 8, 6.01, 21.0),
(1, 9, 6.06, 21.5), (1,10, 6.03, 22.0), (1,11, 6.05, 22.5), (1,12, 6.10, 23.0);

-- Etanol - Referência de venda
INSERT INTO ref_venda (combustivel_id, mes, preco, tributo) VALUES
(2, 1, 3.40, 17.0), (2, 2, 3.55, 19.0), (2, 3, 3.58, 18.0), (2, 4, 3.65, 19.0),
(2, 5, 3.84, 19.5), (2, 6, 3.83, 20.0), (2, 7, 4.11, 20.5), (2, 8, 4.08, 21.0),
(2, 9, 4.09, 21.5), (2,10, 4.05, 22.0), (2,11, 4.04, 22.5), (2,12, 4.12, 23.0);

-- Diesel - Referência de venda
INSERT INTO ref_venda (combustivel_id, mes, preco, tributo) VALUES
(3, 1, 5.88, 17.0), (3, 2, 5.90, 19.0), (3, 3, 5.86, 18.0), (3, 4, 5.87, 19.0),
(3, 5, 5.88, 19.5), (3, 6, 5.85, 20.0), (3, 7, 5.95, 20.5), (3, 8, 5.95, 21.0),
(3, 9, 5.93, 21.5), (3,10, 5.94, 22.0), (3,11, 5.98, 22.5), (3,12, 6.03, 23.0);
