CREATE OR REPLACE MODEL `project.dataset.fraud_model`
OPTIONS(model_type='logistic_reg') AS
SELECT amount, location, channel, device_id, suspicious AS label
FROM `project.dataset.transactions`;