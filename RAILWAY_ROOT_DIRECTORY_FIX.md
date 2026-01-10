# ⚠️ CRITICAL FIX: Railway Root Directory Configuration

## The Problem

Railway's Railpack/Nixpacks cannot detect Python because it's analyzing the **root directory** (which has Flutter files) instead of the `backend/` directory where your Python code is.

**Error you're seeing:**
```
✖ Railpack could not determine how to build the app.
The app contents that Railpack analyzed contains: ./ (root directory with Flutter files)
```

## The Solution

**You MUST set the Root Directory in Railway UI to `backend`**. This cannot be done in code - it's a Railway UI setting.

---

## 🔧 Step-by-Step Fix

### Step 1: Go to Railway Dashboard

1. Go to [railway.app](https://railway.app)
2. Open your project
3. Click on the **service** that's failing (usually named after your repo)

### Step 2: Open Settings

1. Click the **"Settings"** tab (gear icon on the right)
2. Scroll down to find **"Root Directory"** section

### Step 3: Set Root Directory

1. Find **"Root Directory"** field
2. Click **"Edit"** or click in the input field
3. **Enter:** `backend`
4. Click **"Save"** or press Enter

**Important:** The Root Directory should be exactly `backend` (not `/backend` or `./backend`)

### Step 4: Set Start Command

While you're in Settings, also set:

1. Scroll to **"Start Command"** section
2. Click **"Edit"**
3. **Enter:** `python main.py`
4. Click **"Save"**

### Step 5: Redeploy

1. Go to **"Deployments"** tab
2. Click **"Redeploy"** or trigger a new deployment
3. Railway will now:
   - Look in `backend/` directory
   - Find `requirements.txt` and detect Python
   - Find `runtime.txt` for Python version (3.11)
   - Build and deploy your FastAPI app

---

## ✅ What Should Happen After Fix

Once Root Directory is set to `backend`, Railway logs should show:

```
Detecting Python...
Found requirements.txt
Installing dependencies...
Python 3.11 detected
Building...
Starting: python main.py
[OK] Model loaded successfully from ml/model.pkl
API ready to accept requests!
```

---

## 📋 Verification Checklist

After setting Root Directory:

- [ ] Root Directory is set to `backend` (check in Settings)
- [ ] Start Command is set to `python main.py`
- [ ] Build Command is empty (auto-detected) OR set to `pip install -r requirements.txt`
- [ ] Deployment starts successfully
- [ ] Logs show Python detection
- [ ] Logs show dependencies installing
- [ ] Logs show model loading
- [ ] `/health` endpoint returns `{"status": "healthy", "model_loaded": true}`

---

## 🚫 Common Mistakes

❌ **Don't set Root Directory to empty** - Railway will scan root and fail  
❌ **Don't set Root Directory to `/backend`** - Use `backend` without leading slash  
❌ **Don't set Root Directory to `./backend`** - Use `backend` without `./`  
❌ **Don't skip this step** - This is REQUIRED for monorepo deployments  

---

## 📝 Files We Created to Help

These files in `backend/` directory will help Railway:

- ✅ `backend/requirements.txt` - Python dependencies (Railway detects Python from this)
- ✅ `backend/runtime.txt` - Python version specification (Python 3.11)
- ✅ `backend/nixpacks.toml` - Build configuration (optional, but helps)
- ✅ `backend/Procfile` - Start command fallback (optional)

**All these files are committed and pushed to GitHub.**

---

## 🎯 Next Steps After Fix

Once deployment succeeds:

1. Get your Railway domain (Settings → Domains → Generate Domain)
2. Test `/health` endpoint
3. Deploy explanation service separately (see `RAILWAY_DEPLOYMENT_EXPLANATION_SERVICE.md`)
4. Set `EXPLANATION_SERVICE_URL` environment variable
5. Test end-to-end

---

**The fix is simple: Set Root Directory to `backend` in Railway UI Settings!** 🔧
