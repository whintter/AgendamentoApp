-- Criar o banco de dados
CREATE DATABASE agendamento;

-- Usar o banco de dados
USE agendamento;

-- Tabela para administradores
CREATE TABLE admin (
    id_admin INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    telefone VARCHAR(20)
);

-- Tabela para usuários (talvez para gerenciar a barbearia)
CREATE TABLE usuario (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);

-- Tabela para barbearias
CREATE TABLE barbearia (
    id_barber INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,  -- Descrição pode ser maior, por isso TEXT
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    bairro VARCHAR(255),
    cidade VARCHAR(255),
    estado VARCHAR(255),
    telefone VARCHAR(20),
    status VARCHAR(1)  NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
    -- fk_id_user INT,  -- Relacionamento com usuário
    -- FOREIGN KEY (fk_id_user) REFERENCES usuario(id_user) ON DELETE CASCADE
);

-- Tabela para clientes
CREATE TABLE cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    telefone VARCHAR(15) NOT NULL, 
    senha VARCHAR(255) NOT NULL
);

-- Tabela para agendamentos
CREATE TABLE agendamentos (
    id_agendamento INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    hora VARCHAR(5) NOT NULL,  -- Formato 'HH:MM'
    fk_id_cliente INT,
    fk_id_barber INT,
    status CHAR(1) NOT NULL,  -- 'P' para pendente, A para agendado,  'C' para concluído ou Cancelado , etc.
    FOREIGN KEY (fk_id_cliente) REFERENCES cliente(id_cliente) ON DELETE CASCADE,
    FOREIGN KEY (fk_id_barber) REFERENCES barbearia(id_barber) ON DELETE CASCADE
);
CREATE TABLE servicos (
    id_servico INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    descricao VARCHAR(255),
    fk_id_barber INT,
    status CHAR(1) NOT NULL,  -- 'P' para pendente, 'C' para concluído, etc.
    FOREIGN KEY (fk_id_barber) REFERENCES barbearia(id_barber) ON DELETE CASCADE
);
insert into admin (nome,email,senha,telefone) values ("Admin","Admin@gmail","admin123","11 932364637");


