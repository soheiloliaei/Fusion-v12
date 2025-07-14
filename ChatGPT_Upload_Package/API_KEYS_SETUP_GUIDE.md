# 🔑 **API KEYS SETUP GUIDE - DESIGN INSPIRATION PLATFORMS**

## 🚀 **QUICK SETUP CHECKLIST**

### **📌 REQUIRED API KEYS**
- [ ] **Pinterest API** - Developer account required
- [ ] **Dribbble API** - Free developer account
- [ ] **Behance API** - Adobe Developer account
- [ ] **Optional**: Twitter API v2 (now paid, $100/month minimum)

### **📋 SETUP ORDER (Recommended)**
1. **Start with Dribbble** (easiest, free)
2. **Then Behance** (free with Adobe account)
3. **Finally Pinterest** (requires approval)
4. **Skip Twitter** (expensive, use RSS alternatives)

---

## 🎯 **DRIBBBLE API (RECOMMENDED FIRST)**

### **🔗 Where to Get It**
**URL**: https://dribbble.com/account/applications/new

### **📝 Step-by-Step Setup**
1. **Create Dribbble Account**:
   - Go to https://dribbble.com/signup
   - Free account is sufficient

2. **Register Application**:
   - Visit: https://dribbble.com/account/applications/new
   - **Name**: "Design Inspiration Tool"
   - **Description**: "Personal design inspiration aggregator"
   - **Website**: Your website or "http://localhost:3000"
   - **Callback URL**: "http://localhost:3000/callback"

3. **Get Your Keys**:
   - **Client ID**: Copy this value
   - **Client Secret**: Copy this value
   - **Access Token**: Generate one for personal use

### **⚡ RATE LIMITS**
- **60 requests per minute**
- **Free tier**: Sufficient for personal use
- **No approval required**

---

## 🏢 **BEHANCE API**

### **🔗 Where to Get It**
**URL**: https://www.adobe.io/apis/creativecloud/behance.html

### **📝 Step-by-Step Setup**
1. **Create Adobe Developer Account**:
   - Go to https://developer.adobe.com/
   - Sign in with Adobe ID (free)

2. **Create New Project**:
   - Click "Create new project"
   - **Project Name**: "Design Inspiration Tool"
   - **Description**: "Personal design inspiration aggregator"

3. **Add Behance API**:
   - Click "Add API"
   - Select "Behance API"
   - Choose "OAuth Server-to-Server"

4. **Get Your Keys**:
   - **API Key (Client ID)**: Copy this value
   - **Client Secret**: Copy this value

### **⚡ RATE LIMITS**
- **1000 requests per hour**
- **Free tier**: Excellent for personal use
- **No approval required**

---

## 📌 **PINTEREST API (REQUIRES APPROVAL)**

### **🔗 Where to Get It**
**URL**: https://developers.pinterest.com/docs/getting-started/

### **📝 Step-by-Step Setup**
1. **Create Pinterest Business Account**:
   - Go to https://business.pinterest.com/
   - Convert personal account or create new business account

2. **Apply for Developer Access**:
   - Visit: https://developers.pinterest.com/docs/getting-started/
   - Click "Request access"
   - **Application**: Describe your use case
   - **Website**: Your website or GitHub profile

3. **Create App** (After Approval):
   - Go to https://developers.pinterest.com/apps/
   - Click "Create app"
   - **App Name**: "Design Inspiration Tool"
   - **Description**: "Personal design inspiration aggregator"

4. **Get Your Keys**:
   - **App ID**: Copy this value
   - **App Secret**: Copy this value

### **⚡ RATE LIMITS**
- **1000 requests per hour** (free tier)
- **Approval required**: Can take 1-2 weeks
- **Terms**: Must comply with Pinterest brand guidelines

### **🎯 APPROVAL TIPS**
- **Be specific**: "Personal design inspiration aggregator for UX research"
- **Show legitimacy**: Link to your portfolio or GitHub
- **Business use**: Explain how it helps your design work
- **Compliance**: Mention you'll follow Pinterest guidelines

---

## 🐦 **TWITTER API v2 (OPTIONAL - EXPENSIVE)**

### **🔗 Where to Get It**
**URL**: https://developer.twitter.com/en/docs/twitter-api

### **💰 COST WARNING**
- **Basic**: $100/month (minimum)
- **Free tier**: Extremely limited (1,500 posts/month)
- **Not recommended**: Use RSS alternatives instead

### **📝 If You Really Want It**
1. **Create Twitter Developer Account**:
   - Go to https://developer.twitter.com/
   - Apply for developer access

2. **Choose Plan**:
   - **Basic**: $100/month
   - **Pro**: $5,000/month
   - **Enterprise**: Custom pricing

3. **Get Your Keys**:
   - **API Key**: Copy this value
   - **API Secret**: Copy this value
   - **Bearer Token**: Copy this value

### **🔄 RECOMMENDED ALTERNATIVE**
Use RSS feeds instead:
- **Awwwards**: https://www.awwwards.com/rss/
- **CSS-Tricks**: https://css-tricks.com/feed/
- **Smashing Magazine**: https://www.smashingmagazine.com/feed/
- **Designer News**: https://www.designernews.co/

---

## 📋 **CONFIGURATION SETUP**

### **📁 Create API Keys File**
Create `api_keys.json` in your project root:

```json
{
  "dribbble": {
    "client_id": "YOUR_DRIBBBLE_CLIENT_ID",
    "client_secret": "YOUR_DRIBBBLE_CLIENT_SECRET",
    "access_token": "YOUR_DRIBBBLE_ACCESS_TOKEN"
  },
  "behance": {
    "api_key": "YOUR_BEHANCE_API_KEY",
    "client_secret": "YOUR_BEHANCE_CLIENT_SECRET"
  },
  "pinterest": {
    "app_id": "YOUR_PINTEREST_APP_ID",
    "app_secret": "YOUR_PINTEREST_APP_SECRET"
  },
  "twitter": {
    "api_key": "YOUR_TWITTER_API_KEY",
    "api_secret": "YOUR_TWITTER_API_SECRET",
    "bearer_token": "YOUR_TWITTER_BEARER_TOKEN"
  }
}
```

### **🔒 Security Note**
Add `api_keys.json` to your `.gitignore` file to keep keys secure.

---

## ⚡ **QUICK START RECOMMENDATIONS**

### **🎯 Start with These (Free & Fast)**
1. **Dribbble API** - 5 minutes setup, works immediately
2. **Behance API** - 10 minutes setup, works immediately
3. **RSS Feeds** - No setup, works immediately

### **📋 Optional Later**
4. **Pinterest API** - Apply and wait for approval
5. **Skip Twitter** - Use RSS feeds instead

### **🚀 Test Your Setup**
Run the design inspiration API with your keys:
```bash
python3 design_inspiration_api.py
```

---

## 🆘 **TROUBLESHOOTING**

### **Common Issues**
- **Rate Limits**: Start with small requests, increase gradually
- **Authentication**: Double-check all keys are copied correctly
- **Approval Delays**: Pinterest can take 1-2 weeks
- **CORS Issues**: Use server-side API calls, not client-side

### **Support Resources**
- **Dribbble**: https://dribbble.com/api
- **Behance**: https://www.behance.net/dev/api/endpoints/
- **Pinterest**: https://developers.pinterest.com/docs/api/v5/

---

## ✅ **READY TO USE**

Once you have your API keys configured, you can:
1. **Run design inspiration API** independently
2. **Use with PRP builder** for automatic inspiration
3. **Integrate with Fusion v11** for enhanced context

**Next Step**: Run `python3 design_inspiration_api.py` to test your setup! 