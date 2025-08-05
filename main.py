"""
URL Screenshot Tool
Main GUI application for taking screenshots of URLs and saving them to DOCX files.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os
from datetime import datetime

from screenshot_manager import ScreenshotManager
from url_processor import URLProcessor
from docx_generator import DOCXGenerator


class URLScreenshotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Screenshot Tool")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Initialize managers
        self.screenshot_manager = ScreenshotManager()
        self.url_processor = URLProcessor()
        self.docx_generator = DOCXGenerator()
        
        # URL storage
        self.urls = []
        
        # Settings
        self.screenshots_location = tk.StringVar(value="screenshots")
        
        # Create GUI
        self.create_widgets()
        
    def create_widgets(self):
        """Create and arrange GUI widgets"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="URL Screenshot Tool", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Screenshot Location Section
        self.create_location_section(main_frame)
        
        # URL Input Section
        self.create_url_input_section(main_frame)
        
        # URL Display Section
        self.create_url_display_section(main_frame)
        
        # Control Section
        self.create_control_section(main_frame)
        
        # Progress Section
        self.create_progress_section(main_frame)
        
    def create_location_section(self, parent):
        """Create screenshot location section"""
        # Location Frame
        location_frame = ttk.LabelFrame(parent, text="Screenshot Location", padding="10")
        location_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        location_frame.columnconfigure(1, weight=1)
        
        # Screenshot location
        ttk.Label(location_frame, text="Screenshots Folder:").grid(row=0, column=0, sticky=tk.W, pady=5)
        
        folder_frame = ttk.Frame(location_frame)
        folder_frame.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        folder_frame.columnconfigure(0, weight=1)
        
        self.screenshots_entry = ttk.Entry(folder_frame, textvariable=self.screenshots_location)
        self.screenshots_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        
        ttk.Button(folder_frame, text="Browse", 
                  command=self.browse_screenshots_folder).grid(row=0, column=1)
        
    def create_url_input_section(self, parent):
        """Create URL input section"""
        # URL Input Frame
        url_frame = ttk.LabelFrame(parent, text="URL Input Options", padding="10")
        url_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        url_frame.columnconfigure(1, weight=1)
        
        # Manual input
        ttk.Label(url_frame, text="Manual Input:").grid(row=0, column=0, sticky=tk.W, pady=5)
        
        manual_frame = ttk.Frame(url_frame)
        manual_frame.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        manual_frame.columnconfigure(0, weight=1)
        
        # URL Name entry
        ttk.Label(manual_frame, text="URL Name:").grid(row=0, column=0, sticky=tk.W)
        self.url_name_entry = ttk.Entry(manual_frame, width=30)
        self.url_name_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 10))
        
        # URL entry
        ttk.Label(manual_frame, text="URL:").grid(row=1, column=0, sticky=tk.W)
        self.url_entry = ttk.Entry(manual_frame, width=50)
        self.url_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(5, 10), pady=(5, 0))
        
        # Add button
        add_btn = ttk.Button(manual_frame, text="Add URL", command=self.add_manual_url)
        add_btn.grid(row=1, column=2, padx=(5, 0), pady=(5, 0))
        
        # File input buttons
        ttk.Label(url_frame, text="File Input:").grid(row=1, column=0, sticky=tk.W, pady=(10, 5))
        
        file_frame = ttk.Frame(url_frame)
        file_frame.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 5))
        
        ttk.Button(file_frame, text="Load from TXT", 
                  command=self.load_from_txt).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(file_frame, text="Load from CSV", 
                  command=self.load_from_csv).grid(row=0, column=1, padx=5)
        ttk.Button(file_frame, text="Clear All URLs", 
                  command=self.clear_urls).grid(row=0, column=2, padx=(5, 0))
        
    def create_url_display_section(self, parent):
        """Create URL display section"""
        # URL Display Frame
        display_frame = ttk.LabelFrame(parent, text="Loaded URLs", padding="10")
        display_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        display_frame.columnconfigure(0, weight=1)
        display_frame.rowconfigure(0, weight=1)
        
        # URL listbox with scrollbar
        list_frame = ttk.Frame(display_frame)
        list_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        self.url_listbox = tk.Listbox(list_frame, height=8)
        self.url_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.url_listbox.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.url_listbox.configure(yscrollcommand=scrollbar.set)
        
        # Remove selected button
        ttk.Button(display_frame, text="Remove Selected", 
                  command=self.remove_selected_url).grid(row=1, column=0, pady=(10, 0))
        
    def create_control_section(self, parent):
        """Create control buttons section"""
        control_frame = ttk.LabelFrame(parent, text="Controls", padding="10")
        control_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Output file selection
        output_frame = ttk.Frame(control_frame)
        output_frame.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        output_frame.columnconfigure(1, weight=1)
        
        ttk.Label(output_frame, text="Output File:").grid(row=0, column=0, sticky=tk.W)
        self.output_file_var = tk.StringVar(value="screenshots.docx")
        output_entry = ttk.Entry(output_frame, textvariable=self.output_file_var)
        output_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 10))
        
        ttk.Button(output_frame, text="Browse", 
                  command=self.browse_output_file).grid(row=0, column=2)
        
        # Control buttons
        button_frame = ttk.Frame(control_frame)
        button_frame.grid(row=1, column=0, columnspan=3, pady=(10, 0))
        
        self.start_btn = ttk.Button(button_frame, text="Start Screenshot Process", 
                                   command=self.start_screenshot_process)
        self.start_btn.grid(row=0, column=0, padx=(0, 10))
        
        self.stop_btn = ttk.Button(button_frame, text="Stop Process", 
                                  command=self.stop_process, state=tk.DISABLED)
        self.stop_btn.grid(row=0, column=1)
        
    def create_progress_section(self, parent):
        """Create progress display section"""
        progress_frame = ttk.LabelFrame(parent, text="Progress", padding="10")
        progress_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
        progress_frame.columnconfigure(0, weight=1)
        progress_frame.rowconfigure(1, weight=1)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, 
                                           maximum=100)
        self.progress_bar.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Progress text
        self.progress_text = scrolledtext.ScrolledText(progress_frame, height=8, 
                                                      state=tk.DISABLED)
        self.progress_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
    def add_manual_url(self):
        """Add manually entered URL"""
        name = self.url_name_entry.get().strip()
        url = self.url_entry.get().strip()
        
        if not name or not url:
            messagebox.showerror("Error", "Please enter both URL name and URL")
            return
            
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        self.urls.append((name, url))
        self.update_url_display()
        
        # Clear entries
        self.url_name_entry.delete(0, tk.END)
        self.url_entry.delete(0, tk.END)
        
    def load_from_txt(self):
        """Load URLs from TXT file"""
        file_path = filedialog.askopenfilename(
            title="Select TXT file",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                new_urls = self.url_processor.load_from_txt(file_path)
                self.urls.extend(new_urls)
                self.update_url_display()
                self.log_message(f"Loaded {len(new_urls)} URLs from {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load TXT file: {str(e)}")
                
    def load_from_csv(self):
        """Load URLs from CSV file"""
        file_path = filedialog.askopenfilename(
            title="Select CSV file",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                new_urls = self.url_processor.load_from_csv(file_path)
                self.urls.extend(new_urls)
                self.update_url_display()
                self.log_message(f"Loaded {len(new_urls)} URLs from {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load CSV file: {str(e)}")
                
    def clear_urls(self):
        """Clear all URLs"""
        if self.urls and messagebox.askyesno("Confirm", "Clear all URLs?"):
            self.urls.clear()
            self.update_url_display()
            self.log_message("All URLs cleared")
            
    def remove_selected_url(self):
        """Remove selected URL from list"""
        selection = self.url_listbox.curselection()
        if selection:
            index = selection[0]
            removed_url = self.urls.pop(index)
            self.update_url_display()
            self.log_message(f"Removed: {removed_url[0]}")
            
    def update_url_display(self):
        """Update the URL listbox display"""
        self.url_listbox.delete(0, tk.END)
        for name, url in self.urls:
            self.url_listbox.insert(tk.END, f"{name} - {url}")
            
    def browse_output_file(self):
        """Browse for output file location"""
        file_path = filedialog.asksaveasfilename(
            title="Save DOCX file as",
            defaultextension=".docx",
            filetypes=[("Word documents", "*.docx"), ("All files", "*.*")]
        )
        
        if file_path:
            self.output_file_var.set(file_path)
            
    def browse_screenshots_folder(self):
        """Browse for screenshots folder location"""
        folder_path = filedialog.askdirectory(
            title="Select Screenshots Folder",
            initialdir=self.screenshots_location.get()
        )
        
        if folder_path:
            self.screenshots_location.set(folder_path)
            
    def start_screenshot_process(self):
        """Start the screenshot process in a separate thread"""
        if not self.urls:
            messagebox.showerror("Error", "Please add some URLs first")
            return
            
        output_file = self.output_file_var.get()
        if not output_file:
            messagebox.showerror("Error", "Please specify an output file")
            return
            
        # Disable start button, enable stop button
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        
        # Reset progress
        self.progress_var.set(0)
        self.clear_progress_text()
        
        # Start process in separate thread
        self.process_thread = threading.Thread(
            target=self.run_screenshot_process,
            args=(output_file,),
            daemon=True
        )
        self.process_thread.start()
        
    def run_screenshot_process(self, output_file):
        """Run the screenshot process"""
        try:
            self.log_message("Starting screenshot process...")
            
            # Update screenshot manager location and initialize
            screenshots_dir = self.screenshots_location.get()
            self.screenshot_manager.screenshots_dir = screenshots_dir
            self.screenshot_manager.setup_screenshots_directory()
            self.screenshot_manager.setup_driver()
            self.log_message("Chrome driver initialized")
            
            screenshots_data = []
            total_urls = len(self.urls)
            
            for i, (name, url) in enumerate(self.urls):
                if hasattr(self, 'stop_requested') and self.stop_requested:
                    break
                    
                self.log_message(f"Processing {i+1}/{total_urls}: {name}")
                
                try:
                    # Take screenshot
                    screenshot_path = self.screenshot_manager.take_screenshot(url, name)
                    screenshots_data.append((name, url, screenshot_path))
                    self.log_message(f"Screenshot taken: {name}")
                    
                except Exception as e:
                    self.log_message(f"Error taking screenshot for {name}: {str(e)}")
                    
                # Update progress
                progress = ((i + 1) / total_urls) * 100
                self.progress_var.set(progress)
                self.root.update_idletasks()
                
            # Generate DOCX
            if screenshots_data:
                self.log_message("Generating DOCX file...")
                self.docx_generator.create_document(screenshots_data, output_file)
                self.log_message(f"DOCX file created: {output_file}")
                messagebox.showinfo("Success", f"Screenshots saved to {output_file}")
            else:
                self.log_message("No screenshots were taken")
                messagebox.showwarning("Warning", "No screenshots were taken")
                
        except Exception as e:
            self.log_message(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Process failed: {str(e)}")
            
        finally:
            # Cleanup
            self.screenshot_manager.cleanup()
            
            # Re-enable buttons
            self.start_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)
            self.stop_requested = False
            
    def stop_process(self):
        """Stop the screenshot process"""
        self.stop_requested = True
        self.log_message("Stop requested...")
        
    def log_message(self, message):
        """Log message to progress text area"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        full_message = f"[{timestamp}] {message}\n"
        
        self.progress_text.config(state=tk.NORMAL)
        self.progress_text.insert(tk.END, full_message)
        self.progress_text.see(tk.END)
        self.progress_text.config(state=tk.DISABLED)
        self.root.update_idletasks()
        
    def clear_progress_text(self):
        """Clear progress text area"""
        self.progress_text.config(state=tk.NORMAL)
        self.progress_text.delete(1.0, tk.END)
        self.progress_text.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    app = URLScreenshotApp(root)
    root.mainloop()


if __name__ == "__main__":
    main() 