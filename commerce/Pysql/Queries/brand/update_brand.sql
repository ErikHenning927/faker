UPDATE [sapEcom].[sap_productBrand]
    SET 
        [name] = ?,
        [vtexId] = ?,
        [creationDate] = ?,
        [creationTime] = ?,
        [modifiedDate] = ?,
        [modifiedTime] = ?
    WHERE [brandId] = ?