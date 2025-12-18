UPDATE sapEcom.sap_courier
    SET 
        [retrieveShippingLabel] = ?,
        [name] = ?,
        [idSalesforce] = ?,
        [creationDate] = ?,
        [creationTime] = ?,
        [modifiedDate] = ?,
        [modifiedTime] = ?
    WHERE [courierId] = ?