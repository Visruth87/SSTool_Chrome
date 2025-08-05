# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
python setup.py
```
*This will automatically install all required packages and set up the project.*

### Step 2: Run the Application
```bash
python main.py
```

### Step 3: Take Your First Screenshot
1. **Set screenshot location**: Choose where to save screenshots (optional)
2. In the GUI, enter a URL name like "Google"
3. Enter the URL: `https://www.google.com`
4. Click "Add URL"
5. Click "Start Screenshot Process"
6. Wait for Chrome to open and take the screenshot
7. Your DOCX file will be created automatically!

## 📁 Sample Files Included

Try loading the sample files to test the application:
- `samples/sample_urls.txt` - Text file format
- `samples/sample_urls.csv` - CSV file format

## 🎯 Quick Tips

- **Chrome Required**: Make sure Google Chrome is installed and up to date
- **Desktop Screenshots**: The app captures your full desktop with enlarged Chrome windows (1920x1080)
- **New Tabs**: Each URL opens in a new tab for better organization
- **Multiple URLs**: Load many URLs at once from TXT or CSV files
- **Custom Locations**: Choose where to save both screenshots and DOCX files

## 📝 File Formats

### TXT File Format
```
# Comments start with #
Google|https://www.google.com
GitHub,https://github.com
https://www.python.org
```

### CSV File Format
```csv
Name,URL
Google,https://www.google.com
GitHub,https://github.com
Python,https://www.python.org
```

## ⚡ Troubleshooting

| Problem | Solution |
|---------|----------|
| Chrome driver error | Make sure Google Chrome is installed and up to date |
| Network/Firewall issues | Download Chrome driver manually from chromedriver.chromium.org |
| Permission denied | Run as administrator |
| Package installation fails | Try `pip install selenium webdriver-manager python-docx pillow pyautogui pandas` |
| URL won't load | Some sites may block automated browsers |

## 🎉 That's it!

Your URL Screenshot Tool is ready to use. For advanced features and customization, see the full [README.md](README.md). 