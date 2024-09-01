# 🗑️ AutoTrashCleaner - Python Project

This project automatically deletes all files in a specified folder every 4 hours, helping you manage temporary files or maintain a clean directory. Ideal for folders used as temporary storage or a makeshift trash bin.

## 🔧 Built By

**Bhavya Padaliya**  
GitHub: [github.com/bhavyax7673](https://github.com/bhavyax7673)

## 🚀 Features

- **Automatic Deletion**: Deletes all files in the specified folder every 4 hours.
- **Customizable Folder**: Easily specify any folder to act as your auto-trash bin.
- **Recycle Bin Cleanup**: Empties the Windows Recycle Bin after file deletion.

## 🛠️ Installation

### 1. Install Python

Make sure you have Python installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/). During installation, make sure to check the option to "Add Python to PATH."

### 2. Install Required Libraries

This project requires the `winshell` library. Install it using pip:

```python
pip install winshell
```

### 3. Clone This Repository

Use Git to clone the repository to your local machine:

```git
git clone https://github.com/bhavyax7673/auto-trash-cleaner.git
cd auto-trash-cleaner
```

## 📁 Usage

### 1. Edit the Script: In the main.py file, you can change the folder variable to point to the folder you want to use as a trash bin.

```python
folder = "your/path/to/folder"
```

- Note Use Absolute Path Like "E://TRASH" For The Location Outside Of Current Repo

### 2. Run the Script: Run the script manually or set it to run in the background.

1. Manually

```bash
python main.py
```

2. Set It In The Background

```bash
pythonw main.py
```

## ⚙️ How It Works

- The script runs an infinite loop, checking the folder every 4 hours.
- It deletes all files in the specified folder, except for README.md, .git, and main.py files.
- After deleting the files, it empties the Windows Recycle Bin.

## 👤 About Me

- I'm Bhavya Padaliya, a passionate Computer Science Student working on various projects to enhance my skills. This Auto Trash Cleaner is a simple yet powerful tool to help manage temporary files. Feel free to check out my other projects on GitHub.
