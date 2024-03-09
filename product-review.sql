CREATE DATABASE product_review;
USE product_review;

CREATE TABLE product (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(191) NOT NULL,
    price INT NOT NULL,
    description VARCHAR(300) NOT NULL,
    created_at TIMESTAMP NOT NULL
);
    
    CREATE TABLE product_review (
		id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
        product_id INT NOT NULL,
        email VARCHAR(191) NOT NULL,
        rating INT,
        review_content TEXT,
        created_at TIMESTAMP NOT NULL
	);
    
SELECT * FROM product;
    
ALTER TABLE product MODIFY COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP; 
    