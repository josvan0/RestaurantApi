USE RESTAURANT_APP;
INSERT INTO Category (name)
VALUES ('Entradas'),
    ('Comidas'),
    ('Postres'),
    ('Bebidas');
-- load products
LOAD DATA LOCAL INFILE 'C:\\Ivan\\Repos\\RestaurantApi\\db\\products.csv'
    INTO TABLE Product
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (name, description, price);
INSERT INTO Category_Product
VALUES (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (2, 6),
    (2, 7),
    (2, 8),
    (2, 9),
    (2, 10),
    (3, 11),
    (3, 12),
    (3, 13),
    (3, 14),
    (3, 15),
    (4, 16),
    (4, 17),
    (4, 18),
    (4, 19),
    (4, 20);
INSERT INTO ProductImage (productId, path)
VALUES (1, 'product1-1.jpg'),
    (1, 'product1-2.jpg'),
    (1, 'product1-3.jpg'),
    (1, 'product1-4.jpg'),
    (2, 'product2-1.jpg'),
    (2, 'product2-2.jpg'),
    (3, 'product3-1.jpg'),
    (3, 'product3-2.jpg'),
    (3, 'product3-3.jpg'),
    (4, 'product4-1.jpg'),
    (5, 'product5-1.jpg'),
    (5, 'product5-2.jpg'),
    (6, 'product6-1.jpg'),
    (6, 'product6-2.jpg'),
    (7, 'product7-1.jpg'),
    (8, 'product8-1.jpg'),
    (9, 'product9-1.jpg'),
    (10, 'product10-1.jpg'),
    (11, 'product11-1.jpg'),
    (12, 'product12-1.jpg'),
    (13, 'product13-1.jpg'),
    (14, 'product14-1.jpg'),
    (15, 'product15-1.jpg'),
    (16, 'product16-1.jpg'),
    (17, 'product17-1.jpg'),
    (18, 'product18-1.jpg'),
    (19, 'product19-1.jpg'),
    (20, 'product20-1.jpg');
