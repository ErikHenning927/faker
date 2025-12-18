UPDATE deliveryAddresses
    SET 
        [postalcode] = ?,
        [unloadingAddress] = ?,
        [streetnumber] = ?,
        [complement] = ?,
        [remarks] = ?,
        [addressType] = ?,
        [contactAddress] = ?,
        [shippingAddress] = ?,
        [building] = ?,
        [cellphone] = ?,
        [town] = ?,
        [appartment] = ?,
        [company] = ?,
        [typeQualifier] = ?,
        [streetname] = ?,
        [department] = ?,
        [billingAddress] = ?,
        [country] = ?,
        [title] = ?,
        [region] = ?
    WHERE [addressId] = ?