SELECT
  transaction_id,
  amount,
  location,
  channel,
  device_id,
  predicted_label,
  predicted_label_probs
FROM
  ML.PREDICT(MODEL `project.dataset.fraud_model`,
    (SELECT * FROM `project.dataset.new_transactions`));