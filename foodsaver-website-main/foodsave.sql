-- 1. Create Database
CREATE DATABASE IF NOT EXISTS foodsaver_db;
USE foodsaver_db;

-- 2. Create Users Table
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Insert Sample User
INSERT INTO users (name, email, password, phone, address)
VALUES 
('John Doe', 'johndoe@example.com', '123456', '+91 9876543210', '123 Sample Street, Bangalore, India'),
('Jane Smith', 'janesmith@example.com', 'password123', '+91 9123456789', '456 Another Street, Mumbai, India');

-- 4. Verify Table
SELECT * FROM users;
