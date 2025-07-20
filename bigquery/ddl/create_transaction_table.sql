CREATE TABLE `project.dataset.transactions` (
    transaction_id STRING,
    timestamp TIMESTAMP,
    account_id STRING,
    amount FLOAT64,
    currency STRING,
    to_account STRING,
    location STRING,
    channel STRING,
    device_id STRING,
    risk_score FLOAT64,
    suspicious BOOL
);