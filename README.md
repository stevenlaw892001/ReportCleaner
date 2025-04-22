# ReportCleaner

A Python tool for automating the cleanup of outdated system and network report files (XLS, XLSX, PDF) from specified directories, showcasing file handling, date manipulation, and error handling skills.

## Overview

`ReportCleaner` is a Python script designed to streamline the management of weekly system and network reports by automatically deleting outdated files based on dynamically generated date ranges. This project demonstrates proficiency in Python programming, including file system operations, date processing, and robust error handling. It is ideal for scenarios requiring automated cleanup of temporary or archival report files.

## Features

- **Dynamic Date Handling**: Generates file names based on the previous week's Monday-to-Friday range.
- **File Management**: Safely deletes specified XLS, XLSX, and PDF files from designated folders.
- **Cross-Platform Compatibility**: Uses `pathlib` for reliable path handling across Windows, Linux, and macOS.
- **Error Handling**: Includes comprehensive error checking and user feedback for file deletion operations.
- **Modular Design**: Organized with reusable functions and clear documentation for easy maintenance.

## Installation

### Prerequisites

- Python 3.6 or higher
- Required package: `python-dotenv`

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ReportCleaner.git
   cd ReportCleaner
   ```

2. Install the required package:

   ```bash
   pip install python-dotenv
   ```

3. Configure environment variables:

   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` to specify your folder paths, e.g.:
     ```
     RECORD_FOLDER=./data/reports
     DONE_FOLDER=./data/done
     ```

4. Ensure Python is installed:

   ```bash
   python --version
   ```

## Usage

1. **Prepare the Directory Structure**:

   - The script expects a `data/reports/` folder for report files and a `data/done/` folder for processed files, as specified in `.env`.
   - These folders are automatically created if they do not exist.

2. **Run the Script**:

   ```bash
   python report_cleaner.py
   ```

3. **Expected Output**: The script will:

   - Identify files from the previous week (e.g., `SystemA CPU Utilization 24Mar2025-28Mar2025.xls`).
   - Delete matching files in the `data/reports/` and `data/done/` folders.
   - Print feedback for each file (e.g., "Deleted: ...", "File not found: ...").

   Example output:

   ```
   Deleting files in data/reports...
   File not found: data/reports/SystemA CPU Utilization 24Mar2025-28Mar2025.xls
   Deleted: data/reports/Network Traffic for SystemA 2025-03-30.pdf
   ...
   Deletion process completed.
   ```

## Example File Names

The script targets files with names like:

- `SystemA CPU Utilization 24Mar2025-28Mar2025.xls`
- `Network Traffic for SystemA 2025-03-30.pdf`
- `SystemB Disk Utilization 24Mar2025-28Mar2025.xlsx`

## Project Structure

```
ReportCleaner/
├── data/                    # Placeholder for report files (not tracked in Git)
│   ├── reports/            # Directory for report files
│   └── done/               # Directory for processed files
├── report_cleaner.py       # Main Python script
├── README.md               # Project documentation
├── .env.example            # Environment variable template
├── .gitignore              # Git ignore rules
└── CODE_OF_CONDUCT.md      # Community standards
```

## Technical Highlights

This project showcases the following skills:

- **File System Operations**: Using `pathlib` for cross-platform file and directory management.
- **Date Manipulation**: Dynamic generation of date ranges with `datetime` and `timedelta`.
- **Error Handling**: Robust try-except blocks to handle file deletion errors gracefully.
- **Code Organization**: Modular functions with clear docstrings and comments for maintainability.
- **Automation**: Simplifies repetitive tasks, applicable to system administration or data management workflows.

## Contributing

Contributions are welcome! Please:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or suggestions, feel free to open an issue or contact me via GitHub.
