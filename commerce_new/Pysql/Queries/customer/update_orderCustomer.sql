UPDATE customerData
    SET 
        customerDocument = %s,
        customerFirstName = %s,
        customerLastName = %s,
        customerDocumentType = %s,
        customerPhone = %s,
        customerEmail = %s,
        customerTradeName = %s,
        customerCorporateDocument = %s,
        customerStateInscription = %s,
        customerCorporatePhone = %s,
        customerIsCorporate = %s,
        customerUserProfileId = %s,
        customerUserProfileVersion = %s,
        customerClass = %s,
        customerCode = %s
    WHERE [customerId] = %s;