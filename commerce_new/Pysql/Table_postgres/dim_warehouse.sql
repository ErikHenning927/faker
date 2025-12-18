CREATE TABLE warehouse (
    warehouseId VARCHAR(10) PRIMARY KEY,
    "default" INT,
    name VARCHAR(100),
    isAllowRestock INT,
    external INT,
    priority VARCHAR (10),
    warehouseBinTransferWorkflowName VARCHAR(255),
    score FLOAT,
    creationDate DATE,
    creationTime TIME,
    modifiedDate DATE,
    modifiedTime TIME
);
