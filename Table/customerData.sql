CREATE TABLE [customerData] (
    customerId VARCHAR(20),
    customerDocument VARCHAR(20),
    customerFirstName VARCHAR(100),
    customerLastName VARCHAR(100),
    customerDocumentType VARCHAR(20),
    customerPhone VARCHAR(50),
    customerEmail VARCHAR(100),
    customerTradeName VARCHAR(100),
    customerCorporateDocument VARCHAR(20),
    customerStateInscription VARCHAR(50),
    customerCorporatePhone VARCHAR(50),
    customerIsCorporate INT,
    customerUserProfileId VARCHAR(50),
    customerUserProfileVersion VARCHAR(50),
    customerClass VARCHAR(50),
    customerCode VARCHAR(50),
    PRIMARY KEY (customerId)
);
