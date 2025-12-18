UPDATE orders
    SET 
    Description = %s, 
    Origin = %s,
    deliveryQuotedCost = %s, 
    authorizedDate = %s, 
    invoiceShippedDate = %s, 
    invoiceDeliveryDate = %s, 
    date = %s,
    statusUpdatedAt = %s,
    paymentRefund = %s,
    paymentRefundAttempts = %s,
    subtotal = %s,
    totalDiscounts = %s,
    status = %s,
    exportStatus = %s,
    blockCart = %s,
    creationDate = %s,
    creationTime = %s,
    modifiedDate = %s,
    modifiedTime = %s
    WHERE orderId = %s