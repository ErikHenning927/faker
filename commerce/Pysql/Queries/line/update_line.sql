UPDATE sapEcom.sap_productLine
    SET 
        [name] = ?,
        [creationDate] = ?,
        [creationTime] = ?,
        [modifiedDate] = ?,
        [modifiedTime] = ?
    WHERE [lineId] = ?