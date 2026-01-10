# Quick Test Guide - Verify Services Are Connected

## Test 1: Explanation Service Health

Open in browser:
```
https://your-explanation-service-domain.up.railway.app/health
```

**Expected:** `{"status": "ok"}`

---

## Test 2: ML Service Health

Open in browser:
```
https://your-ml-service-domain.up.railway.app/health
```

**Expected:** 
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

---

## Test 3: End-to-End Prediction with Explanation

### Option A: Use Browser (Interactive Docs)

1. Open: `https://your-ml-service-domain.up.railway.app/docs`
2. Click on `/predict` endpoint
3. Click "Try it out"
4. Use this test data:
```json
{
  "transactionAmount": 150.50,
  "transactionAmountDeviation": 0.25,
  "timeAnomaly": 0.3,
  "locationDistance": 25.0,
  "merchantNovelty": 0.2,
  "transactionFrequency": 5
}
```
5. Click "Execute"
6. **Check the response** - it should have an `explanation` field!

**✅ Success:** If `explanation` field is present and not null  
**❌ Issue:** If `explanation` is null or shows error message

---

### Option B: Use curl (Terminal)

```bash
curl -X POST "https://your-ml-service-domain.up.railway.app/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "transactionAmount": 150.50,
    "transactionAmountDeviation": 0.25,
    "timeAnomaly": 0.3,
    "locationDistance": 25.0,
    "merchantNovelty": 0.2,
    "transactionFrequency": 5
  }'
```

---

## Expected Response (Success)

```json
{
  "fraud": false,
  "risk_score": 0.23,
  "explanation": "This transaction appears legitimate (risk: 23%) based on normal amount deviation (0.25), distant location (25.0km), familiar merchant, normal transaction time..."
}
```

---

## Troubleshooting

### If explanation is `null` or error:

1. ✅ Check `EXPLANATION_SERVICE_URL` is set in ML service (not explanation service)
2. ✅ Verify URL uses `https://` (not `http://`)
3. ✅ Check URL has no trailing slash
4. ✅ Ensure ML service was redeployed after setting environment variable
5. ✅ Check Railway logs for both services for errors

### Check Railway Logs:

**ML Service Logs:**
- Look for: `[ERROR] Could not connect to explanation service`
- Check if `EXPLANATION_SERVICE_URL` is being used

**Explanation Service Logs:**
- Look for incoming requests from ML service
- Check for any errors

---

## Success Indicators

- ✅ Both `/health` endpoints return expected responses
- ✅ `/predict` returns `explanation` field with text
- ✅ Explanation is not null or error message
- ✅ Both services show as "Active" in Railway dashboard
