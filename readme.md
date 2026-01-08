Sales Data Automation Script (Python)

Overview:
This project is a Python-based automation script that processes large CSV sales data files, validates records, handles errors, and generates summarized reports in both text and Excel formats.

It is designed to demonstrate real-world automation skills commonly required in freelance and entry-level Python roles.

Features:
1.Reads and processes CSV sales data
2.Performs data validation (quantity, price, missing fields)
3.Logs invalid rows with timestamps
4.Generates daily summary reports in .txt format
5.Generates Excel summary reports using openpyxl
6.Automatically creates required output folders
7.Modular and reusable code structure

Project Structure:
.
├── Input/
│   └── sales.csv
├── Output/
│   ├── report_YYYY-MM-DD.txt
│   └── Summary Report.xlsx
├── Logs/
│   └── errors.txt
├── main.py
├── .gitignore
└── README.md

Technologies Used:
1.Python 3
2.csv (standard library)
3.os (standard library)
4.datetime (standard library)
5.openpyxl

How It Works:
1.Reads data from Input/sales.csv
2.Skips headers and validates rows
3.Calculates total sales per product
4.Logs errors without stopping execution
5.Generates summary reports in:
6.Text format
7.Excel format

How to Run:

Install dependencies:
pip install openpyxl
Place your CSV file inside the Input folder

Run the script:

python main.py

Use Cases
1.Sales report automation
2.Data cleaning and validation
3.CSV to Excel conversion
4.Reporting workflows
5.Freelance automation tasks

Author

Muhammad Fahad Arshad
Junior Python Developer | Automation Enthusiast
