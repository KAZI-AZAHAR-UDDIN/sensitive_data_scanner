import re
import os
import csv
import json
import argparse
import logging
from PyPDF2 import PdfReader

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Stronger Regular Expressions for Phone Numbers and Emails
PHONE_REGEX = r'(\+\d{1,3}[-.\s]?\d{10})|\d{3}-\d{3}-\d{4}|\(\d{3}\)\s*\d{3}-\d{4}|\b\d{10}\b'
EMAIL_REGEX = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

def find_sensitive_data(text):
    """Check if text contains phone numbers or email addresses."""
    return bool(re.search(PHONE_REGEX, text) or re.search(EMAIL_REGEX, text))

def read_txt(file_path):
    """Read text from a TXT file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        logging.error(f"Could not read TXT file: {e}")
        return None

def read_pdf(file_path):
    """Extract text from a PDF file."""
    try:
        reader = PdfReader(file_path)
        text = "\n".join([page.extract_text() or "" for page in reader.pages])
        return text
    except Exception as e:
        logging.error(f"Could not read PDF file: {e}")
        return None

def read_csv(file_path):
    """Read all columns from a CSV file."""
    try:
        text = []
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                text.append(" ".join(row))
        return "\n".join(text)
    except Exception as e:
        logging.error(f"Could not read CSV file: {e}")
        return None

def read_json(file_path):
    """Extract all string values from a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return json.dumps(data)  # Convert JSON object to string
    except Exception as e:
        logging.error(f"Could not read JSON file: {e}")
        return None

def scan_file(file_path):
    """Scan a single file for sensitive data."""
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        return
    
    ext = file_path.lower().split('.')[-1]
    text_to_scan = ""

    if ext == "txt":
        text_to_scan = read_txt(file_path)
    elif ext == "pdf":
        text_to_scan = read_pdf(file_path)
    elif ext == "csv":
        text_to_scan = read_csv(file_path)
    elif ext == "json":
        text_to_scan = read_json(file_path)
    else:
        logging.error(f"Unsupported file format: {file_path}")
        return

    if text_to_scan is None:
        logging.error(f"Could not process the file: {file_path}")
        return

    if text_to_scan.strip() == "":  # Check if file is empty
        logging.warning(f"Empty file: {file_path}")
        return

    if find_sensitive_data(text_to_scan):
        logging.info(f"Sensitive data detected in: {file_path}")
    else:
        logging.info(f"No sensitive data found in: {file_path}")

def scan_folder(folder_path):
    """Scan all files in a folder for sensitive data."""
    if not os.path.exists(folder_path):
        logging.error(f"Folder not found: {folder_path}")
        return

    files = os.listdir(folder_path)
    supported_files = [f for f in files if f.endswith((".txt", ".pdf", ".csv", ".json"))]

    if not supported_files:
        logging.warning("No supported files found in the folder.")
        return

    for file in supported_files:
        scan_file(os.path.join(folder_path, file))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect sensitive data in files")
    parser.add_argument("path", help="Path to a file or folder")
    args = parser.parse_args()

    if os.path.isdir(args.path):
        scan_folder(args.path)
    else:
        scan_file(args.path)
