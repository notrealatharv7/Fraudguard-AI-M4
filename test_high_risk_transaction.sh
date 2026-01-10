#!/bin/bash
# Test with a high-risk transaction to see higher fraud probability

curl -X 'POST' \
  'https://fraudguard-ai-m4-production.up.railway.app/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "transactionAmount": 5000,
  "transactionAmountDeviation": 0.8,
  "timeAnomaly": 0.9,
  "locationDistance": 500,
  "merchantNovelty": 0.9,
  "transactionFrequency": 1
}'
