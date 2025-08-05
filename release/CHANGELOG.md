# Changelog

## Version 2.1.0 - Simplified Chrome-Only Version

### 🔄 **Major Simplification**
- **Removed multi-browser support** - Chrome only for better reliability
- **Simplified GUI** - Removed browser selection interface
- **Cleaner codebase** - Removed Edge/Firefox specific code
- **Focused development** - Single browser means better stability

### ✅ **What's Kept**
- All core screenshot functionality
- New tab handling for URLs
- Custom screenshot location selection
- Enhanced window sizing (1920x1080)
- Professional DOCX output
- All file input methods (manual, TXT, CSV)

### 🗑️ **What's Removed**
- Edge browser support
- Firefox browser support
- Browser selection GUI
- Multi-browser driver management
- Complex fallback mechanisms
- `install_drivers.py` utility
- Multi-browser troubleshooting documentation

## Version 2.0.0 - Enhanced Multi-Browser Support

### 🆕 New Features

#### **Multi-Browser Support**
- Added support for **Microsoft Edge** browser
- Added support for **Mozilla Firefox** browser
- Browser selection interface in Settings section
- Automatic driver management for all browsers

#### **Enhanced Screenshot Capabilities**
- **Larger screenshot windows**: All browsers now use 1920x1080 resolution
- **New tab handling**: URLs open in new tabs instead of replacing current tab
- **Custom screenshot location**: Users can choose where to save screenshot files
- **Improved window management**: Better window sizing and positioning

#### **Enhanced User Interface**
- **Settings Section**: New dedicated section for browser and location settings
- **Browser Selection**: Radio buttons for Chrome, Edge, and Firefox
- **Screenshot Location Picker**: Browse button to select custom screenshot folder
- **Improved Layout**: Better organized GUI with logical grouping

#### **Better File Management**
- Custom screenshot directory selection
- Maintains existing DOCX output location choice
- Better file organization options

### 🔧 Technical Improvements

#### **Browser Driver Management**
- Unified driver setup for all browsers
- Specific configurations for each browser type
- Better error handling for missing browsers
- Automatic driver download and management

#### **Enhanced Screenshot Process**
- New tab functionality for better URL management
- Improved window sizing (1920x1080 for all browsers)
- Better browser window positioning
- Enhanced wait times and page load detection

#### **Code Architecture**
- Modular browser setup methods
- Improved error handling and logging
- Better separation of concerns
- Enhanced configuration management

### 📚 Documentation Updates

#### **README.md**
- Updated features list to highlight multi-browser support
- Added browser installation requirements
- Updated usage instructions
- Enhanced dependency documentation

#### **QUICK_START.md**
- Added browser selection steps
- Updated troubleshooting guide
- Enhanced quick tips section
- Added browser-specific guidance

### 🛠️ Configuration Updates

#### **config.py**
- Added browser-specific settings
- Defined supported browsers list
- Enhanced error messages for each browser
- Browser-specific driver options

### 🔄 Migration from Version 1.0.0

**Backward Compatibility**: Existing functionality remains unchanged
- Chrome is still the default browser
- Default screenshot location remains "screenshots"
- All existing file formats and features work as before

**New Default Behavior**:
- URLs now open in new tabs by default
- Browser windows are larger (1920x1080)
- Enhanced error messages include browser-specific guidance

### 📋 Browser Support Matrix

| Browser | Status | Driver | Auto-Download | Notes |
|---------|--------|--------|---------------|-------|
| Chrome | ✅ Full | ChromeDriver | ✅ Yes | Default, most tested |
| Edge | ✅ Full | EdgeDriver | ✅ Yes | Windows recommended |
| Firefox | ✅ Full | GeckoDriver | ✅ Yes | Cross-platform |

### 🎯 User Benefits

1. **Flexibility**: Choose the browser that works best for specific websites
2. **Reliability**: Some sites work better in different browsers
3. **Better Screenshots**: Larger windows provide more detailed captures
4. **Organization**: New tabs keep URLs organized during batch processing
5. **Customization**: Choose where to save both screenshots and documents

### 🔧 System Requirements

- Python 3.7+
- At least one supported browser installed
- Updated webdriver-manager for automatic driver handling
- Same dependencies as v1.0.0 (no additional packages required)

### 🐛 Bug Fixes

- Fixed window sizing issues across different browsers
- Improved error handling for browser initialization
- Better cleanup of browser processes
- Enhanced tab management

### 🔮 Future Enhancements

- Browser profiles support
- Headless mode options
- Custom browser binary paths
- Mobile browser simulation
- Browser-specific screenshot options 