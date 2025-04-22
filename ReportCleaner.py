import os
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration: Define folder paths from environment variables
RECORD_FOLDER = Path(os.getenv("RECORD_FOLDER", "./data/reports"))
DONE_FOLDER = Path(os.getenv("DONE_FOLDER", "./data/done"))

def get_last_week_range():
    """
    Calculate the date range for last Monday to Friday.
    Returns:
        tuple: (start_date, end_date) in MM/DD/YYYY format.
    """
    today = datetime.now()
    days_to_last_monday = today.weekday()  # Days since last Monday (0 = Monday)
    last_monday = today - timedelta(days=days_to_last_monday)
    last_friday = last_monday + timedelta(days=4)
    return last_monday.strftime("%m/%d/%Y"), last_friday.strftime("%m/%d/%Y")

def format_date_for_filename(date_str):
    """
    Convert a date string from MM/DD/YYYY to DDMonYYYY format for filenames.
    Args:
        date_str (str): Date in MM/DD/YYYY format.
    Returns:
        str: Date in DDMonYYYY format (e.g., 24Mar2025).
    """
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")
    return date_obj.strftime("%d%b%Y")

def delete_files(folder_path, file_list):
    """
    Delete specified files in the given folder with error handling.
    Args:
        folder_path (Path): Path to the folder containing files.
        file_list (list): List of filenames to delete.
    """
    print(f"Deleting files in {folder_path}...")
    for file_name in file_list:
        file_path = folder_path / file_name
        try:
            if file_path.exists():
                file_path.unlink()  # Delete the file
                print(f"Deleted: {file_path}")
            else:
                print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

def main():
    """Main function to orchestrate the report file cleanup process."""
    # Get date range for last week
    start_date, end_date = get_last_week_range()
    start_str = format_date_for_filename(start_date)  # e.g., "24Mar2025"
    end_str = format_date_for_filename(end_date)      # e.g., "28Mar2025"

    # Get current date for network traffic reports
    today_date = datetime.now().strftime("%Y-%m-%d")  # e.g., "2025-03-30"

    # Define files to delete in the reports folder
    record_files_to_delete = [
        f"SystemA CPU Utilization {start_str}-{end_str}.xls",
        f"SystemA Disk Utilization {start_str}-{end_str}.xls",
        f"SystemB CPU Utilization {start_str}-{end_str}.xls",
        f"SystemB Disk Utilization {start_str}-{end_str}.xls",
        f"Network Traffic for SystemA {today_date}.pdf",
        f"Network Traffic for DMZ {today_date}.pdf",
        f"Network Traffic for Combined {today_date}.pdf"
    ]

    # Define files to delete in the done folder
    done_files_to_delete = [
        f"SystemA CPU Utilization {start_str}-{end_str}.xlsx",
        f"SystemA Disk Utilization {start_str}-{end_str}.xlsx",
        f"SystemB CPU Utilization {start_str}-{end_str}.xlsx",
        f"SystemB Disk Utilization {start_str}-{end_str}.xlsx"
    ]

    # Ensure directories exist
    RECORD_FOLDER.mkdir(parents=True, exist_ok=True)
    DONE_FOLDER.mkdir(parents=True, exist_ok=True)

    # Delete files in both folders
    delete_files(RECORD_FOLDER, record_files_to_delete)
    delete_files(DONE_FOLDER, done_files_to_delete)

    print("\nDeletion process completed.")

if __name__ == "__main__":
    main()
