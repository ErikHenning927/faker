UPDATE sapEcom.sap_productFamily
    SET 
        [name] = ?,
        [creationDate] = ?,
        [creationTime] = ?,
        [modifiedDate] = ?,
        [modifiedTime] = ?
    WHERE [familyId] = ?