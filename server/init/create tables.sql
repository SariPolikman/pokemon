CREATE DATABASE pokemondb;
-- USE pokemondb;

-- CREATE TABLE Pokemon(
--     id INT NOT NULL PRIMARY KEY,
--     name VARCHAR(20),
--     height INT,
--     weight INT
-- );

-- CREATE TABLE type_poke(
--     type VARCHAR(20),
--     p_id INT NOT NULL,
--     FOREIGN KEY(p_id) REFERENCES Pokemon(id),
--     PRIMARY KEY (type, p_id )
-- );

-- CREATE TABLE Trainer(
--     name VARCHAR(20) NOT NULL PRIMARY KEY,
--     town VARCHAR(20)
-- );

-- CREATE TABLE Trainer_Pokemon(
--     p_id INT NOT NULL,
--     t_name VARCHAR(20),
--     FOREIGN KEY(p_id) REFERENCES Pokemon(id),
--     FOREIGN KEY(t_name) REFERENCES Trainer(name),
--     PRIMARY KEY (p_id , t_name)
-- );
