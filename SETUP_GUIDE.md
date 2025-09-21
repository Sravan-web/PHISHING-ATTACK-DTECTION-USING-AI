# 🛡️ Phishing Detection System - VS Code Setup Guide

## Complete Setup Instructions for a Fresh Windows PC

This guide will help you run the phishing detection system from scratch on any Windows PC using VS Code.

---

## 📋 Prerequisites

### Step 1: Install Python
1. **Download Python 3.8 or later** from [python.org](https://www.python.org/downloads/)
2. **IMPORTANT**: During installation, check "Add Python to PATH"
3. Verify installation:
   ```cmd
   python --version
   pip --version
   ```

### Step 2: Install VS Code
1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install with default settings
3. **Install recommended extensions**:
   - Python (Microsoft)
   - Live Server (optional, for serving HTML)
   - Thunder Client (optional, for API testing)

### Step 3: Install Git (Optional but Recommended)
1. Download from [git-scm.com](https://git-scm.com/downloads)
2. Install with default settings

---

## 🚀 Project Setup

### Option A: If you have the project files
1. **Copy the entire project folder** to your desired location (e.g., `C:\Users\YourName\phishing-detection-mvp`)

### Option B: If you have a Git repository
1. Open Command Prompt or PowerShell
2. Navigate to your desired directory:
   ```cmd
   cd C:\Users\YourName\
   ```
3. Clone the repository:
   ```cmd
   git clone [repository-url]
   cd phishing-detection-mvp
   ```

### Step 3: Open Project in VS Code
1. **Launch VS Code**
2. **Open the project folder**:
   - File → Open Folder → Select `phishing-detection-mvp` folder
   - OR press `Ctrl+K, Ctrl+O`

---

## 🐍 Python Environment Setup

### Step 1: Create Virtual Environment
In VS Code, open the **integrated terminal** (`Ctrl+`` ` or View → Terminal):

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1

# If you get execution policy error, run this first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# On Windows Command Prompt:
venv\Scripts\activate.bat
```

You should see `(venv)` at the beginning of your terminal prompt.

### Step 2: Install Python Dependencies
```powershell
# Ensure you're in the project root directory
# Install all required packages
pip install -r requirements.txt

# If you get any errors, try updating pip first:
python -m pip install --upgrade pip
```

### Step 3: Download NLTK Data (Required for Text Analysis)
```powershell
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

---

## 🖥️ VS Code Configuration

### Step 1: Set Python Interpreter
1. **Press `Ctrl+Shift+P`** to open command palette
2. Type "Python: Select Interpreter"
3. **Select the virtual environment Python**:
   - Should show path like: `.\venv\Scripts\python.exe`
   - If not visible, click "Enter interpreter path..." and browse to `venv\Scripts\python.exe`

### Step 2: Configure Terminal (Optional)
1. **Press `Ctrl+Shift+P`**
2. Type "Terminal: Select Default Profile"
3. Choose **PowerShell** or **Command Prompt** based on preference

---

## 🎯 Running the System

### Step 1: Start the Backend API
In VS Code terminal (ensure virtual environment is activated):

```powershell
# Navigate to API directory
cd src\api

# Start the Flask server
python app.py
```

You should see output like:
```
Starting Phishing Detection API...
API will be available at: http://localhost:5000
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://localhost:5000
```

**Keep this terminal running** - this is your API server.

### Step 2: Open the Web Interface

#### Method 1: Direct File Access (Simple)
1. **Open a new terminal** in VS Code (`Ctrl+Shift+`` `)
2. Navigate to web-ui folder:
   ```powershell
   cd web-ui
   ```
3. **Open index.html** in your browser:
   - Right-click on `index.html` in VS Code Explorer
   - Select "Open with Live Server" (if installed)
   - OR simply double-click `index.html` to open in default browser

#### Method 2: Local HTTP Server (Recommended)
1. **Open a new terminal** in VS Code (`Ctrl+Shift+`` `)
2. Navigate to web-ui and start HTTP server:
   ```powershell
   cd web-ui
   python -m http.server 8080
   ```
3. **Open browser** and go to: `http://localhost:8080`

---

## 🧪 Testing the System

### Step 1: Verify API is Running
1. Open browser to `http://localhost:5000/health`
2. You should see JSON response: `{"status": "healthy", ...}`

### Step 2: Test the Dashboard
1. **Open the main interface** (index.html)
2. **Check API status** - top right should show "API Online" in green
3. **Test URL analysis**:
   - Enter a safe URL: `https://github.com`
   - Click "Analyze" button
   - Should see results within a few seconds

### Step 3: Run the Test Suite
1. **Open** `web-ui/test-dashboard.html` in your browser
2. **Click "Run All Tests"** button
3. **Verify** all tests pass (green checkmarks)

---

## 🔧 Troubleshooting

### Common Issues & Solutions

#### 1. "Python is not recognized"
**Solution**: Add Python to PATH:
- Search "Environment Variables" in Windows
- Edit Path variable, add Python installation directory
- Restart VS Code

#### 2. "pip is not recognized"
**Solution**: 
```powershell
python -m pip --version
# Use 'python -m pip' instead of 'pip'
```

#### 3. API Server Won't Start
**Check these**:
- Virtual environment is activated (`(venv)` in terminal)
- Port 5000 is not in use
- All dependencies installed correctly

**Verify dependencies**:
```powershell
pip list
```

#### 4. "Module not found" Errors
**Solution**:
```powershell
# Reinstall requirements
pip install --upgrade -r requirements.txt
```

#### 5. Dashboard Shows "API Offline"
**Check**:
- API server is running (Step 1 above)
- No firewall blocking localhost:5000
- Browser console for error messages (F12 → Console)

#### 6. Charts Not Loading
**Solution**:
- Check browser console for JavaScript errors
- Ensure internet connection (for Chart.js CDN)
- Hard refresh browser (`Ctrl+F5`)

#### 7. Permission Errors on Windows
**Solution**:
```powershell
# Run VS Code as Administrator
# OR set execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📁 Project Structure Understanding

```
phishing-detection-mvp/
├── src/                    # Backend Python code
│   ├── api/
│   │   └── app.py         # Flask API server (START HERE)
│   ├── core/              # Analysis modules
│   └── ml/                # Machine learning
├── web-ui/                # Frontend dashboard
│   ├── index.html         # Main interface (OPEN THIS)
│   ├── test-dashboard.html # Testing suite
│   ├── js/                # JavaScript files
│   └── css/               # Stylesheets
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

---

## 🎯 Quick Start Checklist

- [ ] Python 3.8+ installed with PATH
- [ ] VS Code installed with Python extension
- [ ] Project folder opened in VS Code
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] NLTK data downloaded
- [ ] API server running (`python src/api/app.py`)
- [ ] Web interface opened (index.html)
- [ ] API status shows "Online" in dashboard
- [ ] Test analysis with sample URL works

---

## 🎮 Using the System

### Main Features Available:

1. **URL Analysis**
   - Enter any URL in the main input field
   - Toggle "Include content analysis" for detailed scan
   - View results in interactive tabs

2. **Text Analysis**
   - Paste suspicious email content
   - Analyze for phishing keywords and patterns

3. **Batch Analysis**
   - Enter multiple URLs (one per line)
   - Process up to 10 URLs simultaneously

4. **Email Analysis**
   - Drag & drop .eml/.msg files
   - Complete header and content analysis

5. **Real-time Dashboard**
   - Live threat monitoring
   - Interactive charts and statistics
   - Activity feed of recent analyses

6. **Settings**
   - API endpoint configuration
   - Notification preferences
   - Dark mode toggle

---

## 📞 Getting Help

### If you encounter issues:

1. **Check the Console**:
   - VS Code Terminal for Python errors
   - Browser Console (F12) for JavaScript errors

2. **Verify Setup**:
   - Run the test suite (`test-dashboard.html`)
   - Check API health endpoint directly

3. **Common Commands**:
   ```powershell
   # Restart API server
   Ctrl+C (to stop)
   python src/api/app.py (to restart)
   
   # Reinstall dependencies
   pip install --force-reinstall -r requirements.txt
   
   # Check Python environment
   where python
   pip list
   ```

---

## 🎉 Success!

If everything is working correctly, you should have:
- ✅ API server running on `http://localhost:5000`
- ✅ Web dashboard accessible and showing "API Online"
- ✅ Ability to analyze URLs and see detailed results
- ✅ Interactive charts showing threat intelligence
- ✅ All tests passing in the test suite

**You're ready to use the Phishing Detection System!** 🛡️

---

**Note**: This system is designed for educational and legitimate security purposes. Always ensure you're analyzing URLs safely and in compliance with applicable laws and regulations.