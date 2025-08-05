"""
Screenshot Manager
Handles Chrome browser automation and desktop screenshot capture.
"""

import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
from PIL import Image


class ScreenshotManager:
    def __init__(self, screenshots_dir="screenshots"):
        self.driver = None
        self.screenshots_dir = screenshots_dir
        self.setup_screenshots_directory()
        
    def setup_screenshots_directory(self):
        """Create screenshots directory if it doesn't exist"""
        if not os.path.exists(self.screenshots_dir):
            os.makedirs(self.screenshots_dir)
            
    def setup_driver(self):
        """Setup Chrome WebDriver with appropriate options"""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        
        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            return True
            
        except Exception as e:
            raise Exception(f"Failed to setup Chrome driver: {str(e)}")
            
    def take_screenshot(self, url, name, wait_time=3, use_new_tab=True):
        """
        Navigate to URL and take full desktop screenshot
        
        Args:
            url (str): URL to navigate to
            name (str): Name for the screenshot file
            wait_time (int): Time to wait for page load
            use_new_tab (bool): Whether to open URL in new tab
            
        Returns:
            str: Path to the saved screenshot
        """
        if not self.driver:
            raise Exception("Chrome driver not initialized")
            
        try:
            if use_new_tab and len(self.driver.window_handles) > 0:
                # Open URL in new tab
                self.driver.execute_script(f"window.open('{url}', '_blank');")
                # Switch to the new tab
                self.driver.switch_to.window(self.driver.window_handles[-1])
            else:
                # Navigate to URL in current tab
                self.driver.get(url)
            
            # Wait for page to load
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Additional wait for content to load
            time.sleep(wait_time)
            
            # Maximize window and bring to front
            self.driver.maximize_window()
            
            # Set window size for better screenshots
            self.driver.set_window_size(1920, 1080)
            
            # Additional wait to ensure window is properly resized
            time.sleep(1)
            
            # Take full desktop screenshot using pyautogui
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}.png"
            filepath = os.path.join(self.screenshots_dir, filename)
            
            # Take screenshot of entire desktop
            screenshot = pyautogui.screenshot()
            
            # Save screenshot
            screenshot.save(filepath)
            
            return filepath
            
        except Exception as e:
            raise Exception(f"Failed to take screenshot for {url}: {str(e)}")
            
    def take_webpage_screenshot(self, url, name):
        """
        Alternative method: Take screenshot of webpage content only
        
        Args:
            url (str): URL to navigate to
            name (str): Name for the screenshot file
            
        Returns:
            str: Path to the saved screenshot
        """
        if not self.driver:
            raise Exception("Chrome driver not initialized")
            
        try:
            # Navigate to URL
            self.driver.get(url)
            
            # Wait for page to load
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Additional wait for content to load
            time.sleep(3)
            
            # Get page dimensions
            total_width = self.driver.execute_script("return document.body.scrollWidth")
            total_height = self.driver.execute_script("return document.body.scrollHeight")
            
            # Set window size to capture full page
            self.driver.set_window_size(total_width, total_height)
            
            # Take screenshot
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}_webpage.png"
            filepath = os.path.join(self.screenshots_dir, filename)
            
            # Take screenshot using Selenium
            self.driver.save_screenshot(filepath)
            
            return filepath
            
        except Exception as e:
            raise Exception(f"Failed to take webpage screenshot for {url}: {str(e)}")
            
    def take_both_screenshots(self, url, name, wait_time=3):
        """
        Take both desktop and webpage screenshots
        
        Args:
            url (str): URL to navigate to
            name (str): Name for the screenshot files
            wait_time (int): Time to wait for page load
            
        Returns:
            tuple: Paths to desktop and webpage screenshots
        """
        try:
            # Take desktop screenshot
            desktop_path = self.take_screenshot(url, name, wait_time)
            
            # Take webpage screenshot
            webpage_path = self.take_webpage_screenshot(url, name)
            
            return desktop_path, webpage_path
            
        except Exception as e:
            raise Exception(f"Failed to take screenshots for {url}: {str(e)}")
            
    def scroll_and_screenshot(self, url, name):
        """
        Take multiple screenshots while scrolling through the page
        
        Args:
            url (str): URL to navigate to
            name (str): Name prefix for screenshot files
            
        Returns:
            list: Paths to all screenshot files
        """
        if not self.driver:
            raise Exception("Chrome driver not initialized")
            
        try:
            # Navigate to URL
            self.driver.get(url)
            
            # Wait for page to load
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            time.sleep(3)
            
            screenshot_paths = []
            
            # Get page height
            page_height = self.driver.execute_script("return document.body.scrollHeight")
            viewport_height = self.driver.execute_script("return window.innerHeight")
            
            # Take screenshot at top
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}_scroll_0.png"
            filepath = os.path.join(self.screenshots_dir, filename)
            
            screenshot = pyautogui.screenshot()
            screenshot.save(filepath)
            screenshot_paths.append(filepath)
            
            # Scroll and take screenshots
            scroll_position = 0
            scroll_step = viewport_height
            screenshot_count = 1
            
            while scroll_position < page_height:
                scroll_position += scroll_step
                self.driver.execute_script(f"window.scrollTo(0, {scroll_position});")
                time.sleep(1)
                
                filename = f"{name}_{timestamp}_scroll_{screenshot_count}.png"
                filepath = os.path.join(self.screenshots_dir, filename)
                
                screenshot = pyautogui.screenshot()
                screenshot.save(filepath)
                screenshot_paths.append(filepath)
                
                screenshot_count += 1
                
                # Prevent infinite scrolling
                if screenshot_count > 10:
                    break
                    
            return screenshot_paths
            
        except Exception as e:
            raise Exception(f"Failed to take scrolling screenshots for {url}: {str(e)}")
            
    def cleanup(self):
        """Close the Chrome driver"""
        if self.driver:
            try:
                self.driver.quit()
                self.driver = None
            except Exception as e:
                print(f"Error closing driver: {str(e)}")
                
    def __del__(self):
        """Cleanup when object is destroyed"""
        self.cleanup() 