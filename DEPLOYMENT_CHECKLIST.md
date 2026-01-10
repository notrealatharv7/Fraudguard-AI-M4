# 🚀 Railway Deployment Checklist

## Phase 1: Deploy ML Service (Main Fraud Detection API)

### ✅ Pre-Deployment Verification
- [x] Repository pushed to GitHub: `https://github.com/notrealatharv7/Fraudguard-AI-M3`
- [x] `backend/main.py` exists
- [x] `backend/requirements.txt` exists
- [x] `backend/ml/model.pkl` exists
- [x] Code uses `EXPLANATION_SERVICE_URL` environment variable

### Step 1: Create Railway Project
- [ ] Go to [railway.app](https://railway.app)
- [ ] Login with GitHub
- [ ] Click **"+ New Project"**
- [ ] Select **"Deploy from GitHub repo"**
- [ ] Select repository: `notrealatharv7/Fraudguard-AI-M3`

### Step 2: Configure ML Service
- [ ] Service name: `fraudguard-ml-service` (or similar)
- [ ] **Root Directory:** `backend`
- [ ] **Start Command:** `python main.py`
- [ ] **Build Command:** (leave empty - auto-detected)
- [ ] Save settings

### Step 3: Deploy & Get Domain
- [ ] Wait for deployment to complete
- [ ] Check logs for: `[OK] Model loaded successfully`
- [ ] Generate domain in Settings → Domains
- [ ] Copy domain: `https://fraudguard-ml-service-production.up.railway.app`
- [ ] Test: `https://your-domain.up.railway.app/health`

### Step 4: Verify ML Service
- [ ] `/health` returns: `{"status": "healthy", "model_loaded": true}`
- [ ] `/docs` shows interactive API documentation
- [ ] `/predict` endpoint accepts POST requests

---

## Phase 2: Deploy Explanation Service (Separate)

### Step 5: Create New Service in Same Project
- [ ] In Railway project dashboard, click **"+ New Service"** (or **"+ Add Service"**)
- [ ] Select **"Deploy from GitHub repo"**
- [ ] Select **SAME repository**: `notrealatharv7/Fraudguard-AI-M3`

### Step 6: Configure Explanation Service
- [ ] Service name: `fraudguard-explanation-service`
- [ ] **Root Directory:** `backend/explanation_service`
- [ ] **Start Command:** `python main.py`
- [ ] **Build Command:** (leave empty - auto-detected)
- [ ] Save settings

### Step 7: Deploy Explanation Service
- [ ] Wait for deployment (first deploy will download ~500MB model, takes 5-10 minutes)
- [ ] Check logs for model download and loading
- [ ] Generate domain in Settings → Domains
- [ ] Copy domain: `https://fraudguard-explanation-service-production.up.railway.app`
- [ ] Test: `https://your-domain.up.railway.app/health`

### Step 8: Verify Explanation Service
- [ ] `/health` returns: `{"status": "ok"}`
- [ ] `/docs` shows API documentation
- [ ] Service is running and ready

---

## Phase 3: Connect Services

### Step 9: Set Environment Variable in ML Service
- [ ] Go to **ML service** (fraudguard-ml-service) settings
- [ ] Go to **"Environment Variables"** section
- [ ] Click **"+ New Variable"**
- [ ] **Variable Name:** `EXPLANATION_SERVICE_URL`
- [ ] **Value:** `https://fraudguard-explanation-service-production.up.railway.app`
  - ⚠️ Use `https://` (not `http://`)
  - ⚠️ No trailing slash
  - ⚠️ Don't include `/explain` (code adds it automatically)
- [ ] Click **"Add"**

### Step 10: Redeploy ML Service
- [ ] Go to ML service **"Deployments"** tab
- [ ] Click **"Redeploy"** (or trigger new deployment)
- [ ] Wait for deployment to complete
- [ ] ML service will now connect to explanation service

### Step 11: Final End-to-End Test
- [ ] Test ML service `/predict` endpoint (via `/docs` interface)
- [ ] Verify response includes `explanation` field
- [ ] Check that explanation is generated (not null)
- [ ] Both services show as "Active" in Railway dashboard

---

## 🎯 Quick Reference

### ML Service Configuration
- **Root Directory:** `backend`
- **Start Command:** `python main.py`
- **Domain:** `https://fraudguard-ml-service-production.up.railway.app`
- **Environment Variable:** `EXPLANATION_SERVICE_URL` = explanation service domain

### Explanation Service Configuration
- **Root Directory:** `backend/explanation_service`
- **Start Command:** `python main.py`
- **Domain:** `https://fraudguard-explanation-service-production.up.railway.app`

### Test Endpoints
- ML Health: `https://ml-service-domain.up.railway.app/health`
- ML Docs: `https://ml-service-domain.up.railway.app/docs`
- ML Predict: `https://ml-service-domain.up.railway.app/predict` (POST)
- Explanation Health: `https://explanation-service-domain.up.railway.app/health`
- Explanation Docs: `https://explanation-service-domain.up.railway.app/docs`

---

## ⚠️ Important Notes

1. **First deployment of explanation service will be slow** (5-10 minutes) due to model download
2. **Don't set `EXPLANATION_SERVICE_URL` until explanation service is deployed**
3. **Both services must be in the same Railway project** (or you can use different projects, but same repo)
4. **Free tier limitations:** Explanation service may be slow on free tier due to memory constraints
5. **Model file size:** Ensure `backend/ml/model.pkl` is committed to Git (not in `.gitignore`)

---

## ✅ Success Criteria

- [ ] ML service responds to `/health` with `model_loaded: true`
- [ ] Explanation service responds to `/health` with `status: ok`
- [ ] ML service `/predict` returns predictions with explanations
- [ ] Both services are active in Railway dashboard
- [ ] Environment variable is set correctly in ML service

---

## 🆘 Troubleshooting

**ML Service fails to load model:**
- Check that `backend/ml/model.pkl` is committed to Git
- Verify Root Directory is set to `backend` (not empty)
- Check Railway logs for exact error

**Explanation Service build fails:**
- Check Root Directory is `backend/explanation_service`
- Verify `requirements.txt` exists and is valid
- First deployment downloads large model - be patient

**Services can't connect:**
- Verify `EXPLANATION_SERVICE_URL` is set in ML service (not explanation service)
- Check URL doesn't have trailing slash or `/explain`
- Ensure both services are deployed and active
- Check Railway logs for connection errors

---

**Ready to deploy? Follow the checklist above step by step!** 🚀
