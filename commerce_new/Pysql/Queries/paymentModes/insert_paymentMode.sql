INSERT INTO paymentModes (
    paymentModeId,
    name,
    description,
    active,
    refundby,
    creationdate,
    creationtime,
    modifieddate,
    modifiedtime
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
