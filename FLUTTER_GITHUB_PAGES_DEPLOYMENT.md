# 🚀 Deploy Flutter Web App to GitHub Pages

This guide will help you deploy your Fraudguard-AI Flutter web app to GitHub Pages.

---

## 📋 Prerequisites

1. ✅ Flutter app is ready (already configured)
2. ✅ API URL updated to production Railway URL
3. ✅ GitHub repository: `notrealatharv7/Fraudguard-AI-M4`
4. ✅ GitHub Actions enabled for your repository

---

## 🔧 Step 1: Enable GitHub Pages

1. Go to your GitHub repository: `https://github.com/notrealatharv7/Fraudguard-AI-M4`
2. Click **"Settings"** tab
3. Scroll to **"Pages"** section (left sidebar)
4. Under **"Source"**, select: **"GitHub Actions"**
5. Click **"Save"**

**Note:** If you see "Deploy from a branch", change it to "GitHub Actions"

---

## 📝 Step 2: Update Repository Name in Workflow (if needed)

The GitHub Actions workflow assumes your repository is at:
```
https://github.com/notrealatharv7/Fraudguard-AI-M3
```

If your repository name is different, edit `.github/workflows/flutter-web-deploy.yml` and update:
```yaml
run: flutter build web --release --base-href "/YOUR-REPO-NAME/"
```

Replace `YOUR-REPO-NAME` with your actual repository name.

---

## 🚀 Step 3: Deploy (Automatic)

### Option A: Automatic Deployment (Recommended)

1. **Commit and push the changes:**
   ```bash
   git add .
   git commit -m "Configure Flutter web deployment to GitHub Pages"
   git push origin main
   ```

2. **GitHub Actions will automatically:**
   - Build your Flutter web app
   - Deploy to GitHub Pages
   - Make it live at: `https://notrealatharv7.github.io/Fraudguard-AI-M3/`

3. **Check deployment status:**
   - Go to **"Actions"** tab in your GitHub repository
   - Watch the workflow run
   - Wait for it to complete (takes 2-5 minutes)

### Option B: Manual Deployment

1. Go to **"Actions"** tab
2. Click **"Deploy Flutter Web to GitHub Pages"** workflow
3. Click **"Run workflow"** (right side)
4. Select branch: `main`
5. Click **"Run workflow"**

---

## 🌐 Step 4: Access Your Deployed App

After successful deployment, your app will be available at:

```
https://notrealatharv7.github.io/Fraudguard-AI-M4/
```

**Note:** Your repository name is `Fraudguard-AI-M4` (already configured correctly).

---

## ✅ Step 5: Verify Deployment

### Test the deployed app:

1. **Open the URL in browser:**
   ```
   https://notrealatharv7.github.io/Fraudguard-AI-M4/
   ```

2. **Test functionality:**
   - Fill in transaction details
   - Click "Check for Fraud"
   - Verify it connects to your Railway backend
   - Check if predictions are returned

3. **Expected behavior:**
   - App loads successfully
   - Form inputs work
   - API calls to Railway backend succeed
   - Predictions and explanations display correctly

---

## 🔍 Troubleshooting

### Issue: GitHub Actions workflow fails

**Check:**
1. ✅ Flutter is properly installed in workflow (version 3.16.0 or later)
2. ✅ Repository has GitHub Actions enabled
3. ✅ Workflow file is at `.github/workflows/flutter-web-deploy.yml`
4. ✅ Base href matches your repository name

**Common fixes:**
- Update Flutter version in workflow if needed
- Check workflow logs for specific errors
- Verify `pubspec.yaml` is correct

---

### Issue: App loads but API calls fail

**Check:**
1. ✅ API URL is set to Railway production URL (not localhost)
2. ✅ Railway backend is running and accessible
3. ✅ CORS is enabled on backend (should be `allow_origins=["*"]`)

**Fix:**
- Verify `lib/services/api_service.dart` has production URL:
  ```dart
  static const String baseUrl = 'https://fraudguard-ai-m4-production.up.railway.app';
  ```

---

### Issue: 404 or blank page

**Possible causes:**
1. Base href is incorrect
2. Assets not loading correctly
3. Build failed silently

**Fix:**
1. Check GitHub Actions logs
2. Verify base href in workflow matches repository name
3. Rebuild and redeploy

---

### Issue: GitHub Pages not showing updated content

**Fix:**
1. Check GitHub Actions completed successfully
2. Go to Settings → Pages
3. Verify deployment is active
4. Wait 1-2 minutes for DNS propagation
5. Hard refresh browser (Ctrl+F5 or Cmd+Shift+R)

---

## 📱 Mobile Compatibility

Your Flutter web app is responsive and works on:
- ✅ Desktop browsers (Chrome, Firefox, Safari, Edge)
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)
- ✅ Tablets

---

## 🔄 Update Deployment

### Automatic Updates:
Every time you push changes to the `main` branch that affect `flutter_app/fraud_detector/`, the app will automatically rebuild and redeploy.

### Manual Updates:
1. Make your changes
2. Commit and push:
   ```bash
   git add flutter_app/fraud_detector/
   git commit -m "Update Flutter app"
   git push origin main
   ```
3. GitHub Actions will automatically redeploy

---

## 📊 Deployment Status

### Check deployment status:

1. **GitHub Actions tab:**
   - Go to repository → "Actions" tab
   - See workflow runs and their status

2. **GitHub Pages settings:**
   - Go to Settings → Pages
   - See deployment status and URL

3. **Live site:**
   - Visit: `https://notrealatharv7.github.io/Fraudguard-AI-M4/`
   - Test app functionality

---

## 🎯 Success Checklist

- [ ] GitHub Pages enabled in repository settings
- [ ] GitHub Actions workflow file created
- [ ] API URL updated to production Railway URL
- [ ] Changes committed and pushed to main branch
- [ ] GitHub Actions workflow completed successfully
- [ ] App accessible at GitHub Pages URL
- [ ] App connects to Railway backend
- [ ] Predictions and explanations working

---

## 🎉 Summary

Your deployment setup:
- ✅ **Flutter App:** Ready for web deployment
- ✅ **API URL:** Updated to Railway production
- ✅ **GitHub Actions:** Workflow configured
- ✅ **GitHub Pages:** Will be enabled by you

**Next steps:**
1. Enable GitHub Pages in repository settings
2. Push changes to trigger deployment
3. Access your live app at GitHub Pages URL

---

**🚀 Your Flutter web app will be live on GitHub Pages!** 🌐
