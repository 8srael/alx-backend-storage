-- script that creates a table users
-- with id, email and name columns

CREATE TABLE users IF NOT EXISTS (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);