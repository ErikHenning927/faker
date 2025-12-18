UPDATE salesChannel
    SET 
        [stateRegistration] = ?,
        [ownStore] = ?,
        [cnpj] = ?,
        [name] = ?,
        [active] = ?,
        [creationDate] = ?,
        [creationTime] = ?,
        [modifiedDate] = ?,
        [modifiedTime] = ?
    WHERE [salesChannelId] = ?