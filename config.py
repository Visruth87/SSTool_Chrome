"""
Configuration file for URL Screenshot Tool
Contains application settings and constants.
"""

import os
from pathlib import Path

# Application Information
APP_NAME = "URL Screenshot Tool"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Your Name"

# File Paths
PROJECT_ROOT = Path(__file__).parent
SCREENSHOTS_DIR = PROJECT_ROOT / "screenshots"
SAMPLES_DIR = PROJECT_ROOT / "samples"
OUTPUT_DIR = PROJECT_ROOT / "output"

# Screenshot Settings
SCREENSHOT_SETTINGS = {
    "wait_time": 3,  # Seconds to wait for page load
    "max_retries": 3,  # Maximum number of retry attempts
    "retry_delay": 2,  # Seconds to wait between retries
    "timeout": 30,  # Page load timeout in seconds
}

# Chrome Driver Settings
CHROME_OPTIONS = [
    "--start-maximized",
    "--disable-notifications",
    "--disable-popup-blocking",
    "--disable-web-security",
    "--allow-running-insecure-content",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-extensions",
    "--disable-plugins",
    "--window-size=1920,1080",
]

# DOCX Document Settings
DOCX_SETTINGS = {
    "max_image_width_inches": 6,
    "max_image_height_inches": 8,
    "image_quality": 85,  # JPEG quality for images
    "compress_images": True,
}

# File Format Settings
SUPPORTED_IMAGE_FORMATS = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
SUPPORTED_URL_FILE_FORMATS = ['.txt', '.csv']

# URL Validation Settings
URL_VALIDATION = {
    "require_protocol": False,  # If False, will add https:// automatically
    "allowed_protocols": ["http", "https"],
    "timeout": 10,  # Timeout for URL accessibility check
}

# GUI Settings
GUI_SETTINGS = {
    "window_width": 800,
    "window_height": 600,
    "min_width": 600,
    "min_height": 400,
    "theme": "default",  # Can be "default", "clam", "alt", "classic"
}

# Logging Settings
LOGGING_CONFIG = {
    "level": "INFO",  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": "url_screenshot_tool.log",
    "max_size_mb": 10,
    "backup_count": 5,
}

# Sample Data
SAMPLE_URLS = [
    ("Google", "https://www.google.com"),
    ("GitHub", "https://github.com"),
    ("Stack Overflow", "https://stackoverflow.com"),
    ("Python.org", "https://www.python.org"),
    ("Wikipedia", "https://www.wikipedia.org"),
]

# Error Messages
ERROR_MESSAGES = {
    "no_urls": "No URLs provided. Please add some URLs first.",
    "invalid_output": "Please specify a valid output file path.",
    "chrome_driver_error": "Failed to initialize Chrome driver. Please ensure Chrome is installed.",
    "screenshot_error": "Failed to take screenshot for {url}: {error}",
    "file_not_found": "File not found: {file_path}",
    "invalid_file_format": "Unsupported file format: {file_format}",
    "docx_creation_error": "Failed to create DOCX document: {error}",
}

# Success Messages
SUCCESS_MESSAGES = {
    "urls_loaded": "Successfully loaded {count} URLs from {file}",
    "screenshot_taken": "Screenshot taken for {name}",
    "docx_created": "DOCX document created successfully: {file_path}",
    "process_completed": "Screenshot process completed successfully!",
}

def ensure_directories():
    """Create necessary directories if they don't exist"""
    directories = [SCREENSHOTS_DIR, SAMPLES_DIR, OUTPUT_DIR]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)

def get_default_output_filename():
    """Generate default output filename with timestamp"""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"url_screenshots_{timestamp}.docx"

def validate_config():
    """Validate configuration settings"""
    errors = []
    
    # Validate screenshot settings
    if SCREENSHOT_SETTINGS["wait_time"] <= 0:
        errors.append("wait_time must be positive")
        
    if SCREENSHOT_SETTINGS["max_retries"] < 0:
        errors.append("max_retries must be non-negative")
        
    if SCREENSHOT_SETTINGS["timeout"] <= 0:
        errors.append("timeout must be positive")
    
    # Validate DOCX settings
    if DOCX_SETTINGS["max_image_width_inches"] <= 0:
        errors.append("max_image_width_inches must be positive")
        
    if DOCX_SETTINGS["max_image_height_inches"] <= 0:
        errors.append("max_image_height_inches must be positive")
        
    if not 0 <= DOCX_SETTINGS["image_quality"] <= 100:
        errors.append("image_quality must be between 0 and 100")
    
    # Validate GUI settings
    if GUI_SETTINGS["window_width"] <= 0 or GUI_SETTINGS["window_height"] <= 0:
        errors.append("Window dimensions must be positive")
        
    if GUI_SETTINGS["min_width"] <= 0 or GUI_SETTINGS["min_height"] <= 0:
        errors.append("Minimum window dimensions must be positive")
    
    if errors:
        raise ValueError(f"Configuration validation failed: {'; '.join(errors)}")
    
    return True

# Initialize directories when module is imported
ensure_directories() 