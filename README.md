# 🔐 File Integrity Checker

A Python-based cybersecurity project that uses **SHA-256 hashing** to detect unauthorized or unexpected changes in files.

The program creates a baseline hash for a file and compares it with the current hash during future scans.

## 🚀 Features

- Calculates SHA-256 hash of files
- Creates a baseline hash on the first scan
- Stores hashes locally using JSON
- Detects file modifications
- Identifies unchanged files
- Handles invalid file paths
- Simple command-line interface

## 🛠️ Technologies Used

- Python 3
- SHA-256
- `hashlib`
- JSON
- File Handling
- Git & GitHub

## ⚙️ How It Works

1. Select a file to check.
2. The program calculates its SHA-256 hash.
3. On the first scan, the hash is stored as a baseline.
4. On future scans, the current hash is compared with the saved hash.
5. The program reports whether the file has changed.

## ▶️ How to Run

Run:

    python integrity_checker.py

Then enter a file path:

    test.txt

### First Scan

    [INFO] First scan completed.
    File hash has been saved.

### File Unchanged

    [SAFE] File has not changed.

### File Modified

    [WARNING] File has been modified!
    Current hash does not match the saved hash.

## 🧠 What I Learned

Through this project, I practiced:

- SHA-256 hashing
- File integrity concepts
- Python file handling
- JSON data storage
- Functions and conditionals
- Git staging, commits, and pushes
- Using `.gitignore`

## 🔒 Security Note

This project is designed for educational purposes and demonstrates the basic concept of file integrity monitoring.

A hash mismatch indicates that file contents changed, but by itself does not prove that the change was malicious.

## 🔮 Future Improvements

- Monitor multiple files
- Monitor complete directories
- Add timestamps to scan results
- Create activity logs
- Add a GUI
- Add automatic monitoring

## 👨‍💻 Author

**Broun Verma**

Recruiter | BCA Student | Cybersecurity Learner
