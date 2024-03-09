CREATE DATABASE module_7_smmuja;

USE module_7_smmuja;

CREATE TABLE user (
	id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(191) NOT NULL,
    name VARCHAR(191) NOT NULL,
    password VARCHAR(191) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from user;