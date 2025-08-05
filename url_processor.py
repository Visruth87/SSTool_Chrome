"""
URL Processor
Handles loading URLs from different sources (TXT, CSV files).
"""

import csv
import pandas as pd
import os


class URLProcessor:
    def __init__(self):
        pass
        
    def load_from_txt(self, file_path):
        """
        Load URLs from a TXT file
        
        Expected format:
        - Each line: "URL_NAME|URL" or "URL_NAME,URL" or just "URL"
        - Lines starting with # are comments
        
        Args:
            file_path (str): Path to the TXT file
            
        Returns:
            list: List of tuples (name, url)
        """
        urls = []
        
        if not os.path.exists(file_path):
            raise Exception(f"File not found: {file_path}")
            
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    
                    # Skip empty lines and comments
                    if not line or line.startswith('#'):
                        continue
                        
                    # Try different separators
                    if '|' in line:
                        parts = line.split('|', 1)
                    elif ',' in line:
                        parts = line.split(',', 1)
                    elif '\t' in line:
                        parts = line.split('\t', 1)
                    else:
                        # Just URL, generate name
                        parts = [f"URL_{line_num}", line]
                        
                    if len(parts) >= 2:
                        name = parts[0].strip()
                        url = parts[1].strip()
                    else:
                        # Just URL
                        url = parts[0].strip()
                        name = f"URL_{line_num}"
                        
                    # Validate URL
                    if self._is_valid_url(url):
                        # Ensure URL has protocol
                        if not url.startswith(('http://', 'https://')):
                            url = 'https://' + url
                            
                        urls.append((name, url))
                    else:
                        print(f"Warning: Invalid URL on line {line_num}: {url}")
                        
        except Exception as e:
            raise Exception(f"Error reading TXT file: {str(e)}")
            
        return urls
        
    def load_from_csv(self, file_path):
        """
        Load URLs from a CSV file
        
        Expected format:
        - First column: URL name
        - Second column: URL
        - Header row is optional
        
        Args:
            file_path (str): Path to the CSV file
            
        Returns:
            list: List of tuples (name, url)
        """
        urls = []
        
        if not os.path.exists(file_path):
            raise Exception(f"File not found: {file_path}")
            
        try:
            # Try to read with pandas first
            df = pd.read_csv(file_path)
            
            # Check if we have at least 2 columns
            if len(df.columns) < 2:
                raise Exception("CSV file must have at least 2 columns (name, url)")
                
            # Use first two columns regardless of their names
            name_col = df.columns[0]
            url_col = df.columns[1]
            
            for index, row in df.iterrows():
                name = str(row[name_col]).strip()
                url = str(row[url_col]).strip()
                
                # Skip empty rows
                if pd.isna(row[name_col]) or pd.isna(row[url_col]):
                    continue
                    
                if not name or not url:
                    continue
                    
                # Validate URL
                if self._is_valid_url(url):
                    # Ensure URL has protocol
                    if not url.startswith(('http://', 'https://')):
                        url = 'https://' + url
                        
                    urls.append((name, url))
                else:
                    print(f"Warning: Invalid URL on row {index + 2}: {url}")
                    
        except pd.errors.EmptyDataError:
            raise Exception("CSV file is empty")
        except pd.errors.ParserError as e:
            # Fallback to manual CSV parsing
            try:
                urls = self._manual_csv_parse(file_path)
            except Exception as fallback_error:
                raise Exception(f"Error parsing CSV file: {str(e)}")
        except Exception as e:
            raise Exception(f"Error reading CSV file: {str(e)}")
            
        return urls
        
    def _manual_csv_parse(self, file_path):
        """
        Manual CSV parsing as fallback
        
        Args:
            file_path (str): Path to the CSV file
            
        Returns:
            list: List of tuples (name, url)
        """
        urls = []
        
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            
            for row_num, row in enumerate(csv_reader, 1):
                if len(row) < 2:
                    continue
                    
                name = row[0].strip()
                url = row[1].strip()
                
                # Skip header-like rows
                if row_num == 1 and (name.lower() in ['name', 'title', 'url_name'] or
                                    url.lower() in ['url', 'link', 'website']):
                    continue
                    
                if not name or not url:
                    continue
                    
                # Validate URL
                if self._is_valid_url(url):
                    # Ensure URL has protocol
                    if not url.startswith(('http://', 'https://')):
                        url = 'https://' + url
                        
                    urls.append((name, url))
                else:
                    print(f"Warning: Invalid URL on row {row_num}: {url}")
                    
        return urls
        
    def _is_valid_url(self, url):
        """
        Basic URL validation
        
        Args:
            url (str): URL to validate
            
        Returns:
            bool: True if URL appears valid
        """
        if not url:
            return False
            
        # Remove protocol for validation
        clean_url = url
        if url.startswith(('http://', 'https://')):
            clean_url = url[url.find('://') + 3:]
            
        # Basic checks
        if not clean_url:
            return False
            
        # Must contain at least one dot (domain.tld)
        if '.' not in clean_url:
            return False
            
        # Check for common invalid characters at start
        if clean_url.startswith(('.', '/', '@')):
            return False
            
        # Check for spaces (usually indicates invalid URL)
        if ' ' in clean_url.replace('%20', ''):
            return False
            
        return True
        
    def create_sample_txt_file(self, file_path="sample_urls.txt"):
        """
        Create a sample TXT file with example URLs
        
        Args:
            file_path (str): Path where to create the sample file
        """
        sample_content = """# Sample URL file
# Format: NAME|URL or NAME,URL or just URL
# Lines starting with # are comments

Google|https://www.google.com
GitHub|https://github.com
Stack Overflow,https://stackoverflow.com
https://www.python.org
Wikipedia|https://www.wikipedia.org
Reddit,https://www.reddit.com
"""
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(sample_content)
            
        return file_path
        
    def create_sample_csv_file(self, file_path="sample_urls.csv"):
        """
        Create a sample CSV file with example URLs
        
        Args:
            file_path (str): Path where to create the sample file
        """
        sample_data = [
            ["Name", "URL"],
            ["Google", "https://www.google.com"],
            ["GitHub", "https://github.com"],
            ["Stack Overflow", "https://stackoverflow.com"],
            ["Python", "https://www.python.org"],
            ["Wikipedia", "https://www.wikipedia.org"],
            ["Reddit", "https://www.reddit.com"]
        ]
        
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(sample_data)
            
        return file_path
        
    def export_to_txt(self, urls, file_path):
        """
        Export URLs to TXT file
        
        Args:
            urls (list): List of tuples (name, url)
            file_path (str): Output file path
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("# Exported URLs\n")
            file.write("# Format: NAME|URL\n\n")
            
            for name, url in urls:
                file.write(f"{name}|{url}\n")
                
    def export_to_csv(self, urls, file_path):
        """
        Export URLs to CSV file
        
        Args:
            urls (list): List of tuples (name, url)
            file_path (str): Output file path
        """
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "URL"])
            
            for name, url in urls:
                writer.writerow([name, url]) 