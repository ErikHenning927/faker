UPDATE orders
    SET 
    [Description] = ?, 
    [Origin] = ?,
    [deliveryQuotedCost] = ?, 
    [authorizedDate] = ?, 
    [invoiceShippedDate] = ?, 
    [invoiceDeliveryDate] = ?, 
    [date] = ?,
    [statusUpdatedAt] = ?,
    [paymentRefund] = ?,
    [paymentRefundAttempts] = ?,
    [subtotal] = ?,
    [totalDiscounts] = ?,
    [status] = ?,
    [exportStatus] = ?,
    [blockCart] = ?,
    [creationDate] = ?,
    [creationTime] = ?,
    [modifiedDate] = ?,
    [modifiedTime] = ?
    WHERE [orderId] = ?