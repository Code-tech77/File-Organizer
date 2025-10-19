
# File Organizer 🗂️  

### About  
File Organizer is a simple Python script that automatically sorts files in a chosen directory into subfolders based on their file extensions. It helps you declutter and manage your folders efficiently.  

***

### Features 🌟
- Automatically organizes files by type (e.g., images, documents, videos).  
- Creates new folders for extensions if they don’t already exist.  
- Moves files into their corresponding folders safely.  
- Works on Windows, macOS, and Linux.  

***

### How It Works  ⚙️
The script scans all files within a specified folder, checks each file’s extension, and then:  
1. Creates a new folder named after that extension (if it doesn’t already exist).  
2. Moves the file into the corresponding extension folder.  

Example:  
If your folder contains `photo.jpg`, `document.pdf`, and `script.py`, it will automatically create:  
```
jpg/
pdf/
py/
```
and move each file into its respective folder.  

***

### Requirements  
- Python 3.x  
- Standard libraries: `os`, `shutil` (no external dependencies)  

***

### Usage  
1. Clone this repository:
 
   ```bash
   git clone https://github.com/Code-tech77/File-Organizer.git
   ```
  
3. Open the folder and run the script:
    
   ```bash
   python file_organizer.py
   ```
  
5. Enter the full path to the folder you want to organize when prompted.  

Example:
```
Enter Folder Path: C:\Users\YourName\Downloads
```

The script will automatically organize all files in that directory by extension.  

***

### Example Output  
Before:  
```
Downloads/
├── file1.txt  
├── image1.png  
├── report.pdf  
```

After running the script:  
```
Downloads/
├── txt/
│   └── file1.txt
├── png/
│   └── image1.png
└── pdf/
    └── report.pdf
```

***

#### Feel free to connect with me on **LinkedIn** to collaborate or share feedback.

My Linkedin => https://www.linkedin.com/in/mohammed-zuoriki-856133250/

![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white) 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  
