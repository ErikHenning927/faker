CREATE TABLE [paymentModes] (
    [paymentModeId] VARCHAR(20) PRIMARY KEY,
    [name] VARCHAR(255),
    [description] VARCHAR(255),
    [active] INT,
    [refundBy] INT,
    [creationDate] DATE,
    [creationTime] TIME,
    [modifiedDate] DATE,
    [modifiedTime] TIME
);