UPDATE paymentModes
    SET 
        name = %s,
        description = %s,
        active = %s,
        refundBy = %s,
        creationDate = %s,
        creationTime = %s,
        modifiedDate = %s,
        modifiedTime = %s
    WHERE paymentModeId = %s