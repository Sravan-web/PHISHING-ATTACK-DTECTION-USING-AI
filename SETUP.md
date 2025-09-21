# Phishing Detection MVP - Setup Guide

This guide will help you set up and run the phishing detection system on your Windows machine.

## Prerequisites

- **Python 3.8 or higher** (Download from [python.org](https://python.org))
- **Git** (Download from [git-scm.com](https://git-scm.com))
- **Chrome Browser** (for testing the browser extension)
- **PowerShell** (pre-installed on Windows)

## Quick Setup

### 1. Verify Python Installation

Open PowerShell and run:
```powershell
python --version
```

You should see Python 3.8+ displayed. If not, install Python first.

### 2. Navigate to Project Directory

```powershell
cd C:\Users\rajli\phishing-detection-mvp
```

### 3. Create Virtual Environment

```powershell
python -m venv venv
```

### 4. Activate Virtual Environment

```powershell
.\venv\Scripts\Activate
```

Your prompt should now show `(venv)` at the beginning.

### 5. Install Dependencies

```powershell
pip install -r requirements.txt
```

This will install all required packages including:
- Flask (web API)
- scikit-learn (machine learning)
- NLTK (natural language processing)
- BeautifulSoup (web scraping)
- And other dependencies

### 6. Download NLTK Data

Start Python and run:
```powershell
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

## Running the System

### 1. Start the API Server

```powershell
python src\api\app.py
```

You should see:
```
Starting Phishing Detection API...
API will be available at: http://localhost:5000
```

Keep this terminal open - the API server is now running.

### 2. Test the API

Open a new PowerShell window and test:
```powershell
curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d '{"url": "https://www.google.com"}'
```

You should receive a JSON response with analysis results.

### 3. Install Browser Extension (Optional)

1. Open Chrome and go to `chrome://extensions/`
2. Enable "Developer mode" (toggle in top-right)
3. Click "Load unpacked"
4. Select the `browser-extension` folder in your project directory
5. The extension should now appear in your toolbar

## Testing the System

### Run Automated Tests

With the API server running, open another terminal and run:
```powershell
cd C:\Users\rajli\phishing-detection-mvp
.\venv\Scripts\Activate
python tests\test_detection.py
```

This will test all components and show detailed results.

### Manual Testing

#### Test URL Analysis Only:
```powershell
curl -X POST http://localhost:5000/quick-check -H "Content-Type: application/json" -d '{"url": "https://suspicious-site.tk"}'
```

#### Test with Text Content:
```powershell
curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d '{"url": "https://example.com", "text": "URGENT! Your account has been suspended! Click here immediately!"}'
```

#### Test Batch Analysis:
```powershell
curl -X POST http://localhost:5000/batch-analyze -H "Content-Type: application/json" -d '{"urls": ["https://google.com", "https://suspicious-site.tk"]}'
```

## Browser Extension Usage

1. **Installation**: Follow the steps above to install the extension
2. **Automatic Protection**: The extension automatically checks URLs you visit
3. **Manual Analysis**: Click the extension icon to manually analyze the current page
4. **Warning System**: 
   - Green badge: Safe site
   - Yellow badge: Low risk
   - Orange badge: Medium risk  
   - Red badge with "!": High risk
   - Red badge with "X": API unavailable

## Troubleshooting

### Python Not Found
- Make sure Python is installed and added to PATH
- Try `py` instead of `python` on some Windows systems

### Permission Errors
- Run PowerShell as Administrator if needed
- Check that you have write permissions in the project directory

### API Not Starting
- Check if port 5000 is already in use
- Try changing the port in `src\api\app.py` (last line)

### Module Import Errors
- Make sure the virtual environment is activated
- Reinstall requirements: `pip install -r requirements.txt`

### Browser Extension Issues
- Make sure the API server is running on localhost:5000
- Check Chrome's Developer Tools Console for error messages
- Verify the extension is enabled in `chrome://extensions/`

### SSL/Certificate Errors
- These are expected for suspicious sites and contribute to risk scoring
- The system handles these gracefully

## Performance Notes

- **URL Analysis**: ~10-50ms per URL
- **Text Analysis**: ~100-200ms per text sample
- **Content Analysis**: ~1-3 seconds per webpage (depends on site size)
- **API Response**: Typically under 100ms for quick-check, 1-5s for full analysis

## Security Notes

- The system runs locally on your machine
- No data is sent to external servers (except when analyzing target URLs)
- All analysis is performed locally
- Browser extension only communicates with your local API server

## Next Steps

Once you have the basic system running:

1. **Customize Detection Rules**: Edit the analyzer files to add custom patterns
2. **Improve Training Data**: Add more examples in the ML classifier
3. **Enhance UI**: Modify the browser extension popup for better user experience
4. **Add Logging**: Implement logging for production use
5. **Deploy**: Consider deploying the API to a cloud service for team use

## Getting Help

If you encounter issues:

1. Check the console output for error messages
2. Verify all prerequisites are installed
3. Make sure the virtual environment is activated
4. Try restarting the API server
5. Check the troubleshooting section above

The system is designed to be resilient - if one component fails, others should continue working.