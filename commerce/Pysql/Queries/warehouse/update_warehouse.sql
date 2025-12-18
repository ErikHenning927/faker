UPDATE warehouse
SET 
    [default] = ?,
    [name] = ?,
    [isAllowRestock] = ?,
    [external] = ?,
    [priority] = ?,
    [warehouseBinTransferWorkflowName] = ?,
    [score] = ?,
    [creationDate] = ?,
    [modifiedDate] = ?,
    [creationTime] = ?,
    [modifiedTime] = ?
WHERE [warehouseId] = ?;
