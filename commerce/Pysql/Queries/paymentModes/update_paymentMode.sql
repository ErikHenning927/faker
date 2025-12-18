UPDATE paymentModes
    SET 
        [name] = ?,
        [description] = ?,
        [active] = ?,
        [refundBy] = ?,
        [creationDate] = ?,
        [creationTime] = ?,
        [modifiedDate] = ?,
        [modifiedTime] = ?
    WHERE [paymentModeId] = ?