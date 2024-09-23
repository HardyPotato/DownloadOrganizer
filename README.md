# Download Folder Organizer

This Python script automatically organizes files in your Downloads folder into categorized subfolders based on their file type (extension). Files that don't match predefined categories are moved to a `General` folder.

## Features

- Automatically organizes files into predefined categories:
  - **Documents**: `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`
  - **Music**: `.mp3`, `.wav`, `.aac`, `.flac`
  - **Videos**: `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`
  - **Programs**: `.exe`, `.msi`, `.bat`, `.sh`
  - **Compressed**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
  - **Pictures**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`
  - **Technical**: `.ps1`, `.reg`, `.py`, `.js`, `.html`, `.htm`, `.css`, `.xml`, `.json`, `.cfg`, `.conf`, `.log`
- Moves all uncategorized files and folders into a **General** folder.
- Skips already organized files or folders to avoid unnecessary operations.

## Usage

1. Clone the repository.
2. Modify the `download_folder` path in the script to point to your Downloads folder.
3. Run the script:

```bash
python DownloadOrganizer.py
