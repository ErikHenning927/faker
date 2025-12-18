CREATE TABLE [salesChannel] (
    [salesChannelId] INT PRIMARY KEY,
    [stateRegistration] VARCHAR(50),
    [ownStore] INT,
    [cnpj] VARCHAR(20),
    [name] VARCHAR(255),
    [active] INT,
    [creationDate] DATE,
    [creationTime] TIME,
    [modifiedDate] DATE,
    [modifiedTime] TIME
);
