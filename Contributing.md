# Contributing to ReportCleaner

Thank you for considering contributing to `ReportCleaner`! This project automates the cleanup of outdated system and network report files, and we welcome contributions to improve its functionality, documentation, or usability.

## How to Contribute

### 1. Setting Up the Development Environment

- **Prerequisites**: Python 3.6 or higher and `python-dotenv` (see `requirements.txt`).
- **Steps**:
  1. Clone the repository:
     ```bash
     git clone https://github.com/your-username/ReportCleaner.git
     cd ReportCleaner
     ```
  2. Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
  3. Copy `.env.example` to `.env` and configure paths:
     ```bash
     cp .env.example .env
     ```
     Edit `.env` with your folder paths (e.g., `RECORD_FOLDER=./data/reports`).

### 2. Reporting Issues

If you find bugs or have feature suggestions, please:
- Check the [GitHub Issues](https://github.com/your-username/ReportCleaner/issues) page to avoid duplicates.
- Open a new issue with a clear title and description, including:
  - Steps to reproduce (for bugs).
  - Expected and actual behavior.
  - Your environment (e.g., Python version, OS).

### 3. Submitting Changes

To contribute code or documentation:
1. Fork the repository and create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
2. Make your changes, ensuring they follow the project's coding style (PEP 8).
3. Test your changes locally:
   ```bash
   python report_cleaner.py
   ```
4. Commit your changes with a clear message:
   ```bash
   git commit -m "Add your feature or fix description"
   ```
5. Push to your fork:
   ```bash
   git push origin feature/your-feature
   ```
6. Open a pull request (PR) with:
   - A detailed description of your changes.
   - Reference to related issues (if any).

### 4. Coding Guidelines

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
- Include docstrings for new functions and comments for complex logic.
- Ensure your changes are compatible with the existing `.env` configuration.
- Avoid committing sensitive data (e.g., `.env` or report files).

### 5. Code of Conduct

All contributors are expected to adhere to the [Code of Conduct](CODE_OF_CONDUCT.md). Please be respectful and inclusive in all interactions.

## Getting Help

For questions or clarification, feel free to:
- Open an issue on GitHub.
- Contact the maintainer via GitHub messages.

Thank you for helping make `ReportCleaner` better!