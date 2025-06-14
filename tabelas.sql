CREATE TABLE Usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE Materia (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    usuario_id INT REFERENCES Usuario(id)
);

CREATE TABLE HorarioDeAula (
    id SERIAL PRIMARY KEY,
    materia_id INT REFERENCES Materia(id),
    inicio TIME NOT NULL,
    fim TIME NOT NULL,
    dia_semana VARCHAR(20) NOT NULL
);

CREATE TABLE Prova (
    id SERIAL PRIMARY KEY,
    materia_id INT REFERENCES Materia(id),
    data DATE NOT NULL,
    descricao TEXT
);

CREATE TABLE Trabalho (
    id SERIAL PRIMARY KEY,
    materia_id INT REFERENCES Materia(id),
    data_entrega DATE NOT NULL,
    descricao TEXT
);

CREATE TABLE Hobby (
    id SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES Usuario(id),
    nome VARCHAR(255) NOT NULL
);

CREATE TABLE PlanejamentoSemanal (
    id SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES Usuario(id),
    atividades JSONB NOT NULL
);
