# Phase 3: Connect ML Service and Explanation Service

## ✅ Prerequisites
- [x] ML Service deployed and has domain
- [x] Explanation Service deployed and has domain
- [x] Both services are running and healthy

---

## Step 1: Get Your Domain URLs

You need:
1. **ML Service Domain:** `https://fraudguard-ml-service-production.up.railway.app` (or similar)
2. **Explanation Service Domain:** `https://fraudguard-explanation-service-production.up.railway.app` (or similar)

**Where to find them:**
- In Railway dashboard → Your Service → Settings → Domains

---

## Step 2: Set Environment Variable in ML Service

### In Railway Dashboard:

1. **Go to your ML Service** (not explanation service)
2. Click **"Settings"** tab (gear icon)
3. Scroll down to **"Environment Variables"** section
4. Click **"+ New Variable"** button
5. Fill in:
   - **Variable Name:** `EXPLANATION_SERVICE_URL`
   - **Value:** Your explanation service domain (e.g., `https://fraudguard-explanation-service-production.up.railway.app`)
     - ⚠️ **IMPORTANT:** Use `https://` (not `http://`)
     - ⚠️ **IMPORTANT:** No trailing slash (no `/` at the end)
     - ⚠️ **IMPORTANT:** Don't include `/explain` (the code adds it automatically)
   - Example: `https://fraudguard-explanation-service-production.up.railway.app`
6. Click **"Add"** or **"Save"**

---

## Step 3: Redeploy ML Service

After setting the environment variable:

1. Go to **"Deployments"** tab in your ML service
2. Click **"Redeploy"** (or trigger a new deployment)
3. Wait for deployment to complete
4. This will make the ML service connect to the explanation service

**Why redeploy?** Environment variables are only picked up on deployment.

---

## Step 4: Test Connection

### Test 1: ML Service Health
```bash
GET https://your-ml-service-domain.up.railway.app/health
```
**Expected Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### Test 2: Explanation Service Health
```bash
GET https://your-explanation-service-domain.up.railway.app/health
```
**Expected Response:**
```json
{
  "status": "ok"
}
```

### Test 3: End-to-End Prediction with Explanation
```bash
POST https://your-ml-service-domain.up.railway.app/predict
Content-Type: application/json

{
  "transactionAmount": 150.50,
  "transactionAmountDeviation": 0.25,
  "timeAnomaly": 0.3,
  "locationDistance": 25.0,
  "merchantNovelty": 0.2,
  "transactionFrequency": 5
}
```

**Expected Response:**
```json
{
  "fraud": false,
  "risk_score": 0.23,
  "explanation": "This transaction appears legitimate (risk: 23%) based on normal amount deviation (0.25), distant location (25.0km), familiar merchant, normal transaction time..."
}
```

✅ **If `explanation` field is populated** → Services are connected correctly!  
❌ **If `explanation` is `null` or shows error** → Check environment variable and logs

---

## Step 5: Test via Interactive Docs

### ML Service Docs:
1. Go to: `https://your-ml-service-domain.up.railway.app/docs`
2. Click on `/predict` endpoint
3. Click "Try it out"
4. Enter test transaction data
5. Click "Execute"
6. Check the response includes `explanation` field

---

## 🔍 Troubleshooting

### Issue: Explanation is `null` or error message

**Check:**
1. ✅ `EXPLANATION_SERVICE_URL` is set in ML service (not explanation service)
2. ✅ URL uses `https://` (not `http://`)
3. ✅ No trailing slash in URL
4. ✅ Don't include `/explain` in URL (code adds it)
5. ✅ Both services are deployed and running
6. ✅ ML service was redeployed after setting environment variable

**Check Railway Logs:**
- ML service logs: Look for connection errors to explanation service
- Explanation service logs: Check if requests are being received

### Issue: Connection timeout

**Possible causes:**
- Explanation service is not running
- Domain URL is incorrect
- Network issues between services

**Solution:**
- Verify explanation service `/health` endpoint works
- Double-check `EXPLANATION_SERVICE_URL` value
- Check Railway logs for both services

---

## ✅ Success Checklist

- [ ] ML Service domain obtained
- [ ] Explanation Service domain obtained
- [ ] `EXPLANATION_SERVICE_URL` environment variable set in ML service
- [ ] ML service redeployed after setting environment variable
- [ ] ML service `/health` returns `model_loaded: true`
- [ ] Explanation service `/health` returns `status: ok`
- [ ] ML service `/predict` returns predictions with `explanation` field
- [ ] Explanation is not `null` or error message

---

## 🎉 Next Steps After Success

Once everything is working:

1. **Update Flutter App:**
   - Change API URL from `localhost:8000` to your ML service Railway domain
   - Test the Flutter app with production backend

2. **Monitor Services:**
   - Check Railway dashboard for usage and errors
   - Monitor logs for any issues

3. **Optional: Custom Domain**
   - Set up custom domain in Railway (Pro feature)

---

**You're almost done! Follow the steps above to connect your services!** 🚀
