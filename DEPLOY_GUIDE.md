# 🚀 Deploy to GitHub Pages - Step by Step

## What is GitHub Pages?

GitHub Pages is a **free** service that hosts static websites directly from your GitHub repository. Perfect for this web app!

## 📋 Prerequisites

- A GitHub account (free) - [Sign up here](https://github.com/join)
- The `index.html` file from this project

## 🎯 Deployment Steps

### Step 1: Create a New Repository

1. Go to [GitHub](https://github.com)
2. Click the **"+"** icon (top right) → **"New repository"**
3. Name your repository (e.g., `retreat-marketing-planner`)
4. Choose **Public** (required for free GitHub Pages)
5. ✅ Check "Add a README file"
6. Click **"Create repository"**

### Step 2: Upload Your Files

#### Option A: Via Web Interface (Easiest)

1. In your new repository, click **"Add file"** → **"Upload files"**
2. Drag and drop `index.html` onto the page
3. Scroll down and click **"Commit changes"**

#### Option B: Via Git (If you know Git)

```bash
git clone https://github.com/yourusername/retreat-marketing-planner.git
cd retreat-marketing-planner
cp /path/to/index.html .
git add index.html
git commit -m "Add marketing planner web app"
git push origin main
```

### Step 3: Enable GitHub Pages

1. In your repository, click **"Settings"** (top tab)
2. Click **"Pages"** in the left sidebar
3. Under **"Source"**, select **"Deploy from a branch"**
4. Select branch: **main** (or **master**)
5. Select folder: **/ (root)**
6. Click **"Save"**

### Step 4: Wait for Deployment

- GitHub will build your site (takes 1-2 minutes)
- You'll see a success message with your URL
- Your app is live at: `https://yourusername.github.io/retreat-marketing-planner`

### Step 5: Visit Your App!

Click the link or go to:
```
https://yourusername.github.io/retreat-marketing-planner
```

🎉 **That's it! Your app is live and free forever!**

---

## 🎨 Optional: Custom Domain

Want to use `marketing.adventureyogi.com` instead?

### Step 1: Add CNAME Record

In your repository:

1. Click **"Add file"** → **"Create new file"**
2. Name it: `CNAME`
3. Content: `marketing.adventureyogi.com`
4. Click **"Commit changes"**

### Step 2: Configure DNS

In your domain provider (e.g., Namecheap, GoDaddy):

1. Add a CNAME record:
   ```
   Type: CNAME
   Host: marketing
   Value: yourusername.github.io
   TTL: Automatic
   ```

2. Wait 1-24 hours for DNS propagation

3. Go back to GitHub → Settings → Pages
4. Enter your custom domain: `marketing.adventureyogi.com`
5. Check **"Enforce HTTPS"**

Done! Your app is at your custom domain.

---

## 🔄 Updating Your App

When you want to make changes:

1. Edit `index.html` locally
2. Go to your GitHub repository
3. Click on `index.html`
4. Click the pencil icon (✏️) to edit
5. Paste your new code
6. Scroll down and click **"Commit changes"**
7. Wait 1-2 minutes for automatic re-deployment

---

## 🛠️ Alternative Hosting Options

### Netlify (Also Free & Easier)

1. Go to [netlify.com](https://www.netlify.com/)
2. Drag and drop `index.html`
3. Get instant URL (e.g., `amazing-name-123.netlify.app`)
4. Optional: Add custom domain

**Pros:**
- Even easier than GitHub Pages
- Instant deployment
- Great free tier
- Automatic HTTPS
- Easy custom domains

### Vercel (Also Free)

1. Go to [vercel.com](https://vercel.com/)
2. Import your GitHub repository
3. Deploy with one click
4. Get instant URL

**Pros:**
- Super fast
- Automatic deployments on Git push
- Great developer experience

---

## 📱 Sharing Your App

Once deployed, share the link with your team:

```
Marketing Planner: https://yourusername.github.io/retreat-marketing-planner
```

Anyone can use it - no installation required!

---

## 🔐 Security Notes

### ✅ Safe to Deploy
- No server-side code
- No database
- No sensitive data stored
- All processing in browser
- API tokens never leave the user's browser

### 🔒 Keep Private
- Don't commit API tokens to Git
- Don't share your Bookinglayer token
- Users enter their own tokens (not stored)

---

## 🎊 You're Done!

Your Adventure Yogi Retreat Marketing Planner is:

- ✅ Live on the internet
- ✅ Accessible from anywhere
- ✅ Free to host
- ✅ Automatic HTTPS
- ✅ Fast and reliable

**Share it with your team and start planning those retreats!** 🧘‍♀️✨

---

## 📞 Need Help?

### GitHub Pages Not Working?

**Check:**
- Is your repository public?
- Did you select the correct branch?
- Did you wait 1-2 minutes after enabling Pages?
- Is the file named exactly `index.html`?

**Common Fixes:**
- Try Settings → Pages → Save again
- Clear your browser cache
- Try a different browser
- Check GitHub Status page

### Still Stuck?

1. Check your repository is public
2. Verify `index.html` is in the root directory
3. Look for a green checkmark next to your commit
4. Check the Actions tab for build status

---

## 🎯 Quick Troubleshooting

| Issue | Solution |
|-------|----------|
| 404 Page Not Found | Wait 2 minutes, or check file is named `index.html` |
| CSS not loading | Check all code is in one HTML file |
| API not working | User needs valid Bookinglayer token |
| Blank page | Check browser console for errors |

---

**Ready to deploy? Let's go!** 🚀
