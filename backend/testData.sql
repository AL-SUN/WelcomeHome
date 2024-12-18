-- Insert Persons
INSERT INTO Person (userName, password, fname, lname, email) VALUES
('jdoe', 'password123', 'John', 'Doe', 'jdoe@example.com'),
('asmith', 'password456', 'Alice', 'Smith', 'asmith@example.com'),
('bwhite', 'password789', 'Bob', 'White', 'bwhite@example.com'),
('cklein', 'password321', 'Charlie', 'Klein', 'cklein@example.com'),
('ss', 'scrypt:32768:8:1$aQOb4o3RLMGvQze0$5a8c4c504778ab308617c249b68bfb6df5b3b395391188789cbe5374ff298b98348da125e1016d342a565d5c24bfada68c4fd08c886145e2696c2f677864dece', 's', 's', 'ss@example.com'),
('cc', 'scrypt:32768:8:1$AyoZUnybp1a6jAYU$fcdf9802e3bff65480744c5b92dc57da68ef8554d0dac1aeb1f6543c612682e9c4595530e7e4be3aae30fa34e310b81ba3195f072a9306cde3827327c5838687', 'c', 'c', 'dd@example.com'),
('dd', 'scrypt:32768:8:1$UsZjpUUbrORsRUQ3$af995fa762be5ae9eb95e7a03502bcc407f6fcf50ab3038f16e16ace5c885c996c760932b1edec8521bd3afc1c4bdc98c5229c2b89c52917e2718f484d5c7370', 'd', 'd', 'dd@example.com'),
('vv', 'scrypt:32768:8:1$gxZVPDGZ0ydNp60w$dfaeca8ca0d1f83a4495e07bbb90276028712c9ea2d8d9e852ae11047f6eea8a3ed3cf191f801a5e080711a40f75109ea02618fe0e6a518f6f0fee5665cffbe2', 'v', 'v', 'vv@example.com');


-- Insert Person Phones
INSERT INTO PersonPhone (userName, phone) VALUES
('jdoe', '555-1234'),
('asmith', '555-5678'),
('bwhite', '555-8765'),
('cklein', '555-4321'),
('ss', '11-1234'),
('cc', '11-5678'),
('dd', '11-8765'),
('vv', '11-4321');


-- Insert Roles
INSERT INTO Role (roleID, rDescription) VALUES
('volunteer', 'Volunteer'),
('cilent', 'Client'),
('staff', 'Staff'),
('donor', 'Donor'); 


-- Insert Acts
INSERT INTO Act (userName, roleID) VALUES
('vv', 'volunteer'),
('cc', 'cilent'),
('ss', 'staff'),
('dd', 'donor'),  
('vv', 'donor'),
('jdoe', 'volunteer'),
('asmith', 'volunteer'),
('bwhite', 'cilent'),
('cklein', 'cilent'),
('jdoe', 'donor'),  
('asmith', 'staff');


-- Insert Locations
INSERT IGNORE INTO Location (roomNum, shelfNum, shelf, shelfDescription) VALUES
(1, 1, 'A', 'Main storage shelf'),
(1, 2, 'B', 'Secondary storage shelf'),
(2, 1, 'C', 'Clothing shelf'),
(2, 2, 'D', 'Electronics shelf'),
(-1, -1, 'Z', 'Holding location for items in preparation');


-- Insert Categories
INSERT INTO Category (mainCategory, subCategory, catNotes) VALUES
('Furniture', 'Living Room', 'Furniture items for living spaces'),
('Furniture', 'Bedroom', 'Furniture items for bedrooms'),
('Electronics', 'Appliances', 'Home electronic appliances'),
('Electronics', 'Computing', 'Computers and computer accessories'),
('Clothing', 'Men', 'Men''s clothing items'),
('Clothing', 'Women', 'Women''s clothing items');


