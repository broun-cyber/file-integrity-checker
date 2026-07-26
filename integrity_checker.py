import hashlib
import os
import json

HASH_FILE = "hashes.json"


def calculate_hash(file_path):
    """Calculate SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(4096)

                if not chunk:
                    break

                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None


def load_hashes():
    """Load previously saved hashes."""
    if not os.path.exists(HASH_FILE):
        return {}

    try:
        with open(HASH_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


def save_hashes(hashes):
    """Save hashes to a JSON file."""
    with open(HASH_FILE, "w") as file:
        json.dump(hashes, file, indent=4)


print("=== File Integrity Checker ===")

file_path = input("Enter the file path: ").strip()

if not os.path.isfile(file_path):
    print("\n[ERROR] File not found.")

else:
    current_hash = calculate_hash(file_path)
    saved_hashes = load_hashes()

    print(f"\nFile: {file_path}")
    print(f"SHA-256: {current_hash}")

    if file_path not in saved_hashes:
        saved_hashes[file_path] = current_hash
        save_hashes(saved_hashes)

        print("\n[INFO] First scan completed.")
        print("File hash has been saved.")

    elif saved_hashes[file_path] == current_hash:
        print("\n[SAFE] File has not changed.")

    else:
        print("\n[WARNING] File has been modified!")
        print("Current hash does not match the saved hash.")