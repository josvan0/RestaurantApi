-- database setup
DROP DATABASE IF EXISTS RESTAURANT_APP;
CREATE DATABASE RESTAURANT_APP;
USE RESTAURANT_APP;

-- tables
CREATE TABLE IF NOT EXISTS User (
    id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(10),
    username VARCHAR(30) NOT NULL UNIQUE,
    password VARCHAR(30) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Product (
    id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description TEXT DEFAULT 'Description not available',
    price FLOAT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Category (
    id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

-- 1..n tables
CREATE TABLE IF NOT EXISTS ProductImage (
    id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    productId INTEGER NOT NULL,
    path VARCHAR(200) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (productId) REFERENCES Product(id)
);

CREATE TABLE IF NOT EXISTS Order (
    id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    userId INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (userId) REFERENCES User(id)
);

CREATE TABLE IF NOT EXISTS Order_Product (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    orderId INTEGER NOT NULL,
    productId INTEGER NOT NULL,
    quantity SMALLINT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS Sale (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    orderId INTEGER NOT NULL,
    paymentMethod SMALLINT NOT NULL,
    total FLOAT NOT NULL
);

-- n..n tables
CREATE TABLE IF NOT EXISTS Category_Product (
    categoryId INTEGER NOT NULL,
    productId INTEGER NOT NULL
);