-- Insert Items
INSERT INTO Item (iDescription, photo, color, isNew, hasPieces, material, mainCategory, subCategory) VALUES
('Wooden Coffee Table', 'coffee_table.jpg', 'Brown', TRUE, TRUE, 'Wood', 'Furniture', 'Living Room'),
('Leather Sofa', 'leather_sofa.jpg', 'Black', FALSE, TRUE, 'Leather', 'Furniture', 'Living Room'),
('King Size Bed Frame', 'bed_frame.jpg', 'White', TRUE, TRUE, 'Metal', 'Furniture', 'Bedroom'),
('Microwave Oven', 'microwave.jpg', 'Silver', TRUE, TRUE, 'Metal', 'Electronics', 'Appliances'),
('Laptop Computer', 'laptop.jpg', 'Silver', FALSE, TRUE, 'Plastic', 'Electronics', 'Computing'),
('Men''s Winter Jacket', 'winter_jacket.jpg', 'Navy Blue', TRUE, TRUE, 'Polyester', 'Clothing', 'Men'),
('Women''s Summer Dress', 'summer_dress.jpg', 'Floral', FALSE, TRUE, 'Cotton', 'Clothing', 'Women'),
('Leather Jacket', 'jacket1.jpg', 'Black', TRUE, TRUE, 'Leather', 'Clothing', 'Men'),
('Summer Dress', 'dress1.jpg', 'Red', TRUE, TRUE, 'Cotton', 'Clothing', 'Women');


-- Insert corresponding Pieces for each Item
INSERT INTO Piece (ItemID, pieceNum, pDescription, length, width, height, roomNum, shelfNum, pNotes) VALUES
(1, 1, 'Coffee Table Top', 120, 60, 5, -1, -1, 'Main surface of the coffee table'),
(1, 2, 'Coffee Table Legs', 5, 5, 45, -1, -1, 'Legs of the coffee table'),

(2, 1, 'Sofa Main Section', 200, 100, 80, 1, 2, 'Primary seating area'),
(2, 2, 'Sofa Left Arm', 50, 30, 80, 1, 2, 'Left armrest'),
(2, 3, 'Sofa Right Arm', 50, 30, 80, 1, 2, 'Right armrest'),
(2, 4, 'Sofa Back Cushion', 200, 50, 20, 1, 2, 'Back support cushion'),

(3, 1, 'Bed Frame Headboard', 180, 10, 120, 2, 1, 'Decorative headboard'),
(3, 2, 'Bed Frame Left Side Rail', 200, 10, 20, 2, 1, 'Left side support rail'),
(3, 3, 'Bed Frame Right Side Rail', 200, 10, 20, 2, 1, 'Right side support rail'),
(3, 4, 'Bed Frame Center Support', 180, 10, 20, 2, 1, 'Central support beam'),

(4, 1, 'Microwave', 50, 40, 30, 2, 2, 'Main microwave structure'),

(5, 1, 'Laptop', 35, 25, 2, 1, 1, 'Laptop'),

(6, 1, 'Jacket Body', 100, 60, 70, 1, 1, 'Main jacket section'),
(6, 2, 'Jacket Left Sleeve', 60, 20, 70, 1, 1, 'Left arm sleeve'),
(6, 3, 'Jacket Right Sleeve', 60, 20, 70, 1, 1, 'Right arm sleeve'),

(7, 1, 'Dress Main Body', 100, 50, 100, 1, 2, 'Primary dress section'),
(7, 2, 'Dress Top Section', 50, 50, 40, 1, 2, 'Upper part of the dress'),

(8, 1, 'Sleeves', 20, 15, 60, -1, -1, 'Stylish leather sleeves'),
(9, 1, 'Skirt', 30, 25, 50, -1, -1, 'Flowy summer skirt');


-- Insert Donated Items
INSERT INTO DonatedBy (ItemID, userName, donateDate) VALUES
(1, 'dd', '2024-01-15'),
(2, 'vv', '2024-01-20'),
(5, 'dd', '2024-01-22'),
(7, 'vv', '2024-01-25');

-- Insert Orders
INSERT INTO Ordered (orderDate, orderNotes, supervisor, client) VALUES
('2024-02-01', 'Order for office furniture', 'ss', 'cc'),
('2024-03-01', 'Emergency', 'asmith', 'bwhite'),
('2024-04-01', 'Fast Delivery', 'asmith', 'cklein');

-- Insert Items in Orders
INSERT INTO ItemIn (ItemID, orderID, found) VALUES
(1, 1, TRUE),
(8, 2, TRUE),
(9, 3, TRUE);

-- Insert Delivered Items
INSERT INTO Delivered (userName, orderID, status, date) VALUES
('vv', 1, 'Received', '2024-02-06'),
('vv', 2, 'Received', '2024-02-06'),
('jdoe', 3, 'Received', '2024-02-06');