UPDATE salesChannel
    SET 
        stateRegistration = %s,
        ownStore = %s,
        cnpj = %s,
        name = %s,
        active = %s,
        creationDate = %s,
        creationTime = %s,
        modifiedDate = %s,
        modifiedTime = %s
    WHERE salesChannelId = %s