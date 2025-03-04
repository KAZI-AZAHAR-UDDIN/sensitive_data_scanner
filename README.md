<h1 align="center">Sensitive Data Scanner 🔍</h1>

## About This Project
A **Python script** designed to detect **sensitive data** (phone numbers and email addresses) in files. Built as an assignment for Rockfort AI, this tool supports multiple file formats and includes robust error handling, making it a practical security utility.

## Features
- 📂 **Multiple File Support**: Scans `.txt`, `.pdf`, `.csv`, and `.json` files.
- 🔍 **Sensitive Data Detection**: Identifies **phone numbers** (e.g., +919876543210, 123-456-7890) and **emails** (e.g., abc@example.com).
- 🚀 **Regex-Based Matching**: Uses regular expressions for accurate detection.
- 📊 **Error Handling**: Gracefully manages invalid formats, missing files, and corrupt data.

## Technologies Used
| Technology          | Purpose                              |
|---------------------|--------------------------------------|
| **Python**          | Core programming language            |
| **Regex (`re`)**    | Pattern matching for sensitive data  |
| **PyPDF2**          | Extracting text from PDF files       |
| **CSV Module**      | Processing CSV files                 |
| **JSON Module**     | Processing JSON files                |

## 🚀 Project Setup

### Requirements
- Python 3.6 or higher
- Dependency: `PyPDF2`

### 1️⃣ Clone the Repository
```
git clone https://github.com/KAZI-AZAHAR-UDDIN/sensitive-data-scanner.git
cd sensitive_data_scanner

```
2️⃣ Create Virtual Environment
```
python -m venv venv

```
Activate:
Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate

3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
4️⃣ Run the Script
Update file_path in sensitive_data_scanner.py with your file path (e.g., test_files/test.txt).
Run:
```
python sensitive_data_scanner.py
```
## 
Test Files
Included in test_files/:

test.txt: "My number is +919876543210 and email is abc@example.com"
sample.pdf: PDF with "Contact: 123-456-7890"
data.csv: CSV with "name,phone,email" and "Ram,+911234567890,ram@example.com"
info.json: JSON with {"name": "Shyam", "email": "shyam@example.com"}

Output
Sensitive Data Found: Sensitive data detected in the file.
No Sensitive Data: No sensitive data found in the file.
Errors: e.g., Error: File not found at test_files/test.txt
🔥 Key Highlights

🔥 Key Highlights
✅ Standalone Script: No web framework or database needed.

✅ Fast Execution: Efficient regex-based matching.

✅ Versatile: Works across TXT, PDF, CSV, and JSON.

✅ Robust: Comprehensive error handling.



## 👨‍💻 Author
**Kazi Azahar Uddin**  
*Software Engineer | Open to work*  

- **GitHub**: [KAZI-AZAHAR-UDDIN](https://github.com/KAZI-AZAHAR-UDDIN)  
- **LinkedIn**: [Kazi Azahar Uddin](https://www.linkedin.com/in/kazi-azahar-uddin-8b879b205/)  
