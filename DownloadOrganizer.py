import os
import shutil

# Define the paths and categories
download_folder = 'D:\Downloads'  # Replace with the path to your download folder
categories = {
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
    'Programs': ['.exe', '.msi', '.bat', '.sh'],
    'Compressed': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Pictures': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'Technical': ['.ps1', '.reg', '.py', '.js', '.html', '.htm', '.css', '.xml', '.json', '.cfg', '.conf', '.log'],
    'Exclusion': [],
}

# Create category folders if they don't exist
for category in categories:
    folder_path = os.path.join(download_folder, category)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Create General folder
general_folder = os.path.join(download_folder, 'General')
if not os.path.exists(general_folder):
    os.makedirs(general_folder)

# Move files into their respective categories
for item in os.listdir(download_folder):
    item_path = os.path.join(download_folder, item)
    
    # Skip the category and General folders
    if item in categories.keys() or item == 'General':
        continue
    
    # Handle files
    if os.path.isfile(item_path):
        file_extension = os.path.splitext(item)[1].lower()
        moved = False
        for category, extensions in categories.items():
            if file_extension in extensions:
                shutil.move(item_path, os.path.join(download_folder, category, item))
                moved = True
                break
        if not moved:
            shutil.move(item_path, os.path.join(general_folder, item))
    
    # Handle folders
    elif os.path.isdir(item_path):
        shutil.move(item_path, os.path.join(general_folder, item))

print("Files and folders have been organized.")
