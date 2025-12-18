INSERT INTO customerData (
    customerId, customerDocument, customerFirstName, customerLastName, customerDocumentType,
    customerPhone, customerEmail, customerTradeName, customerCorporateDocument, customerStateInscription,
    customerCorporatePhone, customerIsCorporate, customerUserProfileId, customerUserProfileVersion,
    customerClass, customerCode
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)