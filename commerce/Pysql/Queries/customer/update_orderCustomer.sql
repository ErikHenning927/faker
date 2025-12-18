UPDATE customerData
    SET 
        customerDocument = ?,
        customerFirstName = ?,
        customerLastName = ?,
        customerDocumentType = ?,
        customerPhone = ?,
        customerEmail = ?,
        customerTradeName = ?,
        customerCorporateDocument = ?,
        customerStateInscription = ?,
        customerCorporatePhone = ?,
        customerIsCorporate = ?,
        customerUserProfileId = ?,
        customerUserProfileVersion = ?,
        customerClass = ?,
        customerCode = ?
    WHERE [customerId] = ?;