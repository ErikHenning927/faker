INSERT INTO warehouse (
    warehouseId,
    "default",
    "name",
    isAllowRestock,
    "external",
    priority,
    warehouseBinTransferWorkflowName,
    score,
    creationDate,
    creationTime,
    modifiedDate,
    modifiedTime
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)