# URL Screenshot Tool

A Python GUI application that takes screenshots of websites and saves them to DOCX documents. The application uses Google Chrome to load URLs from various sources (manual input, TXT files, CSV files) and capture full desktop screenshots.

## Features

- 🖥️ **Desktop Screenshots**: Captures full desktop screenshots with enlarged Chrome windows (1920x1080)
- 📝 **Multiple Input Methods**: 
  - Manual URL entry
  - Load from TXT files
  - Load from CSV files
- 📄 **DOCX Output**: Automatically generates Word documents with screenshots and URL information
- 🔄 **Batch Processing**: Process multiple URLs in sequence using new tabs
- 📊 **Progress Tracking**: Real-time progress updates and logging
- ⏹️ **Cancellable Operations**: Stop the process at any time
- 📁 **Custom Locations**: Choose where to save screenshots and DOCX files
- 🎨 **Professional GUI**: User-friendly interface built with tkinter

## Prerequisites

- Python 3.7 or higher
- **Google Chrome** browser installed
- Windows, macOS, or Linux

## Installation

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/yourusername/url-screenshot-tool.git
   cd url-screenshot-tool
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## Usage

### Manual URL Entry
1. Enter a URL name in the "URL Name" field
2. Enter the URL in the "URL" field
3. Click "Add URL" to add it to the list

### Loading from Files

#### TXT File Format
Create a text file with URLs in one of these formats:
```
# Comments start with #
Google|https://www.google.com
GitHub,https://github.com
https://www.python.org
Stack Overflow|https://stackoverflow.com
```

#### CSV File Format
Create a CSV file with two columns (Name, URL):
```csv
Name,URL
Google,https://www.google.com
GitHub,https://github.com
Python,https://www.python.org
```

### Taking Screenshots
1. **Set Screenshot Location**: Choose where to save screenshot files (optional)
2. Load your URLs using any of the input methods above
3. Specify an output DOCX file name (or use the default)
4. Click "Start Screenshot Process"
5. Wait for the process to complete

The application will:
- Open Chrome with maximized windows (1920x1080)
- Open each URL in a new tab
- Wait for the page to load
- Take a full desktop screenshot
- Move to the next URL
- Generate a DOCX document with all screenshots

## File Structure

```
url-screenshot-tool/
├── main.py                 # Main GUI application
├── screenshot_manager.py   # Chrome automation and screenshot capture
├── url_processor.py        # URL file loading and processing
├── docx_generator.py       # DOCX document creation
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── screenshots/          # Directory for temporary screenshot files
├── samples/             # Sample input files
└── output/              # Default output directory
```

## Configuration

Edit `config.py` to customize:
- Screenshot timing and retry settings
- Chrome browser options
- DOCX document formatting
- GUI appearance
- File paths and directories

## Sample Files

The application can generate sample input files:

```python
from url_processor import URLProcessor

processor = URLProcessor()

# Create sample TXT file
processor.create_sample_txt_file("sample_urls.txt")

# Create sample CSV file
processor.create_sample_csv_file("sample_urls.csv")
```

## Troubleshooting

### Chrome Driver Issues
- **Automatic Download**: The application automatically downloads Chrome driver
- **Network Issues**: If download fails due to network/firewall, download manually
- **Manual Installation**: Download from https://chromedriver.chromium.org/
- **Version Mismatch**: Ensure Chrome browser and driver versions are compatible

### Screenshot Issues
- Make sure Chrome window is not minimized during capture
- Some websites may block automated browsers
- Increase wait time in config.py for slow-loading sites

### Permission Issues
- Run as administrator if you get permission errors
- Ensure the output directory is writable

### Memory Issues
- For many URLs, process them in smaller batches
- Close other applications to free up memory
- Reduce image quality in config.py if needed

## Dependencies

- **selenium**: Chrome browser automation
- **webdriver-manager**: Automatic Chrome driver management
- **python-docx**: DOCX document creation
- **Pillow**: Image processing
- **pyautogui**: Desktop screenshot capture
- **pandas**: CSV file processing
- **tkinter**: GUI framework (included with Python)

## Features in Detail

### Screenshot Manager
- Automatic Chrome driver setup and management
- Configurable page load waiting
- Multiple screenshot methods (desktop vs webpage only)
- Error handling and retry logic

### URL Processor
- Flexible file format support
- URL validation and normalization
- Automatic protocol addition (http/https)
- Comment support in TXT files

### DOCX Generator
- Professional document formatting
- Automatic image resizing
- Timestamp tracking
- Multiple document layout options

## Limitations

- Requires Chrome browser
- Desktop screenshots include entire screen
- Some websites may detect automation
- Large numbers of URLs may take significant time

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

[Your Name]

## Changelog

### Version 1.0.0
- Initial release
- Basic screenshot functionality
- GUI interface
- Multiple input methods
- DOCX output generation

## Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Create an issue on GitHub
3. Provide detailed error messages and system information

## Future Enhancements

- [ ] Multiple screenshot formats (PDF, HTML)
- [ ] Batch export options
- [ ] Website comparison features
- [ ] Scheduled screenshot capture
- [ ] Cloud storage integration
- [ ] Advanced filtering and sorting
- [ ] Custom Chrome profiles
- [ ] Headless mode option 