CREATE TABLE courier (
    courierId VARCHAR(100) PRIMARY KEY,
    retrieveShippingLabel INT,
    name VARCHAR(255),
    creationDate DATE,
    creationTime TIME,
    modifiedDate DATE,
    modifiedTime TIME
);