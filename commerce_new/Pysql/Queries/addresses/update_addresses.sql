UPDATE deliveryAddresses
    SET 
        postalcode = %s,
        unloadingAddress = %s,
        streetnumber = %s,
        complement = %s,
        remarks = %s,
        addressType = %s,
        contactAddress = %s,
        shippingAddress = %s,
        building = %s,
        cellphone = %s,
        town = %s,
        appartment = %s,
        company = %s,
        typeQualifier = %s,
        streetname = %s,
        department = %s,
        billingAddress = %s,
        country = %s,
        title = %s,
        region = %s
    WHERE addressId = %s