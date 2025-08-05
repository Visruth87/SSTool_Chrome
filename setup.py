"""
Setup script for URL Screenshot Tool
Handles installation and project initialization.
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def install_requirements():
    """Install required packages from requirements.txt"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to install requirements: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    print("Creating project directories...")
    directories = ["screenshots", "samples", "output"]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✓ Created directory: {directory}")

def check_chrome_installation():
    """Check if Chrome is installed"""
    print("Checking Chrome installation...")
    
    system = platform.system().lower()
    chrome_paths = []
    
    if system == "windows":
        chrome_paths = [
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
            os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")
        ]
    elif system == "darwin":  # macOS
        chrome_paths = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        ]
    elif system == "linux":
        chrome_paths = [
            "/usr/bin/google-chrome",
            "/usr/bin/google-chrome-stable",
            "/usr/bin/chromium-browser"
        ]
    
    for path in chrome_paths:
        if os.path.exists(path):
            print(f"✓ Chrome found at: {path}")
            return True
    
    print("⚠ Chrome not found. Please install Google Chrome to use this application.")
    print("Download from: https://www.google.com/chrome/")
    return False

def create_sample_files():
    """Create sample input files if they don't exist"""
    print("Creating sample files...")
    
    # Sample TXT file
    txt_path = Path("samples/sample_urls.txt")
    if not txt_path.exists():
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write("""# Sample URL file for URL Screenshot Tool
# Format: NAME|URL or NAME,URL or just URL
# Lines starting with # are comments

Google|https://www.google.com
GitHub|https://github.com
Stack Overflow,https://stackoverflow.com
Python Official,https://www.python.org
Wikipedia|https://www.wikipedia.org
""")
        print("✓ Created sample_urls.txt")
    
    # Sample CSV file
    csv_path = Path("samples/sample_urls.csv")
    if not csv_path.exists():
        with open(csv_path, 'w', encoding='utf-8') as f:
            f.write("""Name,URL
Google,https://www.google.com
GitHub,https://github.com
Stack Overflow,https://stackoverflow.com
Python Official,https://www.python.org
Wikipedia,https://www.wikipedia.org
""")
        print("✓ Created sample_urls.csv")

def run_application():
    """Run the main application"""
    print("\nStarting URL Screenshot Tool...")
    try:
        subprocess.run([sys.executable, "main.py"])
    except KeyboardInterrupt:
        print("\nApplication terminated by user.")
    except Exception as e:
        print(f"Error running application: {e}")

def main():
    """Main setup function"""
    print("=" * 50)
    print("URL Screenshot Tool Setup")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("✗ Python 3.7 or higher is required!")
        sys.exit(1)
    
    print(f"✓ Python {sys.version.split()[0]} detected")
    
    # Create directories
    create_directories()
    
    # Install requirements
    if not install_requirements():
        print("Setup failed. Please install requirements manually:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    
    # Check Chrome
    chrome_installed = check_chrome_installation()
    
    # Create sample files
    create_sample_files()
    
    print("\n" + "=" * 50)
    print("Setup completed successfully!")
    print("=" * 50)
    
    if not chrome_installed:
        print("⚠ Warning: Chrome not detected. Please install Chrome before using the application.")
    
    print("\nTo start the application, run:")
    print("python main.py")
    
    # Ask if user wants to run the application now
    try:
        response = input("\nWould you like to start the application now? (y/n): ")
        if response.lower() in ['y', 'yes']:
            run_application()
    except KeyboardInterrupt:
        print("\nSetup complete. Run 'python main.py' to start the application.")

if __name__ == "__main__":
    main() 