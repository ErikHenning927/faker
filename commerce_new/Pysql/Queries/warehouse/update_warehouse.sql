UPDATE warehouse
SET 
    "default" = %s,
    name = %s,
    isAllowRestock = %s,
    external = %s,
    priority = %s,
    warehouseBinTransferWorkflowName = %s,
    score = %s,
    creationDate = %s,
    creationTime = %s,
    modifiedDate = %s,
    modifiedTime = %s
WHERE warehouseId = %s;
